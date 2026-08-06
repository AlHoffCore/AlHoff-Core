import unittest

from core.orchestrator import Orchestrator


class TestOrchestrator(unittest.TestCase):

    def test_status_lifecycle(self):
        orchestrator = Orchestrator()
        self.assertEqual(orchestrator.status, "initialized")

        orchestrator.start()

        self.assertEqual(orchestrator.status, "running")


if __name__ == "__main__":
    unittest.main()
