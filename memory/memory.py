class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry):
        self.history.append(entry)

    def get_context(self):
        return "\n".join(self.history)