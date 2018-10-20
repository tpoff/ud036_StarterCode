import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        title (str): Title of the movie.
        storyline (str): Summary of movie.
        poster_image_url (str): url for movie poster.
        trailer_youtube_url (str): url for youtube trailer for movie.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Constructor for a Movie instance.

        Args:
            movie_title (str): The name of the movie.
            movie_storyline (str): Summary of the movie.
            poster_image (str): Link to the movie poster.
            trailer_youtube (str): Link to the youtube movie trailer.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Uses the webbrowser.open function to open the youtube trailer using
        the stored url in the class instance.

        Args:

        Returns:
        """

        # use the webbrowser package to open the youtube url in the default
        # browser.
        webbrowser.open(self.trailer_youtube_url)
