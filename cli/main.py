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

def main():
    while True:
        print("\nMovie Review CLI")
        print("1. List movies")
        print("2. List reviewers")
        print("3. List reviews")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            list_movies()
        elif choice == '2':
            list_reviewers()
        elif choice == '3':
            list_reviews()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

