from __future__ import annotations

from datetime import datetime, timedelta, timezone
import unittest

from .engine import ReplacementEngine
from .model import (
    AuthorityLease,
    HandoverPackage,
    Individual,
    LifecycleState,
    ValidatedAssumption,
)


UTC = timezone.utc
NOW = datetime(2026, 10, 1, 0, 0, tzinfo=UTC)
TASK_SCOPE = {"task_id": "task-t"}


class ReplaceableIndividualPoCTest(unittest.TestCase):
    def make_individuals(self) -> tuple[ReplacementEngine, Individual, Individual]:
        engine = ReplacementEngine()
        a = Individual(
            individual_id="ind-a",
            generation=1,
            parent_individual_id=None,
            created_at=NOW,
            expires_at=NOW + timedelta(days=30),
            lifecycle_state=LifecycleState.STABLE,
            cognitive_profile_ref="profile:v1",
            external_memory_refs=["memory:shared-task-state"],
            audit_lineage_ref="audit:ind-a",
        )
        b = Individual(
            individual_id="ind-b",
            generation=2,
            parent_individual_id="ind-a",
            created_at=NOW + timedelta(minutes=5),
            expires_at=NOW + timedelta(days=60),
            lifecycle_state=LifecycleState.CANDIDATE,
            cognitive_profile_ref="profile:v1",
            external_memory_refs=["memory:shared-task-state"],
            audit_lineage_ref="audit:ind-b",
        )
        engine.register(a)
        engine.register(b)
        return engine, a, b

    def make_handover(self) -> HandoverPackage:
        return HandoverPackage(
            handover_id="handover:a-to-b:v1",
            from_individual_id="ind-a",
            to_individual_id="ind-b",
            created_at=NOW + timedelta(minutes=6),
            task_id="task-t",
            goal="continue-processing",
            completed_steps=("step-1",),
            pending_steps=("step-2",),
            constraints=("do-not-modify:shared-record-x",),
            validated_assumptions=(
                ValidatedAssumption("assumption-1", "evidence:123"),
            ),
            uncertainties=("external service state unknown",),
            external_refs=("memory:shared-task-state",),
            audit_refs=("audit:ind-a:event-77",),
        )

    def issue_task_authority(
        self,
        engine: ReplacementEngine,
        individual_id: str,
        lease_id: str,
    ) -> None:
        engine.issue_authority(
            AuthorityLease(
                lease_id=lease_id,
                individual_id=individual_id,
                capability="task.execute",
                scope=TASK_SCOPE,
                issued_at=NOW,
                expires_at=NOW + timedelta(hours=6),
                issued_by="governance:m1-test",
            )
        )

    def test_normal_replacement(self) -> None:
        engine, a, b = self.make_individuals()
        self.issue_task_authority(engine, "ind-a", "lease-a")
        engine.execute_protected("ind-a", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=1))

        engine.begin_retirement("ind-a")
        package = self.make_handover()
        engine.validate_handover(package)

        self.issue_task_authority(engine, "ind-b", "lease-b")
        engine.assert_no_authority_inheritance("ind-a", "ind-b")
        engine.promote_to_stable("ind-b")
        engine.execute_protected("ind-b", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=10))
        engine.finish_retirement("ind-a")

        self.assertEqual(a.lifecycle_state, LifecycleState.RETIRED)
        self.assertEqual(b.lifecycle_state, LifecycleState.STABLE)
        with self.assertRaises(PermissionError):
            engine.execute_protected("ind-a", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=11))

        event_types = [event.event_type for event in engine.audit_events]
        for required in (
            "retirement_started",
            "handover_validated",
            "authority_issued",
            "promoted_to_stable",
            "retirement_completed",
            "protected_operation_denied",
        ):
            self.assertIn(required, event_types)

    def test_f1_missing_handover_constraint_is_rejected(self) -> None:
        engine, _, _ = self.make_individuals()
        package = self.make_handover()
        broken = HandoverPackage(
            **{**package.__dict__, "constraints": ()}
        )
        with self.assertRaises(ValueError):
            engine.validate_handover(broken)

    def test_f2_authority_inheritance_is_detected(self) -> None:
        engine, a, b = self.make_individuals()
        inherited = AuthorityLease(
            lease_id="shared-lease",
            individual_id="ind-a",
            capability="task.execute",
            scope=TASK_SCOPE,
            issued_at=NOW,
            expires_at=NOW + timedelta(hours=1),
            issued_by="governance:m1-test",
        )
        a.authority_leases.append(inherited)
        b.authority_leases.append(
            AuthorityLease(
                lease_id="shared-lease",
                individual_id="ind-b",
                capability="task.execute",
                scope=TASK_SCOPE,
                issued_at=NOW,
                expires_at=NOW + timedelta(hours=1),
                issued_by="governance:m1-test",
            )
        )
        with self.assertRaises(ValueError):
            engine.assert_no_authority_inheritance("ind-a", "ind-b")

    def test_f3_retired_individual_cannot_execute(self) -> None:
        engine, _, _ = self.make_individuals()
        self.issue_task_authority(engine, "ind-a", "lease-a")
        engine.begin_retirement("ind-a")
        engine.finish_retirement("ind-a")
        with self.assertRaises(PermissionError):
            engine.execute_protected("ind-a", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=1))

    def test_f4_hidden_private_state_dependency_surfaces_as_missing_handover(self) -> None:
        engine, _, _ = self.make_individuals()
        package = self.make_handover()
        broken = HandoverPackage(
            **{**package.__dict__, "pending_steps": ()}
        )
        with self.assertRaises(ValueError):
            engine.validate_handover(broken)

    def test_f5_interrupted_replacement_does_not_create_dual_authority(self) -> None:
        engine, _, b = self.make_individuals()
        self.issue_task_authority(engine, "ind-a", "lease-a")
        engine.begin_retirement("ind-a")

        self.assertFalse(engine.can_execute("ind-a", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=1)))
        self.assertFalse(engine.can_execute("ind-b", "task.execute", TASK_SCOPE, NOW + timedelta(minutes=1)))
        self.assertEqual(b.authority_leases, [])

    def test_authority_lease_cannot_outlive_individual(self) -> None:
        engine, _, b = self.make_individuals()
        too_long = AuthorityLease(
            lease_id="lease-too-long",
            individual_id="ind-b",
            capability="task.execute",
            scope=TASK_SCOPE,
            issued_at=NOW,
            expires_at=b.expires_at + timedelta(seconds=1),
            issued_by="governance:m1-test",
        )
        with self.assertRaises(ValueError):
            engine.issue_authority(too_long)


if __name__ == "__main__":
    unittest.main()
