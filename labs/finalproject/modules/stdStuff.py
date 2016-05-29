import pickle

directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"
postIdFile = "postId.txt"

#possibly deprecated
splitChar = chr(182)
splitPost = chr(208)

class User(object):
	'''a user of the blog system'''
	def __init__(self, name, password):
		self.name = name
		self.password = password
		
		#holds a list of friend NAMES
		self.friends = []
		
		self.inbox = Inbox(name)
		
		#holds post objects
		self.posts = []

class TextContainer(object):
	'''A standard class title, text etc. Inherit from this class'''
	
	def __init__(self, id, user, title, text):
		#should be an int
		self.id = id
		
		self.user = user
		self.title = title
		self.text = text

class Post(TextContainer):
	'''A post in the system'''
	def __init__(self, id, user, title, text):
		super(Post, self).__init__(id, user, title, text)
		
		self.score = 0
		
		#Holds comment objects
		self.comments = []
	
	def addComment(self, user, text):
		self.comments.append( Comment(user, text))
	
	def increaseScore(self):
		self.score += 1
	
	def decreaseScore(self):
		self.score -= 1

class Comment(TextContainer):
	'''A comment in the system'''
	def __init__(self, id, user, text):
		super(Comment, self).__init__(id, user, "", text)
		
		self.score = 0

class Inbox(object):
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

class Message(TextContainer):
	'''A message'''
	def __init__(self, id, user, title, text):
		super(Message, self).__init__(id, user, title, text)
	
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







