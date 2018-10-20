import media
import fresh_tomatoes

# The first step for this project is to build several Movie instances detailing
# several movies we want to display. We then use the
# fresh_tomatoes.open_movies_page function to create the html page by passing
# in a list of the movie instances we created.

# The basic format for creating a movie object is
# movie = media.Movie(
#    "Movie Title",
#    "Movie Summary",
#    "url to image of movie poster",  # NOQA
#    "hurl to the movie's trailer on youtube")
# Use the above format to create new movie objects. Once a new movie is
# created add it to the movies list at the bottom of the script.

# Construct a Movie instance for Toy Story.
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY606_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Construct a Movie instance for Avatar.
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://img.goldposter.com/2015/05/Avatar_poster_goldposter_com_10.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# Construct a Movie instance for Avengers.
avengers = media.Movie(
    "Avengers",
    "Earth's mightiest heroes must come together and learn to fight as a team "
    "if they are going to stop the mischievous Loki and his alien army from "
    "enslaving humanity.",
    "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Construct a Movie instance for The Martian.
the_martian = media.Movie(
    "The Martian",
    "An astronaut becomes stranded on Mars after his team assume him dead.",
    "https://images-na.ssl-images-amazon.com/images/I/A1%2BFw58qbDL._SY606_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

# Construct a Movie instance for Spider-Man: Into the Spider-Verse.
spiderverse = media.Movie(
    "Spider-Man: Into the Spider-Verse",
    "Spider-Man mentors a teenager from Brooklyn, N.Y., to"
    " become the next web-slinging superhero.",
    "https://www.sonypictures.com/movies/spidermanintothespiderverse/assets/images/onesheet.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tg52up16eq0")

# Construct a Movie instance for The Intern.
the_intern = media.Movie(
    "The Intern",
    "Seventy-year-old widower Ben Whittaker has discovered that retirement "
    "isn't all it's cracked up to be. Seizing an opportunity to get back in "
    "the game, he becomes a senior intern at an online fashion site, founded "
    "and run by Jules Ostin.",
    "http://www.gstatic.com/tv/thumb/v22vodart/11550244/p11550244_v_v8_ac.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

# Now that we've created several Movie instances, put them into a list
movies = [
    toy_story,
    avatar,
    avengers,
    the_martian,
    spiderverse,
    the_intern
]

# Now we pass this list to the fresh_tomatoes.open_movies_page
# This will construct the html page using our Movie objects and open it
# in the browser.
fresh_tomatoes.open_movies_page(movies)
