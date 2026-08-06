import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Task:
    agent_name: str
    payload: object
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        if not isinstance(self.agent_name, str) or not self.agent_name:
            raise ValueError("Agent name must be a non-empty string")
