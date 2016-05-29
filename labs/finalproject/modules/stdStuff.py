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
		
		#holds a list of friend NAMES
		self.friends = []
		
		self.inbox = Inbox(name)

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

class Inbox:
	'''Each user's inbox'''
	def __init__(self, user):
		self.user = user
		self.size = 0
		self.messages = []
	
	def listMessages(self):
		for message in messages:
			message.display()
	
	def sendMessage(self, message):
		'''Send a message to a user'''
		pass

class Message:
	'''A message'''
	def __init__(self, user, title, text):
		self.user = user
		self.title = title
		self.text = text
	
	def display(self):
		'''Display message contents in html'''
		res = ""
		res += makeTag("h5", self.user)
		res += makeTag("h3", self.title)
		res += makeTag("p", self.text)
		return res

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
	readStream = open(directory + targFile, "rb")
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
	objWStream = open(directory + targFile, "wb")
	objWStream.write("")
	for x in objList:
		pickle.dump(x, objWStream)
	objWStream.close()







