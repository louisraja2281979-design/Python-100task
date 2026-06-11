class MovieRecommendationApp:
    def __init__(self):
        self.movies = {
            "Action": [
                "John Wick",
                "Mad Max: Fury Road",
                "The Dark Knight",
                "Mission Impossible"
            ],
            "Comedy": [
                "The Mask",
                "Mr. Bean",
                "Home Alone",
                "Jumanji"
            ],
            "Drama": [
                "Forrest Gump",
                "The Pursuit of Happyness",
                "The Shawshank Redemption",
                "Titanic"
            ],
            "Sci-Fi": [
                "Interstellar",
                "Inception",
                "The Matrix",
                "Avatar"
            ],
            "Horror": [
                "The Conjuring",
                "Insidious",
                "It",
                "A Quiet Place"
            ]
        }

    def show_genres(self):
        print("\nAvailable Genres:")
        for i, genre in enumerate(self.movies.keys(), start=1):
            print(f"{i}. {genre}")

    def recommend_movies(self, genre):
        if genre in self.movies:
            print(f"\nRecommended {genre} Movies:")
            for movie in self.movies[genre]:
                print(f"• {movie}")
        else:
            print("Genre not found!")

    def run(self):
        while True:
            print("\n===== MOVIE RECOMMENDATION APP =====")
            print("1. Show Genres")
            print("2. Get Recommendations")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_genres()

            elif choice == "2":
                self.show_genres()
                genre = input("\nEnter genre name: ").title()
                self.recommend_movies(genre)

            elif choice == "3":
                print("Thank you for using the app!")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = MovieRecommendationApp()
    app.run()