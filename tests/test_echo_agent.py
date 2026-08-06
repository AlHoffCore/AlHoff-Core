import unittest

from agents.echo_agent import EchoAgent
from core.agent_registry import AgentRegistry
from core.orchestrator import Orchestrator


class TestEchoAgent(unittest.TestCase):

    def test_run_returns_string_unchanged(self):
        agent = EchoAgent()

        self.assertEqual(agent.run("diagnostic task"), "diagnostic task")

    def test_run_returns_dictionary_unchanged(self):
        agent = EchoAgent()
        task = {"type": "diagnostic"}

        self.assertIs(agent.run(task), task)

    def test_agent_can_be_registered_as_echo(self):
        registry = AgentRegistry()
        agent = EchoAgent()

        registry.register("echo", agent)

        self.assertIs(registry.get("echo"), agent)

    def test_orchestrator_returns_exact_same_object(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("echo", EchoAgent())
        task = {"message": "test"}

        result = orchestrator.run_agent("echo", task)

        self.assertIs(result, task)


if __name__ == "__main__":
    unittest.main()
