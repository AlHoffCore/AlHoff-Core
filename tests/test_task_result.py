import unittest
from dataclasses import FrozenInstanceError

from core.task_result import TaskResult


class TestTaskResult(unittest.TestCase):

    def test_values_are_stored_with_object_identity(self):
        payload = {"message": "diagnostic"}
        output = ["completed"]

        result = TaskResult("echo", payload, output, "task-123")

        self.assertEqual(result.agent_name, "echo")
        self.assertEqual(result.task_id, "task-123")
        self.assertIs(result.payload, payload)
        self.assertIs(result.output, output)

    def test_task_result_is_immutable(self):
        result = TaskResult(
            "echo",
            "diagnostic",
            "completed",
            "task-123",
        )

        with self.assertRaises(FrozenInstanceError):
            result.output = "changed"


if __name__ == "__main__":
    unittest.main()
