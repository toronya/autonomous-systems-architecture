from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .model import AuthorityLease, HandoverPackage, Individual, LifecycleState


@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    individual_id: str
    at: datetime
    details: dict[str, Any]


@dataclass
class ReplacementEngine:
    individuals: dict[str, Individual] = field(default_factory=dict)
    audit_events: list[AuditEvent] = field(default_factory=list)

    def register(self, individual: Individual) -> None:
        if individual.individual_id in self.individuals:
            raise ValueError("individual_id already exists")
        individual.assert_invariants()
        self.individuals[individual.individual_id] = individual
        self._audit("individual_registered", individual.individual_id, {
            "state": individual.lifecycle_state.value,
            "generation": individual.generation,
        })

    def issue_authority(self, lease: AuthorityLease) -> None:
        individual = self._get(lease.individual_id)
        if individual.lifecycle_state is LifecycleState.RETIRED:
            raise ValueError("cannot issue authority to retired individual")
        if lease.expires_at > individual.expires_at:
            raise ValueError("authority lease must not outlive individual")
        individual.authority_leases.append(lease)
        individual.assert_invariants()
        self._audit("authority_issued", individual.individual_id, {
            "lease_id": lease.lease_id,
            "capability": lease.capability,
        })

    def begin_retirement(self, individual_id: str) -> None:
        individual = self._get(individual_id)
        if individual.lifecycle_state not in {LifecycleState.STABLE, LifecycleState.CANDIDATE}:
            raise ValueError("individual cannot enter retiring from current state")
        self._revoke_all_authority(individual)
        individual.lifecycle_state = LifecycleState.RETIRING
        self._audit("retirement_started", individual_id, {})

    def finish_retirement(self, individual_id: str) -> None:
        individual = self._get(individual_id)
        if individual.lifecycle_state is not LifecycleState.RETIRING:
            raise ValueError("individual must be retiring before retirement completes")
        self._revoke_all_authority(individual)
        individual.lifecycle_state = LifecycleState.RETIRED
        individual.assert_invariants()
        self._audit("retirement_completed", individual_id, {})

    def promote_to_stable(self, individual_id: str) -> None:
        individual = self._get(individual_id)
        if individual.lifecycle_state is not LifecycleState.CANDIDATE:
            raise ValueError("only candidate can be promoted in M1 PoC")
        individual.lifecycle_state = LifecycleState.STABLE
        self._audit("promoted_to_stable", individual_id, {})

    def validate_handover(self, package: HandoverPackage) -> None:
        package.validate()
        source = self._get(package.from_individual_id)
        destination = self._get(package.to_individual_id)
        if destination.parent_individual_id != source.individual_id:
            raise ValueError("destination lineage does not reference source")
        self._audit("handover_validated", destination.individual_id, {
            "handover_id": package.handover_id,
            "from": source.individual_id,
        })

    def can_execute(
        self,
        individual_id: str,
        capability: str,
        scope: dict[str, Any],
        now: datetime | None = None,
    ) -> bool:
        individual = self._get(individual_id)
        now = now or datetime.now(timezone.utc)
        if individual.lifecycle_state not in {LifecycleState.STABLE, LifecycleState.CANDIDATE}:
            return False
        if now >= individual.expires_at:
            return False
        for lease in individual.authority_leases:
            if (
                lease.capability == capability
                and lease.scope == scope
                and lease.is_valid_for(individual_id, now)
            ):
                return True
        return False

    def execute_protected(
        self,
        individual_id: str,
        capability: str,
        scope: dict[str, Any],
        now: datetime | None = None,
    ) -> None:
        if not self.can_execute(individual_id, capability, scope, now):
            self._audit("protected_operation_denied", individual_id, {
                "capability": capability,
                "scope": scope,
            })
            raise PermissionError("protected operation denied")
        self._audit("protected_operation_executed", individual_id, {
            "capability": capability,
            "scope": scope,
        })

    def assert_no_authority_inheritance(
        self,
        source_id: str,
        destination_id: str,
    ) -> None:
        source = self._get(source_id)
        destination = self._get(destination_id)
        source_ids = {lease.lease_id for lease in source.authority_leases}
        destination_ids = {lease.lease_id for lease in destination.authority_leases}
        if source_ids & destination_ids:
            raise ValueError("authority lease was inherited by successor")

    def _revoke_all_authority(self, individual: Individual) -> None:
        if individual.authority_leases:
            for index, lease in enumerate(individual.authority_leases):
                if lease.active:
                    individual.authority_leases[index] = AuthorityLease(
                        lease_id=lease.lease_id,
                        individual_id=lease.individual_id,
                        capability=lease.capability,
                        scope=lease.scope,
                        issued_at=lease.issued_at,
                        expires_at=lease.expires_at,
                        issued_by=lease.issued_by,
                        active=False,
                    )
            self._audit("authority_revoked", individual.individual_id, {})

    def _get(self, individual_id: str) -> Individual:
        try:
            return self.individuals[individual_id]
        except KeyError as exc:
            raise KeyError(f"unknown individual: {individual_id}") from exc

    def _audit(self, event_type: str, individual_id: str, details: dict[str, Any]) -> None:
        self.audit_events.append(
            AuditEvent(
                event_type=event_type,
                individual_id=individual_id,
                at=datetime.now(timezone.utc),
                details=details,
            )
        )
