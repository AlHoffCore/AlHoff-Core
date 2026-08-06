import unittest
from dataclasses import FrozenInstanceError

from core.main import AlHoffCore
from core.task import Task
from core.task_result import TaskResult


class TestTask(unittest.TestCase):

    def test_agent_name_and_payload_are_stored(self):
        payload = {"message": "diagnostic"}

        task = Task("echo", payload)

        self.assertEqual(task.agent_name, "echo")
        self.assertIs(task.payload, payload)
        self.assertIsInstance(task.task_id, str)
        self.assertTrue(task.task_id)

    def test_different_tasks_have_different_ids(self):
        first_task = Task("echo", "first")
        second_task = Task("echo", "second")

        self.assertNotEqual(first_task.task_id, second_task.task_id)

    def test_task_is_immutable(self):
        task = Task("echo", "diagnostic")

        with self.assertRaises(FrozenInstanceError):
            task.agent_name = "other"

    def test_empty_agent_name_raises_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "Agent name must be a non-empty string",
        ):
            Task("", "diagnostic")

    def test_non_string_agent_name_raises_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "Agent name must be a non-empty string",
        ):
            Task(123, "diagnostic")

    def test_echo_task_returns_task_result(self):
        core = AlHoffCore()
        payload = {"message": "diagnostic"}
        task = Task("echo", payload)

        result = core.run_task(task)

        self.assertIsInstance(result, TaskResult)
        self.assertEqual(result.agent_name, "echo")
        self.assertEqual(result.task_id, task.task_id)
        self.assertIs(result.payload, payload)
        self.assertIs(result.output, payload)

    def test_unknown_agent_raises_key_error(self):
        core = AlHoffCore()
        task = Task("unknown", "diagnostic")

        with self.assertRaises(KeyError):
            core.run_task(task)

    def test_non_task_raises_type_error(self):
        core = AlHoffCore()

        with self.assertRaisesRegex(TypeError, "task must be a Task instance"):
            core.run_task(object())


if __name__ == "__main__":
    unittest.main()
