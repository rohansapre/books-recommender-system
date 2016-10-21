class User(object):
	"""docstring for User"""
	def __init__(self, id, location, age):
		super(User, self).__init__()
		self.id = id
		self.location = location
		self.age = age

class Book(object):
	"""docstring for Book"""
	def __init__(self, isbn, title):
		super(Book, self).__init__()
		self.isbn = isbn
		self.title = title
		