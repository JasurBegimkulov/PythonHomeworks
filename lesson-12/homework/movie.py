import requests
import random


API_KEY = "123456789abcdef123456789abcdef12"
BASE_URL = "https://api.themoviedb.org/3"


def get_genres():
    genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(genre_url)
    genres = response.json()["genres"]
    
    print("\nAvailable Genres:")
    for genre in genres:
        print(f"{genre['id']}: {genre['name']}")
    
    return genres


def get_movie_by_genre(genre_id):
    movies_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(movies_url)
    movies = response.json()["results"]

    if movies:
        movie = random.choice(movies)
        print("\n🎬 Movie Recommendation 🎬")
        print(f"📽 Title: {movie['title']}")
        print(f"📜 Overview: {movie['overview']}")
        print(f"⭐ Rating: {movie['vote_average']}/10")
    else:
        print("\n❌ No movies found for this genre. Try another!")


genres = get_genres()
genre_id = input("\nEnter a genre ID to get a movie recommendation: ")
get_movie_by_genre(genre_id)