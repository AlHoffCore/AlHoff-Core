import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Task:
    agent_name: str
    payload: object
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self):
        if not isinstance(self.agent_name, str) or not self.agent_name:
            raise ValueError("Agent name must be a non-empty string")
