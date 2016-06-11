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
	<head><title>Search</title>
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
		body += "Logged in as: " + username
		body += \
		'''
	<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
	<a href = "profile.py">Back to Profile </a>'''
		body += displayInboxWidget(c)
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
	
			if "downVote" in form or "upVote" in form:
				targId = int(form.getvalue("postId"))
				targName = form.getvalue('user')
				currentUser = c["username"].value
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
		
				name = userDict[targName]
				if "downVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId and (not (currentUser in name.posts[index].votedUsers.keys()) or (name.posts[index].votedUsers[currentUser] != 'downVote')):
							name.posts[index].decreaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addDownVote(currentUser)
							break
				elif "upVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId and (not (currentUser in name.posts[index].votedUsers.keys()) or (name.posts[index].votedUsers[currentUser] != 'upVote')):
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addUpVote(currentUser)
							break
				stdStuff.objListToFile(userDict, stdStuff.directory,
											stdStuff.userFile, isDict=True)
	
			for x in userList:
				if x.name == searchUser:
					#body += x.displayPosts()
					body += x.displaySearchPostsWithVoter(searchUser)
					found = True
			if found:
				#Add Friend option
				body+= '''<a href = 'search.py?user=''' + searchUser + '''&add=friend'>Add Friend</a>'''    

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
