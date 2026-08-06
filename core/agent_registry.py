class AgentRegistry:

    def __init__(self):
        self._agents = {}

    def register(self, name, agent):
        if name in self._agents:
            raise ValueError(f"Agent already registered: {name}")

        self._agents[name] = agent

    def get(self, name):
        return self._agents.get(name)

    def list_names(self):
        return list(self._agents)
