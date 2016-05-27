import pickle

directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"

splitChar = chr(182)
splitPost = chr(208)

class User:
	'''a user of the blog system'''
	def __init__(self, name, password):
		self.name = name
		self.password = password

class Post:
	'''A post in the system'''
	def __init__(self, id, user, title, text):
		#should be an int
		self.id = id
		self.user = user
		self.title = title
		self.text = text
		self.score = 0
		
		#Holds comment objects
		self.comments = []
	
	def addComment(self, user, text):
		self.comments.append( Comment(user, text))

class Comment:
	'''A comment in the system'''
	def __init__(self, user, text):
		self.user = user
		self.text = text
		self.score = 0

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

def objFileToList(targFile):
	readStream = open(directory + targFile, "r")
	resList = []
	try:
		while True:
			resList.append(pickle.load(readStream))
	except EOFError:
		print "End of File"
	finally:
		readStream.close()
	
	return resList











