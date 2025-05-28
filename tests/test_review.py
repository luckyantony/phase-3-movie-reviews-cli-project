import pytest
import sqlite3

@pytest.fixture(scope="session", autouse=True)
def setup_database_once():
    conn = sqlite3.connect("movie_reviews.db")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

from models.review import Review
from models.reviewers import Reviewer
from models.movie import Movie

def test_review_creation():
    reviewer = Reviewer("Reviewer A")
    reviewer.save()
    movie = Movie("Movie A", "Horror")
    movie.save()
    review = Review(reviewer.id, movie.id, 4, "Scary!")
    assert review.rating == 4
    assert review.comment == "Scary!"

def test_review_save():
    reviewer = Reviewer("Reviewer B")
    reviewer.save()
    movie = Movie("Movie B", "Comedy")
    movie.save()
    review = Review(reviewer.id, movie.id, 3, "Funny")
    review.save()
    assert review.id is not None