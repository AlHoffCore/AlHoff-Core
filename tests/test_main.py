import unittest
from contextlib import redirect_stdout
from io import StringIO

from agents.echo_agent import EchoAgent
from core.main import AlHoffCore


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


if __name__ == "__main__":
    unittest.main()
