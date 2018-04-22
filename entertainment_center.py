import fresh_tomatoes
import media

m1 = media.Movie(
    "Dr. Strangelove",
    "https://upload.wikimedia.org/wikipedia/en/e/e6/Dr._Strangelove_poster"
    ".jpg",
    "https://www.youtube.com/watch?v=IE9CmX15PYA")

m2 = media.Movie(
    "Gattaca",
    "https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster"
    "_B.jpg",
    "https://www.youtube.com/watch?v=BpzVFdDeWyo")

m3 = media.Movie(
    "Wall Street (1987)",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Wall_Street_film.jpg",
    "https://www.youtube.com/watch?v=FCctqbRrsBQ")


m4 = media.Movie(
    "Fight Club",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

m5 = media.Movie(
    "Inception",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_t"
    "heatrical_poster.jpg",
    "https://www.youtube.com/watch?v=JEv8W3pWqH0")

m6 = media.Movie(
    "The Matrix",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# instances of movies

movies = [m1, m2, m3, m4, m5, m6]
# List of instances of movies.

fresh_tomatoes.open_movies_page(movies)
# Builds HTML file with movies list.
