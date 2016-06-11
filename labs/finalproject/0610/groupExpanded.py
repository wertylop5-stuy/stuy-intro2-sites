#!/usr/bin/python
#This file is to view an expanded file
print 'content-type: text/html'
print ''
import cgitb,cgi,sys,os,Cookie,pickle
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff
directory = '../data/'


head = '''<!DOCTYPE html>
<html>
<head><title>Comments on this post</title>
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''

form = cgi.FieldStorage()


f = open(directory + stdStuff.groupFile, 'r')
groupList = f.read()
f.close()

if 'displayGroups' in form:
	f = open(directory +  stdStuff.currentGroupFile, 'w')
	f.write(form.getvalue('displayGroups'))
	f.close()

groupStatus = ''

f = open(directory +  stdStuff.currentGroupFile, 'r')
currentGroup = f.read()
f.close()


userDict = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile, byName=True)
groupDict = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.groupFile, byName=True)
userList = stdStuff.objFileToList(stdStuff.directory,
							stdStuff.userFile)
groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)
#gordons code
def poster():
	return '''<br>
<br>
<br>
<br>
<form action = "groupExpanded.py" method = "GET">
Text: <textarea name="comment" rows="10" cols="15">
</textarea>
<br>
<input name="done" type="submit" value="Make comment">
</form>'''

def displayPost(id, cookie, titleTag, bodyTag, userTag, commentTag):
	res = ""
	groupList = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.groupFile)
	
	for x in groupList:
		if (x.name == currentGroup):
			for post in x.posts:
				if post.id == id:
					res += post.display()
					res += "<br><h3>Comments</h3><br>"
					
					for comment in post.comments:
						res += """<table>
<tr>
	<td>""" + str(comment.score) + """</td>
	<td>
"""
						res += comment.display()
						
						res += "<a href='groupExpanded.py?downVote=lol&commentId="+\
	str(comment.id) + "'&postId='" + str(post.id) + "'>Down Vote</a><br>"
						
						res += "<a href='groupExpanded.py?upVote=lol&commentId="+\
	str(comment.id) + "'&postId='" + str(post.id) + "'>Up Vote</a><br>"
						res += "<a href='groupExpanded.py?removeVote=lol&commentId="+\
	str(comment.id) + "'&postId='" + str(post.id) + "'>Remove Vote</a><br>"
						
						res += """</td>
	</tr>
</table>
"""
						
			break
	if 'searchUserPost' in form:
		for x in groupList:
			if (x.name == searchUserPost):
				for post in x.posts:
					if post.id == id:
						res += post.display()
						res += "<br><h3>Comments</h3><br>"
						
						for comment in post.comments:
							res += """<table>
	<tr>
		<td>""" + str(comment.score) + """</td>
		<td>
	"""
							res += comment.display()
							
							res += "<a href='groupExpanded.py?downVote=lol&commentId="+\
		str(comment.id) + "'&postId='" + str(post.id) + "'>Down Vote</a><br>"
							
							res += "<a href='groupExpanded.py?upVote=lol&commentId="+\
		str(comment.id) + "'&postId='" + str(post.id) + "'>Up Vote</a><br>"
							res += "<a href='groupExpanded.py?removeVote=lol&commentId="+\
                str(comment.id) + "'&postId='" + str(post.id) + "'>Remove Vote</a><br>"
							res += """</td>
		</tr>
	</table>
	"""
							
					break
	return res

def writeComment(targId, cookie, commentText):
	targName = currentGroup
	currentUser = c['username'].value
	groupList = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.groupFile)
	counter = stdStuff.getCounter()
	
	for index, value in enumerate(groupList):
		if value.name == targName:
			for index2, value2 in enumerate(value.posts):
				if int(value2.id) == int(targId):
					value.posts[index2].addComment(counter, currentUser, commentText)
	stdStuff.objListToFile(groupList, stdStuff.directory, stdStuff.groupFile)
	stdStuff.setCounter(counter)

def authenticate(u,ID,IP):
    loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
	    if a[0] == username:
		    return a[1]==str(ID) and a[2]==IP
    return False

c = None
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c = Cookie.SimpleCookie()
	c.load(cookie_string)
	##print all the data in the cookie
	#body+= "<h1>cookie data</h1>"
	#for each in c:
	#    body += each+":"+str(c[each].value)+"<br>"
	
	
	if 'username' in c and 'ID' in c:
		username = c['username'].value
		ID = c['ID'].value
		IP = os.environ['REMOTE_ADDR']
		
		if authenticate(username,ID,IP):
			body += """<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
<a href="profile.py">Go back to profile</a>
"""
			if "expandButton" in form:
				temp = int(form.getvalue("expandButton"))
				lol = open(stdStuff.directory + stdStuff.postIdFile, "w")
				lol.write(str(temp))
				lol.close()

			lol = open(stdStuff.directory + stdStuff.postIdFile, "r")
			targId = int(lol.read())
			lol.close()

			if 'searchUserPost' in form:
				searchUserPost = str(form.getvalue('searchUserPost'))
			
			if "downVote" in form or "upVote" in form or "removeVote" in form:
				commentId = int(form.getvalue("commentId"))
	
				currentUser = c["username"].value
				targName = c["username"].value
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				
				
				groupList = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.groupFile)
				targGroup = currentGroup
				name = groupDict[targGroup]
				'''
				for x in groupList:
					if x.name == targGroup:
						if "downVote" in form:
							for index, value in enumerate(name.posts):
								#print name.posts[index].votedUsers
								#print name.posts[index].score
								for index2, value2 in \
									enumerate(value.comments):
										if int(value2.id) == int(commentId) and (not (currentUser in name.posts[index].comments[index2].votedUsers.keys())):
											name.posts[index].comments[index2].decreaseScore()
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].addDownVote(currentUser)
											break
										if int(value2.id) == int(commentId) and (name.posts[index].comments[index2].votedUsers[currentUser] == 'noVote'):
											name.posts[index].comments[index2].decreaseScore()
											name.posts[index].comments[index2].addDownVote(currentUser)
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].comments[index2].addDownVote(currentUser)
										if int(value2.id) == int(commentId) and (name.posts[index].comments[index2].votedUsers[currentUser] == 'upVote'):
											name.posts[index].comments[index2].decreaseScore()
											name.posts[index].comments[index2].decreaseScore()
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].addDownVote(currentUser)
											break
						if "upVote" in form:
							for index, value in enumerate(name.posts):
								#print name.posts[index].votedUsers
								#print name.posts[index].score
								for index2, value2 in \
									enumerate(value.comments):
										if int(value2.id) == int(commentId) and (not (currentUser in name.posts[index].comments[index2].votedUsers.keys())):
											name.posts[index].comments[index2].increaseScore()
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].addUpVote(currentUser)
											break
										if int(value2.id) == int(commentId) and (name.posts[index].comments[index2].votedUsers[currentUser] == 'noVote'):
											name.posts[index].comments[index2].increaseScore()
											name.posts[index].comments[index2].addUpVote(currentUser)
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].comments[index2].addDownVote(currentUser)
										if int(value2.id) == int(commentId) and (name.posts[index].comments[index2].votedUsers[currentUser] == 'downVote'):
											name.posts[index].comments[index2].increaseScore()
											name.posts[index].comments[index2].increaseScore()
											#x.posts[index].votedUsers[x.name] = "upVote"
											name.posts[index].comments[index2].addUpVote(currentUser)
											break
						if "removeVote" in form:
							for index, value in enumerate(name.posts):
								#print name.posts[index].votedUsers
								#print name.posts[index].score
								for index2, value2 in \
									enumerate(value.comments):
										if int(value2.id) == int(commentId) and ((not (currentUser in name.posts[index].comments[index2].votedUsers.keys()))):
											pass
											#x.posts[index].votedUsers[x.name] = "upVote"
										if int(value2.id) == int(commentId) and ((name.posts[index].comments[index2].votedUsers[currentUser] == 'downVote')):
											name.posts[index].comments[index2].increaseScore()
											name.posts[index].comments[index2].removeVote(currentUser)
											#x.posts[index].votedUsers[x.name] = "upVote"
										if int(value2.id) == int(commentId) and (name.posts[index].comments[index2].votedUsers[currentUser] == 'upVote'):     
											name.posts[index].comments[index2].decreaseScore()
											name.posts[index].comments[index2].removeVote(currentUser)
											
									#x.posts[index].votedUsers[x.name] = "upVote"
						
						break
				'''
				for x in groupList:
					if x.name == targGroup:
						if "downVote" in form:
							for index, value in enumerate(name.posts):
								if value.id == targId:
									for comment in value.comments:
										if comment.id == commentId:
											if not(targName in \
											comment.votedUsers.keys()) or\
											comment.votedUsers[targName] ==\
											"noVote":
												comment.decreaseScore()
								
												comment.addDownVote(targName)
											elif (comment.votedUsers[targName] !=\
											'downVote'):
												comment.decreaseScore()
												comment.decreaseScore()
								
												comment.addDownVote(targName)
											break
				
						elif "upVote" in form:
							for index, value in enumerate(name.posts):
								if value.id == targId:
									for comment in value.comments:
										if comment.id == commentId:
											if not(targName in \
											comment.votedUsers.keys()) or\
											comment.votedUsers[targName] ==\
											"noVote":
												comment.increaseScore()
								
												comment.addUpVote(targName)
											elif (comment.votedUsers[targName] !=\
											'upVote'):
												comment.increaseScore()
												comment.increaseScore()
								
												comment.addUpVote(targName)
											break
				
				
						elif "removeVote" in form:
							for index, value in enumerate(name.posts):
								if value.id == targId:
									for comment in value.comments:
										if targName in comment\
															.votedUsers.keys():
											if comment.votedUsers[targName] == \
											"upVote":
												comment\
												.votedUsers[targName] = "noVote"
									
												comment.decreaseScore()
								
											elif comment.votedUsers[targName] == \
											"downVote":
												comment\
												.votedUsers[targName] = "noVote"
									
												comment.increaseScore()
											break
				
				stdStuff.objListToFile(groupDict, stdStuff.directory,
										stdStuff.groupFile, isDict=True)



			if "done" in form:
				writeComment(targId, c, form.getvalue("comment"))

			body += displayPost(targId, c, "", "", "", "")
			body += poster()

			body += """<a href="groupsPage.py">Go back to group page</a>"""
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











