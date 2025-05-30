from models.reviewers import Reviewer
from models.movie import Movie
from models.review import Review

def list_movies():
    print("\nMovies:")
    for movie in Movie.all():
        print(movie)

def list_reviewers():
    print("\nReviewers:")
    for reviewer in Reviewer.all():
        print(reviewer)

def list_reviews():
    print("\nReviews:")
    for review in Review.all():
        print(review)

def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    movie = Movie(title, genre)
    movie.save()
    print(f"Movie '{title}' added.")

def add_reviewer():
    name = input("Enter reviewer name: ")
    reviewer = Reviewer(name)
    reviewer.save()
    print(f"Reviewer '{name}' added.")

def add_review():
    try:
        reviewer_id = int(input("Enter reviewer ID: "))
        movie_id = int(input("Enter movie ID: "))
        rating = int(input("Enter rating (1–5): "))
        comment = input("Enter review comment: ")
        review = Review(reviewer_id, movie_id, rating, comment)
        review.save()
        print("Review added.")
    except ValueError:
        print("Invalid input. Try again.")

def delete_movie():
    try:
        movie_id = int(input("Enter movie ID to delete: "))
        Movie.delete_by_id(movie_id)
        print(f"Movie with ID {movie_id} deleted.")
    except ValueError:
        print("Invalid input.")

def delete_reviewer():
    try:
        reviewer_id = int(input("Enter reviewer ID to delete: "))
        Reviewer.delete_by_id(reviewer_id)
        print(f"Reviewer with ID {reviewer_id} deleted.")
    except ValueError:
        print("Invalid input.")

def delete_review():
    try:
        review_id = int(input("Enter review ID to delete: "))
        Review.delete_by_id(review_id)
        print(f"Review with ID {review_id} deleted.")
    except ValueError:
        print("Invalid input.")

def menu():
    print("\nMovie Review CLI")
    print("1. List movies")
    print("2. List reviewers")
    print("3. List reviews")
    print("4. Add movie")
    print("5. Add reviewer")
    print("6. Add review")
    print("7. Delete movie")
    print("8. Delete reviewer")
    print("9. Delete review")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            list_movies()
        elif choice == '2':
            list_reviewers()
        elif choice == '3':
            list_reviews()
        elif choice == '4':
            add_movie()
        elif choice == '5':
            add_reviewer()
        elif choice == '6':
            add_review()
        elif choice == '7':
            delete_movie()
        elif choice == '8':
            delete_reviewer()
        elif choice == '9':
            delete_review()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
