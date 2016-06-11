#! /usr/bin/python
import sys,pickle,cgitb,cgi,os,Cookie
sys.path.insert(0, "../modules")
import stdStuff

cgitb.enable()

print "content-type: text/html\n"


directory = '../data/'
f = open(directory + stdStuff.groupFile, 'r')
groupList = f.read()
f.close()

form = cgi.FieldStorage()


body = ''

foot = '''</body>
<html>'''


#print currentGroup
f = open(directory + stdStuff.groupFile, 'r')
groupList = f.read()
f.close()

userDict = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile, byName=True)
groupDict = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.groupFile, byName=True)
userList = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile)
groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)

def authenticate(u,ID,IP):
	loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
	loggedIn = [each.split(',') for each in loggedIn]
	loggedIn.remove([''])
	for a in loggedIn:
		if a[0] == username:
			return a[1]==str(ID) and a[2]==IP
	return False

def createNotMember():
	notMember = ''
	groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)
	for group in groupList:
		if group.name == currentGroup:
			userList = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile)
			for member in userList:     
				if not(member.name in group.members):
					notMember += '<option>' + (member.name) + '</option?> \n\t'
	return notMember

def createIsMember():
	isMember = ''
	groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)
	for group in groupList:
		if group.name == currentGroup:
			userList = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile)
			for member in userList:     
				if (member.name in group.members) and (member.name != currentUser):
					isMember += '<option>' + (member.name) + '</option?> \n\t'
	return isMember

def poster():
	return '''<form action = "groupsPage.py" method = "GET">
Title: <input name="postTitle" type="textfield">
<br>
Text: <textarea name="textBody" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" value = "Make Post">
</form>'''

def writePost(cookie, formThing):
	counter = stdStuff.getCounter()
	
	groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)
	
	for x in groupList:
		if x.name == currentGroup:
			x.addPost( stdStuff.Post(
							counter, 
							cookie["username"].value,
							formThing.getvalue("postTitle"),
							formThing.getvalue('textBody')))
			break
	
	stdStuff.setCounter(counter)
	stdStuff.objListToFile(groupList, stdStuff.directory, stdStuff.groupFile)

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

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

def displayPosts(cookie):
	res = ""
	
	#will sort
	totalPosts = []
	
	#all users in system
	groupDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.groupFile, byName=True)
	
	totalPosts.extend(groupDict[currentGroup].posts[:])

	'''
	#remember, the friends array only holds names
	for friend in userDict[currentUser].friends:
		totalPosts.extend(userDict[friend].posts[:])
	'''
	totalPosts.sort(key=lambda x: x.id, reverse=True)
	
	for post in totalPosts:
		res += """<table>
		<tr>
		<td>""" + str(post.score) + """</td>
		<td>
	"""
		res += post.display()
	
		res += "<a href='groupsPage.py?downVote=lol&postId="+\
str(post.id) + "'>Down Vote</a><br>"

		res += "<a href='groupsPage.py?upVote=lol&postId="+\
str(post.id) + "'>Up Vote</a><br>"
		res += "<a href='groupsPage.py?removeVote=lol&postId="+\
str(post.id) + "'>Remove Vote</a><br>" 
		res += """<a href='groupExpanded.py?expandButton=""" + \
str(post.id) + "'>Comment </a>"

		res += """</td>
	</tr>
	</table>
"""
	
	return res
