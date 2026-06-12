import json

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

config = Config()
