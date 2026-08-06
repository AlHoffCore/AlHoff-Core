import unittest
from contextlib import redirect_stdout
from io import StringIO

from agents.echo_agent import EchoAgent
from core.main import AlHoffCore
from core.task import Task


class TestAlHoffCore(unittest.TestCase):

    def test_start_output(self):
        core = AlHoffCore()
        output = StringIO()

        with redirect_stdout(output):
            core.start()

        result = output.getvalue()
        self.assertIn("AlHoff Core", result)
        self.assertIn("Version: 0.1.0", result)
        self.assertIn("Core erfolgreich gestartet.", result)

    def test_echo_agent_is_registered(self):
        core = AlHoffCore()

        agent = core.orchestrator.agent_registry.get("echo")

        self.assertIsInstance(agent, EchoAgent)

    def test_echo_agent_returns_exact_same_task(self):
        core = AlHoffCore()
        task = {"message": "diagnostic"}

        result = core.run_agent("echo", task)

        self.assertIs(result, task)

    def test_unknown_agent_raises_key_error(self):
        core = AlHoffCore()

        with self.assertRaises(KeyError):
            core.run_agent("unknown", "test-task")

    def test_new_core_has_empty_task_result_history(self):
        core = AlHoffCore()

        history = core.list_task_results()

        self.assertIsInstance(history, tuple)
        self.assertEqual(history, ())

    def test_successful_task_is_stored_as_same_result_instance(self):
        core = AlHoffCore()

        result = core.run_task(Task("echo", "test-task"))
        history = core.list_task_results()

        self.assertEqual(len(history), 1)
        self.assertIs(history[0], result)

    def test_task_result_history_preserves_execution_order(self):
        core = AlHoffCore()

        first_result = core.run_task(Task("echo", "first"))
        second_result = core.run_task(Task("echo", "second"))
        history = core.list_task_results()

        self.assertIs(history[0], first_result)
        self.assertIs(history[1], second_result)

    def test_get_task_result_returns_stored_instance(self):
        core = AlHoffCore()
        result = core.run_task(Task("echo", "test-task"))

        stored_result = core.get_task_result(result.task_id)

        self.assertIs(stored_result, result)


if __name__ == "__main__":
    unittest.main()
