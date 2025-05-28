from models.reviewers import Reviewer
from models.movie import Movie
from models.review import Review

# Try creating a reviewer
r = Reviewer("Test Reviewer")
r.save()
print("Created reviewer:", r)

# Try creating a movie
m = Movie("The Matrix", "Sci-Fi")
m.save()
print("Created movie:", m)

# Try creating a review
rev = Review(r.id, m.id, 5, "Mind-blowing effects!")
rev.save()
print("Created review:", rev)

# Print all movies
print("All movies:")
for movie in Movie.all():
    print(movie)

# Print all reviews
print("All reviews:")
for review in Review.all():
    print(review)
