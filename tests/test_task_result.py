import unittest
from dataclasses import FrozenInstanceError

from core.task_result import TaskResult


class TestTaskResult(unittest.TestCase):

    def test_values_are_stored_with_object_identity(self):
        payload = {"message": "diagnostic"}
        output = ["completed"]

        result = TaskResult("echo", payload, output)

        self.assertEqual(result.agent_name, "echo")
        self.assertIs(result.payload, payload)
        self.assertIs(result.output, output)

    def test_task_result_is_immutable(self):
        result = TaskResult("echo", "diagnostic", "completed")

        with self.assertRaises(FrozenInstanceError):
            result.output = "changed"


if __name__ == "__main__":
    unittest.main()
