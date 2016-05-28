import pickle

directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"
postIdFile = "postId.txt"

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
	
	def increaseScore(self):
		self.score += 1
	
	def decreaseScore(self):
		self.score -= 1
	

class Comment:
	'''A comment in the system'''
	def __init__(self, user, text):
		self.user = user
		self.text = text
		self.score = 0

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

def isFileEmpty(directory, fileN):
	readStream = open(directory + fileN, "r")
	thing = readStream.read()
	readStream.close()
	if thing == "":
		return True
	return False

def objFileToList(directory, targFile):
	resList = []
	if isFileEmpty(directory, targFile):
		return resList
	readStream = open(directory + targFile, "r")
	try:
		while True:
			resList.append(pickle.load(readStream))
	except EOFError:
		pass
	except IndexError:
		pass
	finally:
		readStream.close()
	
	return resList

def objListToFile(objList, directory, targFile):
	"""Writes a list of objects to a file"""
	'''
	with open(directory + targFile, "w") as objWStream:
		for x in objList:
			pickle.dump(x, objWStream)
	'''
	objWStream = open(directory + targFile, "w")
	objWStream.write("")
	for x in objList:
		pickle.dump(x, objWStream)
	objWStream.close()







