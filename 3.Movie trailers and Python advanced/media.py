"""
This is the program that contains the parent constructor for movie object and the show trailer function to open youtube trailers.
"""

# import webbrowser for webbrowser functions
import webbrowser

class Movie(object):
	""" A class that stores movie related information along with ability to show a movie trailer. """

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # class variable

	# constructor to get info about a certain movie
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# instance variable
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# method to display trailers
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) # webbrowser functions
