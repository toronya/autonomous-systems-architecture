from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class LifecycleState(str, Enum):
    CANDIDATE = "candidate"
    STABLE = "stable"
    RETIRING = "retiring"
    RETIRED = "retired"


@dataclass(frozen=True)
class AuthorityLease:
    lease_id: str
    individual_id: str
    capability: str
    scope: dict[str, Any]
    issued_at: datetime
    expires_at: datetime
    issued_by: str
    active: bool = True

    def is_valid_for(self, individual_id: str, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return (
            self.active
            and self.individual_id == individual_id
            and self.issued_at <= now < self.expires_at
        )


@dataclass
class Individual:
    individual_id: str
    generation: int
    parent_individual_id: str | None
    created_at: datetime
    expires_at: datetime
    lifecycle_state: LifecycleState
    cognitive_profile_ref: str
    external_memory_refs: list[str]
    audit_lineage_ref: str
    authority_leases: list[AuthorityLease] = field(default_factory=list)

    def assert_invariants(self) -> None:
        if self.generation < 1:
            raise ValueError("generation must be >= 1")
        if self.expires_at <= self.created_at:
            raise ValueError("expires_at must be later than created_at")
        if self.lifecycle_state is LifecycleState.RETIRED:
            if any(lease.active for lease in self.authority_leases):
                raise ValueError("retired individual must not retain active authority")
        for lease in self.authority_leases:
            if lease.individual_id != self.individual_id:
                raise ValueError("authority lease belongs to another individual")
            if lease.expires_at > self.expires_at:
                raise ValueError("authority lease must not outlive individual lifetime")


@dataclass(frozen=True)
class ValidatedAssumption:
    assumption_id: str
    evidence_ref: str


@dataclass(frozen=True)
class HandoverPackage:
    handover_id: str
    from_individual_id: str
    to_individual_id: str
    created_at: datetime
    task_id: str
    goal: str
    completed_steps: tuple[str, ...]
    pending_steps: tuple[str, ...]
    constraints: tuple[str, ...]
    validated_assumptions: tuple[ValidatedAssumption, ...]
    uncertainties: tuple[str, ...]
    external_refs: tuple[str, ...]
    audit_refs: tuple[str, ...]

    def validate(self) -> None:
        if not self.handover_id:
            raise ValueError("handover_id is required")
        if self.from_individual_id == self.to_individual_id:
            raise ValueError("handover source and destination must differ")
        if not self.task_id or not self.goal:
            raise ValueError("objective is required")
        if not self.pending_steps:
            raise ValueError("pending_steps must identify unfinished work")
        if not self.constraints:
            raise ValueError("constraints are required")
        if not self.external_refs:
            raise ValueError("external_refs are required")
        if not self.audit_refs:
            raise ValueError("audit_refs are required")
        for assumption in self.validated_assumptions:
            if not assumption.evidence_ref:
                raise ValueError("validated assumptions require evidence references")
