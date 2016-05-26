directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"

splitChar = chr(182)
splitPost = chr(208)

class User:
	def __init__(self, name, password):
		self.name = name
		self.password = password

class Post:
	def __init__(self, id, user, title, text):
		self.id = id
		self.user = user
		self.title = title
		self.text = text
		self.comments = []

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"


