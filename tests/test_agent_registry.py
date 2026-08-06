import unittest

from core.agent_registry import AgentRegistry
from core.orchestrator import Orchestrator


class TestAgentRegistry(unittest.TestCase):

    def test_register_and_get_agent(self):
        registry = AgentRegistry()
        agent = object()

        registry.register("test-agent", agent)

        self.assertIs(registry.get("test-agent"), agent)

    def test_get_unknown_agent_returns_none(self):
        registry = AgentRegistry()

        self.assertIsNone(registry.get("unknown"))

    def test_list_names_contains_registered_names(self):
        registry = AgentRegistry()
        registry.register("first-agent", object())
        registry.register("second-agent", object())

        self.assertEqual(
            registry.list_names(),
            ["first-agent", "second-agent"],
        )

    def test_duplicate_registration_raises_value_error(self):
        registry = AgentRegistry()
        registry.register("test-agent", object())

        with self.assertRaises(ValueError):
            registry.register("test-agent", object())

    def test_orchestrator_has_empty_agent_registry(self):
        orchestrator = Orchestrator()

        self.assertEqual(orchestrator.agent_registry.list_names(), [])


if __name__ == "__main__":
    unittest.main()
