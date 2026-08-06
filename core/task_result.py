from dataclasses import dataclass


@dataclass(frozen=True)
class TaskResult:
    agent_name: str
    payload: object
    output: object
