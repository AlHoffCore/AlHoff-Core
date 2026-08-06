from .agent_registry import AgentRegistry


class Orchestrator:

    def __init__(self):
        self.status = "initialized"
        self.agent_registry = AgentRegistry()

    def start(self):
        self.status = "running"
