#! /usr/bin/python
import sys,pickle,cgitb,cgi,os,Cookie
#TODO redirect add friend link to addFriend.py with argument in url
print "content-type: text/html\n"
cgitb.enable()
form = cgi.FieldStorage()

sys.path.insert(0, "../modules")
import stdStuff

head = """<!DOCTYPE html>
<html>
	<head>
		<title>Search</title>
		<link rel="stylesheet" type="text/css" href="../style/search.css">
	</head>
	<body>
"""
body = ""
foot = """
				</td>
			</tr>
		</table>
	</body>
</html>"""

def authenticate(u,ID,IP):
	loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
	loggedIn = [each.split(',') for each in loggedIn]
	loggedIn.remove([''])
	for a in loggedIn:
		if a[0] == username:
			return a[1]==str(ID) and a[2]==IP
	return False

def displayInboxWidget(cookie):
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div class="widget" id="inboxWidget">
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
<div class="widget" id="groupWidget">
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

def displayPosts(cookie, target):
	currentUser = cookie["username"].value
	res = ""
	
	#will sort
	totalPosts = []
	
	#all users in system
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	totalPosts.extend(userDict[target].posts[:])
	
	#remember, the friends array only holds names
	'''for friend in userDict[currentUser].friends:
		totalPosts.extend(userDict[friend].posts[:])'''
	
	totalPosts.sort(key=lambda x: x.id, reverse=True)
	
	for post in totalPosts:
		res += """<table class="post">
		<tr>
		<td>""" + str(post.score) + """</td>
		<td>
	"""
		res += post.display()
	
		res += "<a href='search.py?downVote=lol&postId="+\
str(post.id) + "&user=" + str(target) + "'>Down Vote</a><br>"

		res += "<a href='search.py?upVote=lol&postId="+\
str(post.id) + "&user=" + str(target) + "'>Up Vote</a><br>"
		res += "<a href='search.py?removeVote=lol&postId="+\
str(post.id) + "&user=" + str(target) + "'>Remove Vote</a><br>"
		res += """<a href='postExpanded.py?expandButton=""" + \
str(post.id) + "'>Comment </a>"

		res += """</td>
	</tr>
	</table>
"""
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
		body += "<div id='userHeader'>"
		body += """
<div id="username">
<p>Logged in as: """ + \
username + \
"""</p>
</div>"""
		body += """
<div id="userButtons">
<form method="GET" action="homepage.py">
	<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
	<input name="addFriend" type="submit" value="Add a friend">
</form>
<a href="profile.py">Go back to profile</a>
</div>
</div>
"""
		#for the fixed post
		body += "<div id='userHeader2'></div>"
			
		body += displayInboxWidget(c)
		body += displayGroupWidget(c)
		body +='''
	<br>
	<form>
		Search for people: <input type = "text" name = "user">
		<input type = "submit" value = "Commence Search">
	</form>
'''


		if len(form) > 0:
	
			searchUser = form.getvalue('user')
			found = False
			userList = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)
			'''for x in userList:
				if x.name == c["username"].value:
					user = x'''
			body+= "<h1>Searched Name: " + searchUser + "</h1>"
			#print userList
			
			userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
			currentUser = c["username"].value
			if ("downVote" in form) or ("upVote" in form) or ("removeVote" in form):
				targId = int(form.getvalue("postId"))
				targName = form.getvalue('user')
				currentUser = c["username"].value
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
							
	
			for x in userList:
				if x.name == searchUser:
					if x.name == currentUser:
						#body += x.displaySearchPostsWithVoter(searchUser)
						body += displayPosts(c, x.name)
						found = True
					elif x.name in userDict[currentUser].friends:
						#body += x.displayPosts()
						#body += x.displaySearchPostsWithVoter(searchUser)
						body += displayPosts(c, x.name)
						found = True
					else:
						#Add Friend option
						body+= '''<a href='addFriend.py?userTarget=''' + searchUser + '''&search=Find+User'>Add Friend</a>'''
						found = True
			if not found:
				    body += "<h2>That's not a registered user!</h2>"

			if 'add' in form:
				#Later repalce with send friend request
				if searchUser == c['username'].value:
					body+= 'You cannot be friends with yourself ;=;<br>'
				elif not(searchUser in user.friends):
					   user.addFriend(searchUser)
					   body+= 'Added friend<br>'
				elif searchUser in user.friends:
					body+= "Friend is already in friend list<br>"

			if len(body) == 0 and found:
				body+= "User has not posted anything yet!"
			elif len(body) == 0:
				body+= "User is not found."
	
print head
print body
print foot
