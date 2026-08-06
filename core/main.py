"""
AlHoff Core
Entry Point
"""

from datetime import datetime


class AlHoffCore:

    def __init__(self):
        self.name = "AlHoff Core"
        self.version = "0.1.0"

    def start(self):
        print("=" * 50)
        print(self.name)
        print("=" * 50)
        print(f"Version: {self.version}")
        print(f"Startzeit: {datetime.now()}")
        print()
        print("Core erfolgreich gestartet.")
        print()


if __name__ == "__main__":
    core = AlHoffCore()
    core.start()