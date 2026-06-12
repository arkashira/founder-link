import pytest
from src.user import User, user_repository

def test_create_user():
    user = User(id=1, name='John Doe', email='john@example.com')
    user_repository.create(user)
    assert user_repository.get(1) == user

def test_get_user():
    user = User(id=1, name='John Doe', email='john@example.com')
    user_repository.create(user)
    assert user_repository.get(1) == user

def test_get_non_existent_user():
    user_repository.data = []  # Reset the data
    user_repository.save()
    assert user_repository.get(1) is None
