import unittest
from contextlib import redirect_stdout
from io import StringIO

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


if __name__ == "__main__":
    unittest.main()
