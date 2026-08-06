from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    agent_name: str
    payload: object

    def __post_init__(self):
        if not isinstance(self.agent_name, str) or not self.agent_name:
            raise ValueError("Agent name must be a non-empty string")
