import unittest
from dataclasses import FrozenInstanceError
from datetime import datetime, timezone

from core.task_result import TaskResult


class TestTaskResult(unittest.TestCase):

    def test_values_are_stored_with_object_identity(self):
        payload = {"message": "diagnostic"}
        output = ["completed"]
        completed_at = datetime.now(timezone.utc)

        result = TaskResult(
            "echo",
            payload,
            output,
            "task-123",
            completed_at,
        )

        self.assertEqual(result.agent_name, "echo")
        self.assertEqual(result.task_id, "task-123")
        self.assertIs(result.payload, payload)
        self.assertIs(result.output, output)
        self.assertIs(result.completed_at, completed_at)
        self.assertIsInstance(result.completed_at, datetime)
        self.assertEqual(result.completed_at.tzinfo, timezone.utc)

    def test_task_result_is_immutable(self):
        result = TaskResult(
            "echo",
            "diagnostic",
            "completed",
            "task-123",
            datetime.now(timezone.utc),
        )

        with self.assertRaises(FrozenInstanceError):
            result.output = "changed"


if __name__ == "__main__":
    unittest.main()
