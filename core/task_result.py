from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TaskResult:
    agent_name: str
    payload: object
    output: object
    task_id: str
    completed_at: datetime
