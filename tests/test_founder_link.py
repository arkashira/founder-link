from founder_link import FounderLink
import pytest
from datetime import datetime, timedelta

def test_create_account():
    founder_link = FounderLink()
    username = "test_user"
    email = "test@example.com"
    password = "test_password"
    assert founder_link.create_account(username, email, password)
    assert not founder_link.create_account(username, email, password)

def test_redirect_to_mvp_builder():
    founder_link = FounderLink()
    username = "test_user"
    email = "test@example.com"
    password = "test_password"
    founder_link.create_account(username, email, password)
    mvp_template = founder_link.redirect_to_mvp_builder(username)
    assert mvp_template
    assert mvp_template["name"] == "Basic MVP"

def test_validate_idea():
    founder_link = FounderLink()
    username = "test_user"
    email = "test@example.com"
    password = "test_password"
    founder_link.create_account(username, email, password)
    idea = "Test idea"
    assert founder_link.validate_idea(username, idea)

def test_account_creation_time():
    founder_link = FounderLink()
    username = "test_user"
    email = "test@example.com"
    password = "test_password"
    start_time = datetime.now()
    founder_link.create_account(username, email, password)
    end_time = datetime.now()
    account_creation_time = end_time - start_time
    assert account_creation_time < timedelta(minutes=2)
