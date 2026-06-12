import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class User:
    username: str
    email: str
    password: str

class FounderLink:
    def __init__(self):
        self.users = {}
        self.mvp_templates = {
            "basic": {
                "name": "Basic MVP",
                "description": "A basic MVP template"
            }
        }

    def create_account(self, username, email, password):
        if username in self.users:
            return False
        self.users[username] = User(username, email, password)
        return True

    def get_mvp_template(self, template_name):
        return self.mvp_templates.get(template_name)

    def redirect_to_mvp_builder(self, username):
        user = self.users.get(username)
        if user:
            return self.get_mvp_template("basic")
        return None

    def validate_idea(self, username, idea):
        user = self.users.get(username)
        if user:
            # Simulate idea validation
            return True
        return False
