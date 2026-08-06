"""
AlHoff Core
Entry Point
"""

from datetime import datetime

from agents.echo_agent import EchoAgent

from .orchestrator import Orchestrator


class AlHoffCore:

    def __init__(self):
        self.name = "AlHoff Core"
        self.version = "0.1.0"
        self.orchestrator = Orchestrator()
        self.orchestrator.agent_registry.register("echo", EchoAgent())

    def start(self):
        self.orchestrator.start()
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
