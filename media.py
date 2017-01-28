class Movie():
    """
    Stores information of a movie.

    Attributes:
        title (str): title of a movie
        poster_image_url (str): url of a poster
        trailer_youtube_url (str): url of a trailer on youtube
    """
    
    def __init__(self, movie_title,
                 poster_image,trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
