import pickle, copy
#TODO line 219 fix user display tag
directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"
postIdFile = "postId.txt"
groupFile = "groups.txt"
groupsNameFile = "groupsName.txt"
currentGroupFile = "currentGroup.txt"

#possibly deprecated
splitChar = chr(182)
splitPost = chr(208)

class User(object):
	'''a user of the blog system'''
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.inbox = Inbox(name)
		
		#holds a list of friend NAMES
		self.friends = []
		
		#holds post objects
		self.posts = []
		
		self.searchUser = ''
	
	def addPost(self, post):
		self.posts.append(post)
	
	def addFriend(self, friendName):
		self.friends.append(friendName)
	
	def displayPosts(self, idTag="h6", userTag="h2", titleTag="h1", textTag="p"):
		res = ""
		for x in self.posts:
			res += x.display(idTag, userTag, titleTag, textTag)
		return res
	
	def displaySearchPostsWithVoter(self, searchUser, idTag="h6", userTag="h2", titleTag="h1", textTag="p"):
		res = ""
		for x in self.posts:
			res += """<table>
				<tr>
				<td>""" + str(x.score) + """</td>
				<td>
				"""
			res += x.display(idTag, userTag, titleTag, textTag)
			
			res += "<a href='search.py?downVote=lol&postId="+ str(x.id) + '&user=' + searchUser + "'>Down Vote</a><br>" + \
"<a href='search.py?upVote=lol&postId="+ str(x.id) + '&user=' + searchUser + "'>Up Vote</a><br>" + \
"<a href='search.py?removeVote=lol&postId="+ str(x.id) + '&user=' + searchUser + "'>Remove Vote</a><br>" + \
"""<a href='postExpandedSearch.py?expandButton=""" + str(x.id) + '&searchUserPost=' + searchUser +"'>Comment </a>"
			res += """</td>
	</tr>
	</table>
"""
		return res

class TextContainer(object):
	'''A standard class title, text etc. Inherit from this class'''
	
	def __init__(self, id, user, title, text):
		#should be an int
		self.id = id
		
		self.user = user
		self.title = title
		self.text = text
	
	def display(self):
		res = ""
		res += makeTag("h6", self.id)
		res += makeTag("h2", self.user)
		res += makeTag("h1", self.title)
		res += makeTag("p", self.text)
		return res

class Post(TextContainer):
	'''A post in the system'''
	def __init__(self, id, user, title, text):
		super(Post, self).__init__(id, user, title, text)
		
		self.score = 0
		
		#Holds comment objects
		self.comments = []
		
		self.votedUsers = {}
	
	def display(self, idTag="h6", userTag="h2", titleTag="h1", textTag="p"):
		'''Prints html of the post'''
		res = ""
		res += makeTag(idTag, "Id: " + str(self.id))
		res += makeTag(userTag, "User: " + str(self.user))
		res += makeTag(titleTag, self.title)
		res += makeTag(textTag, self.text)
		return res
	
	def displayComments(self):
		res = ""
		for x in self.comments:
			res += x.display()
		return res
	
	def addComment(self, id, user, text):
		self.comments.append( Comment(id, user, text))
	
	def increaseScore(self):
		self.score += 1
	
	def decreaseScore(self):
		self.score -= 1
	
	def addUpVote(self,user):
		self.votedUsers[user] = 'upVote'
	
	def addDownVote(self,user):
		self.votedUsers[user] = 'downVote'
	
	def removeVote(self,user):
		self.votedUsers[user] = 'noVote'

class Comment(TextContainer):
	'''A comment in the system'''
	def __init__(self, id, user, text):
		super(Comment, self).__init__(id, user, "", text)
		
		self.score = 0
		
		self.votedUsers = {}
	
	def display(self, idTag="h6", userTag="h3", textTag="p"):
		res = ""
		res += makeTag(idTag, "Id: " + str(self.id))
		res += makeTag(userTag, "User: " + str(self.user))
		res += makeTag(textTag, self.text)
		return res
	
	def increaseScore(self):
		self.score += 1
	
	def decreaseScore(self):
		self.score -= 1
	
	def addUpVote(self,user):
		self.votedUsers[user] = 'upVote'
	
	def addDownVote(self,user):
		self.votedUsers[user] = 'downVote'
	
	def removeVote(self,user):
		self.votedUsers[user] = 'noVote'

class Inbox(object):
	'''Each user's inbox'''
	def __init__(self, user):
		self.user = user
		self.size = 0
		self.messages = []
	
	def listMessages(self):
		res = ""
		for message in self.messages:
			res += message.display()
		return res
	
	def sendMessage(self, recipient, title, message, request=False):
		'''Send a new message to a user'''
		counter = getCounter()
		userDict = objFileToList(directory, userFile, byName=True)
		#ignores title and message
		if request:
			userDict[recipient].inbox.messages.append(
							FriendRequest(counter, self.user, recipient,
							self.user + " would like to be friends with you"))
		else:
			userDict[recipient].inbox.messages.append(
							Message(counter, self.user, recipient, title, message))
		objListToFile(userDict, directory, userFile, isDict=True)
		setCounter(counter)

