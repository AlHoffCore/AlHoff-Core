import unittest

from core.orchestrator import Orchestrator


class TestAgent:

    def __init__(self):
        self.received_task = None

    def run(self, task):
        self.received_task = task
        return "completed"


class TestOrchestrator(unittest.TestCase):

    def test_status_lifecycle(self):
        orchestrator = Orchestrator()
        self.assertEqual(orchestrator.status, "initialized")

        orchestrator.start()

        self.assertEqual(orchestrator.status, "running")

    def test_run_agent_passes_task_and_returns_result(self):
        orchestrator = Orchestrator()
        agent = TestAgent()
        orchestrator.agent_registry.register("test-agent", agent)

        result = orchestrator.run_agent("test-agent", "test-task")

        self.assertEqual(agent.received_task, "test-task")
        self.assertEqual(result, "completed")

    def test_run_unknown_agent_raises_key_error(self):
        orchestrator = Orchestrator()

        with self.assertRaisesRegex(KeyError, "Unknown agent: unknown"):
            orchestrator.run_agent("unknown", "test-task")

    def test_run_agent_without_callable_run_raises_type_error(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("invalid-agent", object())

        with self.assertRaises(TypeError):
            orchestrator.run_agent("invalid-agent", "test-task")


if __name__ == "__main__":
    unittest.main()
