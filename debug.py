from models.reviewers import Reviewer
from models.movie import Movie
from models.review import Review

r = Reviewer("Test Reviewer")
r.save()
print("Created reviewer:", r)

m = Movie("The Matrix", "Sci-Fi")
m.save()
print("Created movie:", m)

rev = Review(r.id, m.id, 5, "Mind-blowing effects!")
rev.save()
print("Created review:", rev)

print("All movies:")
for movie in Movie.all():
    print(movie)

print("All reviews:")
for review in Review.all():
    print(review)

