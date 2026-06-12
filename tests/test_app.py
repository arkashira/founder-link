import pytest
import sys
from io import StringIO
from src.app import main

def test_main():
    sys.argv = ['app.py', '--name', 'John Doe', '--email', 'john@example.com']
    out = StringIO()
    sys.stdout = out
    main()
    sys.stdout = sys.__stdout__
    assert 'Account created for John Doe' in out.getvalue()
    assert 'MVP: MVP for John Doe' in out.getvalue()
