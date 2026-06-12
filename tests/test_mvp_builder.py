import pytest
from src.mvp_builder import mvp_builder
from src.user import User

def test_build_mvp():
    user = User(id=1, name='John Doe', email='john@example.com')
    mvp = mvp_builder.build(user)
    assert mvp == 'MVP for John Doe'
