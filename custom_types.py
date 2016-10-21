class User(object):
	"""docstring for User"""
	def __init__(self, id, location, age):
		super(User, self).__init__()
		self.id = id
		self.location = location
		self.age = age

	def getID():
		self.id

class Book(object):
	"""docstring for Book"""
	def __init__(self, isbn, title):
		super(Book, self).__init__()
		self.isbn = isbn
		self.title = title

class Rating(object):
	"""docstring for Rating"""
	def __init__(self, user_id, isbn, value):
		super(Rating, self).__init__()
		self.user_id = user_id
		self.isbn = isbn
		self.value = value