class Message(TextContainer):
	'''A message'''
	def __init__(self, id, srcUser, targUser, title, text, viewed=False):
		super(Message, self).__init__(id, "", title, text)
		self.srcUser = srcUser
		self.targUser = targUser
		self.viewed = viewed
		self.hasReplies = False
		self.replies = []
		self.replySrc = srcUser
		self.replyTarg = targUser
	
	def display(self):
		'''Display message contents in html'''
		res = ""
		print str(len(self.replies))
		if len(self.replies) == 0:
			print "no reply"
			res += makeTag("h6", self.id)
			res += makeTag("h5", "From: " + self.srcUser)
			res += makeTag("h3", self.title)
			res += makeTag("p", self.text)
		else:
			print "long"
			res += makeTag("h6", self.id)
			res += makeTag("h5", "From: " + \
			self.replies[len(self.replies) - 1].srcUser)
			
			res += makeTag("h3", self.title)
			
			res += makeTag("p",
						self.replies[len(self.replies) - 1].text)
		
		#for the first time a message is displayed
		#self.viewed = True
		return res
	
	def reply(self, text, userDict, currentUser):
		counter = getCounter()
		if not(self.hasReplies):
			print "fresh"
			self.hasReplies = True
			self.title = "Re: " + self.title
			#the original message is the first reply
			self.replies.append(copy.deepcopy(self))
		
		#make a new reply
		self.replies.append(
							Message(counter, self.replyTarg,
								self.replySrc, 
								"",
								text, True))
		#self.viewed = False
		
		
		
		hasBeenFound = False
		for index, message in enumerate(userDict[self.replyTarg].inbox.messages):
			if message.id == self.id:
				print "located"
				userDict[self.replyTarg].inbox\
								.messages[index] = copy.deepcopy(self)
				hasBeenFound = True
				break
		
		if not(hasBeenFound):
			print "new reply"
			userDict[self.replyTarg].inbox\
					.messages.append(copy.deepcopy(self))
		
		if not(self.replies[len(self.replies) - 1].targUser == self.replySrc):
			temp = self.targUser
			self.targUser = self.srcUser
			self.srcUser = temp
		
		setCounter(counter)

class FriendRequest(Message):
	'''A volatile type of message that treats viewed as an accept or decline'''
	def __init__(self, id, srcUser, targUser, text, viewed=False):
		super(FriendRequest, self).__init__(id,
									srcUser, targUser,
									"Friend request", text)
	
	
	def acceptRequest(self, usrDict):
		'''src and targ are pretty much interchangeable'''
		usrDict[self.srcUser].friends.append(self.targUser)
		usrDict[self.targUser].friends.append(self.srcUser)
		self.viewed = True
	
	def declineRequest(self):
		self.viewed = True
	
	def display(self):
		res = ""
		res += makeTag("h6", self.id)
		res += makeTag("h5", "From: " + self.srcUser)
		res += makeTag("h1", self.title)
		res += makeTag("h3", self.text)
		return res

class Group(object):
	'''A group of people'''
	def __init__(self, name, visibility, user):
		self.name = name
		self.members = []
		self.visibility = visibility
		self.posts = []
		self.admins = []
		self.admins.append(user)
		self.members.append(user)
	def changeVisibility(self,visibility2):
		self.visibility = visibility2
	def changeName(self, name):
		if name == '':
			pass
		else:
			self.name = name 
	def addPost(self,post):
		self.posts.append(post)
	def addMember(self, member):
		if member == '':
			pass
		else:
			self.members.append(member)
	def addAdmin(self, admin):
		if member == '':
			pass
		else:
			self.admins.append(admin)
	def kickMember(self, member):
		if member == '':
			pass
		else:
			self.members.remove(member)
	def kickAdmin(self, admin):
		self.admins.remove(admin)

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

def isFileEmpty(directory, fileN):
	'''Deprecated, do not use'''
	readStream = open(directory + fileN, "r")
	thing = readStream.read()
	readStream.close()
	if thing == "":
		return True
	return False

def objFileToList(directory, targFile, byName=False):
	'''Default makes a list, opt args can make dictionaries'''
	res = None
	with open(directory + targFile, "rb") as readStream:
		try:
			if byName:
				#res is a dictionary
				res = {}
				while True:
					temp = pickle.load(readStream)
					res[temp.name] = temp
			else:
				#res is a list
				res = []
				while True:
					res.append(pickle.load(readStream))
		except EOFError:
			pass
		except IndexError:
			pass
	
	return res

def objListToFile(objList, directory, targFile, isDict=False):
	"""Writes a list of objects to a file"""
	with open(directory + targFile, "wb") as objWStream:
		objWStream.write("")
		if isDict:
			for x in objList:
				pickle.dump(objList[x], objWStream)
		else:
			for x in objList:
				pickle.dump(x, objWStream)

def getCounter():
	counter = -1
	with open(directory + counterFile, "r") as countStream:
		counter = int(countStream.read())
	return counter

def setCounter(current):
	with open(directory + counterFile, "w") as countWStream:
		countWStream.write(str(current + 1))










