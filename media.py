import webbrowser

class Movie():
    """Encapsulates movie objects."""

    def __init__(self, title, image, trailer):
        """Variables used in fresh_tomatoes.py

        Constructor gives arguments to instances variables.
        """

        self.title = title
        self.trailer_youtube_url = trailer
        self.poster_image_url = image
        # instances variables and 


