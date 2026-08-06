from .agent_registry import AgentRegistry


class Orchestrator:

    def __init__(self):
        self.status = "initialized"
        self.agent_registry = AgentRegistry()

    def start(self):
        self.status = "running"

    def run_agent(self, name, task):
        agent = self.agent_registry.get(name)
        if agent is None:
            raise KeyError(f"Unknown agent: {name}")

        if not callable(getattr(agent, "run", None)):
            raise TypeError("Agent run method is not callable")

        return agent.run(task)
