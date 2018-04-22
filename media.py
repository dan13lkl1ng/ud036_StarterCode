class Movie():
    """Managing the attributes of a movie.

    This class gets the attributes of a movie in the constructor
    and sets the instace variables to them.

    Attributes:
        title (str): Title of movie.
        image (str): Link to the box image.
        trailer (str): Link to the trailer.
    """

    def __init__(self, title, image, trailer):
        """Variables used in fresh_tomatoes.py

        Constructor gives arguments to instance variables.
        """

        self.title = title
        self.trailer_youtube_url = trailer
        self.poster_image_url = image
# instance variables
