class EventMemory:
    def __init__(self):
        self.history = []

    def add(self, step, result):
        self.history.append({
            "step": step,
            "result": result
        })

    def get_context(self):
        return str(self.history)