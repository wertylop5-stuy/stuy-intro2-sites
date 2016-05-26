directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"

splitChar = chr(182)
splitPost = chr(208)

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

