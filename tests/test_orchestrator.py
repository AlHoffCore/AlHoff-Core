import unittest

from core.orchestrator import Orchestrator
from core.task import Task


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

    def test_new_orchestrator_has_empty_task_result_history(self):
        orchestrator = Orchestrator()

        self.assertEqual(orchestrator.list_task_results(), ())

    def test_successful_task_stores_same_result_instance(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("test-agent", TestAgent())

        result = orchestrator.run_task(Task("test-agent", "test-task"))
        history = orchestrator.list_task_results()

        self.assertIsInstance(history, tuple)
        self.assertEqual(len(history), 1)
        self.assertIs(history[0], result)

    def test_task_results_remain_in_execution_order(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("test-agent", TestAgent())

        first_result = orchestrator.run_task(Task("test-agent", "first"))
        second_result = orchestrator.run_task(Task("test-agent", "second"))
        history = orchestrator.list_task_results()

        self.assertIs(history[0], first_result)
        self.assertIs(history[1], second_result)

    def test_unknown_agent_is_not_stored_in_history(self):
        orchestrator = Orchestrator()

        with self.assertRaises(KeyError):
            orchestrator.run_task(Task("unknown", "test-task"))

        self.assertEqual(orchestrator.list_task_results(), ())

    def test_invalid_task_is_not_stored_in_history(self):
        orchestrator = Orchestrator()

        with self.assertRaises(TypeError):
            orchestrator.run_task(object())

        self.assertEqual(orchestrator.list_task_results(), ())

    def test_get_task_result_returns_none_for_empty_history(self):
        orchestrator = Orchestrator()

        self.assertIsNone(orchestrator.get_task_result("unknown"))

    def test_get_task_result_returns_stored_instance(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("test-agent", TestAgent())
        result = orchestrator.run_task(Task("test-agent", "test-task"))

        stored_result = orchestrator.get_task_result(result.task_id)

        self.assertIs(stored_result, result)

    def test_get_task_result_finds_correct_result(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("test-agent", TestAgent())
        first_result = orchestrator.run_task(Task("test-agent", "first"))
        second_result = orchestrator.run_task(Task("test-agent", "second"))

        self.assertIs(
            orchestrator.get_task_result(first_result.task_id),
            first_result,
        )
        self.assertIs(
            orchestrator.get_task_result(second_result.task_id),
            second_result,
        )

    def test_get_task_result_does_not_change_history(self):
        orchestrator = Orchestrator()
        orchestrator.agent_registry.register("test-agent", TestAgent())
        first_result = orchestrator.run_task(Task("test-agent", "first"))
        second_result = orchestrator.run_task(Task("test-agent", "second"))
        history_before = orchestrator.list_task_results()

        self.assertIsNone(orchestrator.get_task_result("unknown"))
        orchestrator.get_task_result(first_result.task_id)

        history_after = orchestrator.list_task_results()
        self.assertEqual(history_after, history_before)
        self.assertIs(history_after[0], first_result)
        self.assertIs(history_after[1], second_result)


if __name__ == "__main__":
    unittest.main()
