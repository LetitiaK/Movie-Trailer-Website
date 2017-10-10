class Movie():
  """ This class is used to define movies."""

  def __init__(self, title, poster_image_url, trailer_youtube_url):
      """Inits the class Movie with the variables title, poster_image_url,
      and trailer_youtube_url
      """
      self.title = title
      self.poster_image_url = poster_image_url
      self.trailer_youtube_url = trailer_youtube_url
