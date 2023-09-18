class ConversationHistoryLog:
    def __init__(self, fn):
        self.fn = fn

    def write(self, line):
        with open(self.fn, 'a') as f:
            f.write(line + '\n')

    def get_all(self):
        with open(self.fn, 'r') as f:
            return f.read().splitlines()
