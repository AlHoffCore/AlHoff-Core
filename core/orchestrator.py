from .agent_registry import AgentRegistry
from .task import Task
from .task_result import TaskResult


class Orchestrator:

    def __init__(self):
        self.status = "initialized"
        self.agent_registry = AgentRegistry()
        self._task_results = []

    def start(self):
        self.status = "running"

    def run_agent(self, name, task):
        agent = self.agent_registry.get(name)
        if agent is None:
            raise KeyError(f"Unknown agent: {name}")

        if not callable(getattr(agent, "run", None)):
            raise TypeError("Agent run method is not callable")

        return agent.run(task)

    def run_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("task must be a Task instance")

        output = self.run_agent(task.agent_name, task.payload)
        result = TaskResult(
            task.agent_name,
            task.payload,
            output,
            task.task_id,
        )
        self._task_results.append(result)
        return result

    def list_task_results(self):
        return tuple(self._task_results)

    def get_task_result(self, task_id):
        for result in self._task_results:
            if result.task_id == task_id:
                return result

        return None
