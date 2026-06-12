import json
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

class UserRepository:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def create(self, user):
        self.data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
        self.save()

    def get(self, id):
        for user in self.data:
            if user['id'] == id:
                return User(**user)
        return None

user_repository = UserRepository()
