class Orchestrator:

    def __init__(self):
        self.status = "initialized"

    def start(self):
        self.status = "running"