'''
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
		currentUser = c['username'].value
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
<a href="profile.py">Go back to profile</a>
"""
currentUser = c['username'].value
#print currentUser

if 'displayGroups' in form:
	f = open(directory +  stdStuff.currentGroupFile, 'w')
	f.write(form.getvalue('displayGroups'))
	f.close()

groupStatus = ''

f = open(directory +  stdStuff.currentGroupFile, 'r')
currentGroup = f.read()
f.close()

if 'done' in form:
	if form.getvalue('done') == "Add Member":
		for group in groupList:
			if group.name == currentGroup:
				group.addMember(form.getvalue('addMember'))
				stdStuff.objListToFile(groupList, stdStuff.directory,
										stdStuff.groupFile,)
	if form.getvalue('done') == "Kick Member":
		for group in groupList:
			if group.name == currentGroup:
				group.kickMember(form.getvalue('kickMember'))
				stdStuff.objListToFile(groupList, stdStuff.directory,
										stdStuff.groupFile,)
	if form.getvalue('done') == "Change Visibility":
		for group in groupList:
			if group.name == currentGroup:
				group.changeVisibility(form.getvalue('visibility'))
				stdStuff.objListToFile(groupList, stdStuff.directory,
										stdStuff.groupFile,)
	if form.getvalue('done') == "Change Name":
		groupName = stdStuff.deleteBrackets(form.getvalue('groupName'))
		for group in groupList:
			if group.name == currentGroup:
				if groupName in groupDict.keys():
					global groupStatus
					groupStatus = "Group name is already taken. Group name has not been changed."
				else:
					group.changeName(groupName)
					f = open(directory +  stdStuff.currentGroupFile, 'w')
					f.write(groupName)
					f.close()
					f = open(directory +  stdStuff.currentGroupFile, 'r')
					currentGroup = f.read()
					f.close()
					stdStuff.objListToFile(groupList, stdStuff.directory,
										stdStuff.groupFile,)

body += groupStatus

notMember = createNotMember()
#print notMember
addMember = """Add Member:""" + \
	     '<form method = "GET" action = "groupsPage.py">' + \
	     '<select name = "addMember">' + \
	     notMember + \
	     """</select>\n\t""" + \
	     """<input type = "submit" name = "done" value = "Add Member">""" + \
	     """</form><br>\n"""
#body += addMember


isMember = createIsMember()
kickMember = """Kick Member:""" + \
	     '<form method = "GET" action = "groupsPage.py">' + \
	     '<select name = "kickMember">' + \
	     isMember + \
	     """</select>\n\t""" + \
	     """<input type = "submit" name = "done" value = "Kick Member">""" + \
	     """</form><br>\n"""
changeVisibility ="""Change Visibility:""" + \
	     '<form method = "GET" action = "groupsPage.py">' + \
	     '<select name = "visibility">' + \
	     '<option>public</option>' + \
	     '<option>private</option' + \
	     """</select>\n\t""" + \
	     """<input type = "submit" name = "done" value = "Change Visibility">""" + \
	     """</form><br>\n"""
changeName ="""Change Group Name:""" + \
	     '<form method = "GET" action = "groupsPage.py">' + \
	     '<input type = "text" name = "groupName">' + \
	     """<input type = "submit" name = "done" value = "Change Name">""" + \
	     """</form><br>\n"""
#body += kickMember
for group in groupList:
		if group.name == currentGroup:
			userList = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile)
			for member in userList:     
				if (member.name in group.admins) and (currentUser == member.name):
					if len(notMember) > 0:
						body += addMember
					if len(isMember) > 0:  
						body += kickMember
					body += changeVisibility
					body += changeName
'''


	


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
<a href="profile.py">Go back to profile</a>
<br>
<br>
<br>
"""
			body += """<a href = "groups.py">Back to Groups </a>
	<br>
	<form>
		Search for people: <input type = "text" name = "user">
		<input type = "submit" value = "Commence Search">
	</form>"""
			currentUser = c['username'].value
			#print currentUser

			if 'displayGroups' in form:
				f = open(directory +  stdStuff.currentGroupFile, 'w')
				f.write(form.getvalue('displayGroups'))
				f.close()

			groupStatus = ''

			f = open(directory +  stdStuff.currentGroupFile, 'r')
			currentGroup = f.read()
			f.close()

			if 'done' in form:
				if form.getvalue('done') == "Add Member":
					for group in groupList:
						if group.name == currentGroup:
							group.addMember(form.getvalue('addMember'))
							stdStuff.objListToFile(groupList, stdStuff.directory,
													stdStuff.groupFile,)
				if form.getvalue('done') == "Kick Member":
					for group in groupList:
						if group.name == currentGroup:
							group.kickMember(form.getvalue('kickMember'))
							stdStuff.objListToFile(groupList, stdStuff.directory,
													stdStuff.groupFile,)
				if form.getvalue('done') == "Change Visibility":
					for group in groupList:
						if group.name == currentGroup:
							group.changeVisibility(form.getvalue('visibility'))
							stdStuff.objListToFile(groupList, stdStuff.directory,
													stdStuff.groupFile,)
				if form.getvalue('done') == "Change Name":
					groupName = stdStuff.deleteBrackets(form.getvalue('groupName'))
					for group in groupList:
						if group.name == currentGroup:
							if groupName in groupDict.keys():
								global groupStatus
								groupStatus = "Group name is already taken. Group name has not been changed."
							else:
								group.changeName(groupName)
								f = open(directory +  stdStuff.currentGroupFile, 'w')
								f.write(groupName)
								f.close()
								f = open(directory +  stdStuff.currentGroupFile, 'r')
								currentGroup = f.read()
								f.close()
								stdStuff.objListToFile(groupList, stdStuff.directory,
													stdStuff.groupFile,)

			body += groupStatus

			notMember = createNotMember()
			#print notMember
			addMember = '''Add Member:''' + \
					 '<form method = "GET" action = "groupsPage.py">' + \
					 '<select name = "addMember">' + \
					 notMember + \
					 '''</select>\n\t''' + \
					 '''<input type = "submit" name = "done" value = "Add Member">''' + \
					 '''</form><br>\n'''
			#body += addMember


			isMember = createIsMember()
			kickMember = '''Kick Member:''' + \
					 '<form method = "GET" action = "groupsPage.py">' + \
					 '<select name = "kickMember">' + \
					 isMember + \
					 '''</select>\n\t''' + \
					 '''<input type = "submit" name = "done" value = "Kick Member">''' + \
					 '''</form><br>\n'''
			changeVisibility ='''Change Visibility:''' + \
					 '<form method = "GET" action = "groupsPage.py">' + \
					 '<select name = "visibility">' + \
					 '<option>public</option>' + \
					 '<option>private</option' + \
					 '''</select>\n\t''' + \
					 '''<input type = "submit" name = "done" value = "Change Visibility">''' + \
					 '''</form><br>\n'''
			changeName ='''Change Group Name:''' + \
					 '<form method = "GET" action = "groupsPage.py">' + \
					 '<input type = "text" name = "groupName">' + \
					 '''<input type = "submit" name = "done" value = "Change Name">''' + \
					 '''</form><br>\n'''
			#body += kickMember
			for group in groupList:
					if group.name == currentGroup:
						userList = stdStuff.objFileToList(stdStuff.directory,
										stdStuff.userFile)
						for member in userList:     
							if (member.name in group.admins) and (currentUser == member.name):
								if len(notMember) > 0:
									body += addMember
								if len(isMember) > 0:  
									body += kickMember
								body += changeVisibility
								body += changeName
			
			
			
			
			if "postTitle" in form:
				writePost(c, form)
			
			if ("downVote" in form) or ("upVote" in form) or ("noVote" in form):
				targId = int(form.getvalue("postId"))
				targName = c["username"].value
				currentUser = c["username"].value
				groupDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.groupFile, byName=True)
				
				name = groupDict[currentGroup]
				if "downVote" in form:
					for index, value in enumerate(name.posts):
						print name.posts[index].votedUsers
						print name.posts[index].score
						if value.id == targId and (not (currentUser in name.posts[index].votedUsers.keys())):
							name.posts[index].decreaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addDownVote(currentUser)
						if value.id == targId and (name.posts[index].votedUsers[currentUser] == 'noVote'):
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addDownVote(currentUser)
						if value.id == targId and (name.posts[index].votedUsers[currentUser] == 'upVote'):
							name.posts[index].decreaseScore()
							name.posts[index].decreaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addDownVote(currentUser)
							break
				if "upVote" in form:
					for index, value in enumerate(name.posts):
						print name.posts[index].votedUsers
						print name.posts[index].score
						if value.id == targId and (not (currentUser in name.posts[index].votedUsers.keys())):
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addUpVote(currentUser)
						if value.id == targId and (name.posts[index].votedUsers[currentUser] == 'noVote'):
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addUpVote(currentUser)
						if value.id == targId and (name.posts[index].votedUsers[currentUser] == 'downVote'):
							name.posts[index].increaseScore()
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addUpVote(currentUser)
							break
				if "removeVote" in form:
					for index, value in enumerate(name.posts):
						print name.posts[index].votedUsers
						print name.posts[index].score
						if value.id == targId and ((not (currentUser in name.posts[index].votedUsers.keys()))):
							pass
							#x.posts[index].votedUsers[x.name] = "upVote"
						if value.id == targId and ((name.posts[index].votedUsers[currentUser] == 'downVote')):
							name.posts[index].increaseScore()
							name.posts[index].removeVote(currentUser)
							#x.posts[index].votedUsers[x.name] = "upVote"
						if value.id == targId and (name.posts[index].votedUsers[currentUser] == 'upVote'):     
							name.posts[index].decreaseScore()
							name.posts[index].removeVote(currentUser)
									
							#x.posts[index].votedUsers[x.name] = "upVote"
						
						break
				stdStuff.objListToFile(userDict, stdStuff.directory,
										stdStuff.userFile, isDict=True)
				stdStuff.objListToFile(groupDict, stdStuff.directory,
										stdStuff.groupFile, isDict=True)
				'''
				targId = int(form.getvalue("postId"))
				targName = c["username"].value
				
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				
				name = userDict[targName]
				if "downVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId and (not (name in name.posts[index].votedUsers.keys()) or (name.posts[index].votedUsers[name] != 'downVote')):
							name.posts[index].decreaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addDownVote(name)
							break
				elif "upVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId and (not (name in name.posts[index].votedUsers.keys()) or (name.posts[index].votedUsers[name] != 'upVote')):
							name.posts[index].increaseScore()
							#x.posts[index].votedUsers[x.name] = "upVote"
							name.posts[index].addUpVote(name)
							break
				stdStuff.objListToFile(userDict, stdStuff.directory,
										stdStuff.userFile, isDict=True)
				'''
			
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







head = \
'''
<!DOCTYPE html>
<html>
	<head><title>''' + currentGroup + '''</title>
	</head>
	<body>
'''

					
print head
print body
print foot
