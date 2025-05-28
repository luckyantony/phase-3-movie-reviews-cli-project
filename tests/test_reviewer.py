import pytest
import sqlite3

@pytest.fixture(scope="session", autouse=True)
def setup_database_once():
    conn = sqlite3.connect("movie_reviews.db")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

from models.reviewers import Reviewer

def test_reviewer_creation():
    reviewer = Reviewer("Test User")
    assert reviewer.name == "Test User"
    assert reviewer.id is None

def test_reviewer_save():
    reviewer = Reviewer("Test Save")
    reviewer.save()
    assert reviewer.id is not None