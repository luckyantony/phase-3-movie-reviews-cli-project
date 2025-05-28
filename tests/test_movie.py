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