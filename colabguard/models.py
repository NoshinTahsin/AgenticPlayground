"""Small, dependency-free data models used by the early learning modules."""

from dataclasses import asdict, dataclass
from typing import Literal


@dataclass(frozen=True)
class Message:
    role: Literal["user", "assistant"]
    content: str


@dataclass(frozen=True)
class Scenario:
    id: str
    title: str
    user_request: str
    trusted_policy: str
    expected_outcome: str


@dataclass(frozen=True)
class AgentResponse:
    answer: str
    decision: str
    evidence_used: list[str]

    def to_dict(self) -> dict:
        return asdict(self)
