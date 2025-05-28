import pytest
import sqlite3

@pytest.fixture(scope="session", autouse=True)
def setup_database_once():
    conn = sqlite3.connect("movie_reviews.db")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

from models.movie import Movie

def test_movie_creation():
    movie = Movie("Test Movie", "Drama")
    assert movie.title == "Test Movie"
    assert movie.genre == "Drama"
    assert movie.id is None

def test_movie_save():
    movie = Movie("Test Save Movie", "Action")
    movie.save()
    assert movie.id is not None