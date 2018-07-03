import webbrowser

class Movie(object):	
	"""docstring for Movie == This Class Provide a Way To Store Movie Related Information"""
	#VALID_RADING = ['Mohammed','AZ','SAAD','Azghour']
	def __init__(self, movie_title,movie_story_line,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_story_line					# self is not a Python keyword
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		# super(Movie, self).__init__()
		# self.arg = arg  

		# def __init__(self,Best_Trailer):
		# 	self.Best_Trailer = Best_Trailer

		# def Showing_My_Best_Trailer(self):
		# 	webbrowser.open(self.Best_Trailer)

		# def show_Trailer(self):					#Instance Methode
		# 	webbrowser.open(self.trailer_youtube_url)

		
# class TvShow(Veideo):
# 	"""docstring for TvShow"""
# 	def __init__(self, Title,season,Episod):
# 		self.Title = Title
# 		self.season = season
# 		self.Episod = Episod
# 		#super(TvShow, self).__init__()
# 		#self.arg = arg

	#def GetLocal_Listing(self):        #And Create Instances Season1,Breakin_Bad


# class Veideo(object):
# 	"""docstring for Veideo"""
# 	def __init__(self, title,duraion):
# 		self.title =	title
# 		self.duraion = duraion
# 		# super(Veideo, self).__init__()
# 		# self.arg = arg
