from models.reviewers import Reviewer
from models.movie import Movie
from models.review import Review

r1 = Reviewer("Alice")
r2 = Reviewer("Bob")
r1.save()
r2.save()

m1 = Movie("Inception", "Sci-Fi")
m2 = Movie("Titanic", "Romance")
m1.save()
m2.save()

rev1 = Review(r1.id, m1.id, 5, "Amazing movie!")
rev2 = Review(r2.id, m2.id, 4, "Very touching.")
rev1.save()
rev2.save()

print("Database seeded!")
