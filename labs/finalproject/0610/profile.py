#!/usr/bin/python
print 'content-type: text/html\n'
#TODO include \n in posts, friends, fix gordon voting sys
import Cookie,os,cgi,pickle,sys,cgitb,hashlib

cgitb.enable()

sys.path.insert(0, "../modules")
import stdStuff

head = '''<!DOCTYPE html>
<html>
<head><title>Profile</title>
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''



form = cgi.FieldStorage()

def authenticate(u,ID,IP):
	loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
	loggedIn = [each.split(',') for each in loggedIn]
	loggedIn.remove([''])
	for a in loggedIn:
		if a[0] == username:
			return a[1]==str(ID) and a[2]==IP
	return False

splitChar = chr(182)
splitPost = chr(208)

#gordons code
def poster():
	return '''<form action = 'search.py'>
Search by User: <input type = 'text' name = 'user'>
<input type = 'submit' value = 'Commence Search'>
</form>
<br>
''' +\
'''<form action = "profile.py" method = "GET">
Title: <input name="postTitle" type="textfield">
<br>
Text: <textarea name="textBody" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" value = "Make Post">
</form>'''

def writePost(cookie, formThing):
	counter = stdStuff.getCounter()
	
	userList = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)
	
	for x in userList:
		if x.name == cookie["username"].value:
			x.addPost(stdStuff.Post(
					counter, 
					cookie["username"].value,
					stdStuff.deleteBrackets(formThing.getvalue("postTitle")),
					stdStuff.deleteBrackets(formThing.getvalue('textBody'))))
			break
	
	stdStuff.setCounter(counter)
	stdStuff.objListToFile(userList, stdStuff.directory, stdStuff.userFile)

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

def displayPosts(cookie):
	currentUser = cookie["username"].value
	res = ""
	
	#will sort
	totalPosts = []
	
	#all users in system
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	totalPosts.extend(userDict[currentUser].posts[:])
	
	#remember, the friends array only holds names
	for friend in userDict[currentUser].friends:
		totalPosts.extend(userDict[friend].posts[:])
	
	totalPosts.sort(key=lambda x: x.id, reverse=True)
	
	for post in totalPosts:
		res += """<table>
		<tr>
		<td>""" + str(post.score) + """</td>
		<td>
	"""
		res += post.display()
	
		res += "<a href='profile.py?downVote=lol&postId="+\
str(post.id) + "'>Down Vote</a><br>"

		res += "<a href='profile.py?upVote=lol&postId="+\
str(post.id) + "'>Up Vote</a><br>"
		res += "<a href='profile.py?removeVote=lol&postId="+\
str(post.id) + "'>Remove Vote</a><br>"
		res += """<a href='postExpanded.py?expandButton=""" + \
str(post.id) + "'>Comment </a>"

		res += """</td>
	</tr>
	</table>
"""
	
	return res

def displayInboxWidget(cookie):
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div align='right'>
	<table border='1'>
		<tr>
			<td>
				<a href="inbox.py">View messages</a>
			</td>
		</tr>
	</table>
</div>
"""
	return res

def displayGroupWidget(cookie):
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div align='right'>
	<table border='1'>
		<tr>
			<td>
				<a href="groups.py">View groups</a>
			</td>
		</tr>
	</table>
</div>
"""
	return res

def makePage(cookie):
	res = ""
	currentUser = cookie["username"].value
	res += displayInboxWidget(cookie)
	res += displayGroupWidget(cookie)
	res += str(poster())
	res += displayPosts(cookie)
	return res
	


if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	##print all the data in the cookie
	#body+= "<h1>cookie data</h1>"
	#for each in c:
	#	body += each+":"+str(c[each].value)+"<br>"


	
	if 'username' in c and 'ID' in c:
		username = c['username'].value
		ID = c['ID'].value
		IP = os.environ['REMOTE_ADDR']
		
		if authenticate(username,ID,IP):
			### PUT PAGE STUFF HERE
			body += "Logged in as: " + username
			body += """<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
"""
			if "postTitle" in form:
				writePost(c, form)
			currentUser = c["username"].value
			
			if ("downVote" in form) or ("upVote" in form) or ("removeVote" in form):
				targId = int(form.getvalue("postId"))
				targName = c["username"].value
				
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				
				name = userDict[targName]
				if "downVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId: 
							if not(currentUser in \
							name.posts[index].votedUsers.keys()) or\
							name.posts[index].votedUsers[currentUser] == "noVote":
								name.posts[index].decreaseScore()
								
								name.posts[index].addDownVote(currentUser)
							elif (name.posts[index].votedUsers[currentUser] !=\
							'downVote'):
							
								name.posts[index].decreaseScore()
								name.posts[index].decreaseScore()
								
								name.posts[index].addDownVote(currentUser)
							
							break
				
				elif "upVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId:
							if not(currentUser in \
							name.posts[index].votedUsers.keys()) or\
							name.posts[index].votedUsers[currentUser] == "noVote":
								name.posts[index].increaseScore()
								
								name.posts[index].addUpVote(currentUser)
							elif (name.posts[index].votedUsers[currentUser] !=\
							'upVote'):
								name.posts[index].increaseScore()
								name.posts[index].increaseScore()
								
								name.posts[index].addUpVote(currentUser)
							
							break
				
				
				elif "removeVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId:
							if currentUser in name.posts[index]\
												.votedUsers.keys():
								if name.posts[index] \
								.votedUsers[currentUser] == "upVote":
									name.posts[index]\
									.votedUsers[currentUser] = "noVote"
									
									name.posts[index].decreaseScore()
								
								elif name.posts[index] \
								.votedUsers[currentUser] == "downVote":
									name.posts[index]\
									.votedUsers[currentUser] = "noVote"
									
									name.posts[index].increaseScore()
								
							break
				
				
				stdStuff.objListToFile(userDict, stdStuff.directory,
										stdStuff.userFile, isDict=True)
			
			body+=makePage(c)
		else:
			body+="Failed to Authenticate cookie<br>\n"
			body+= 'Go Login <a href="login.py">here</a><br>'
	else:
		body+= "Your information expired<br>\n"
		body+= 'Go Login <a href="login.py">here</a><br>'
else:
	body+= 'You seem new<br>\n'
	body+='Go Login <a href="login.py">here</a><br>'







print head
print body
print foot
