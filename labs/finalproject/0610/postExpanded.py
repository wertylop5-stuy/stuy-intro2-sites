#!/usr/bin/python
#This file is to view an expanded file

print 'content-type: text/html'
print ''
import cgitb,cgi,sys,os,Cookie,pickle
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff

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








#gordons code
def poster():
	return '''<br>
<br>
<br>
<br>
<form action = "postExpanded.py" method = "GET">
Text: <textarea name="comment" rows="10" cols="15">
</textarea>
<br>
<input name="done" type="submit" value="Make comment">
</form>'''

def displayPost(id, currentUser, titleTag, bodyTag, userTag, commentTag):
	res = ""
	userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
	
	for post in userDict[currentUser].posts:
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
				
				res += "<a href='postExpanded.py?downVote=lol&commentId="+\
str(comment.id) + "&postId=" + str(post.id) + "'>Down Vote</a><br>"
					
				res += "<a href='postExpanded.py?upVote=lol&commentId="+\
str(comment.id) + "&postId=" + str(post.id) + "'>Up Vote</a><br>"
				
				res += "<a href='postExpanded.py?removeVote=lol&commentId="+\
str(comment.id) + "&postId=" + str(post.id) + "'>Remove Vote</a><br>"
				
				res += """</td>
	</tr>
</table>
"""
			return res
	
	for friend in userDict[currentUser].friends:
		for post in userDict[friend].posts:
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
				
					res += "<a href='postExpanded.py?downVote=lol&commentId="+\
	str(comment.id) + "&postId=" + str(post.id) + "'>Down Vote</a><br>"
					
					res += "<a href='postExpanded.py?upVote=lol&commentId="+\
str(comment.id) + "&postId=" + str(post.id) + "'>Up Vote</a><br>"
					
					res += "<a href='postExpanded.py?removeVote=lol&commentId="+\
str(comment.id) + "&postId=" + str(post.id) + "'>Remove Vote</a><br>"
				
					res += """</td>
	</tr>
</table>
"""
					return res
	return res

def writeComment(targId, currentUser, commentText):
	userDict = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.userFile, byName=True)
	counter = stdStuff.getCounter()
	
	for post in userDict[currentUser].posts:
		if post.id == targId:
			post.addComment(counter, currentUser, commentText)
			stdStuff.objListToFile(userDict, stdStuff.directory,
							stdStuff.userFile, isDict=True)
			stdStuff.setCounter(counter)
			return
	
	for friend in userDict[currentUser].friends:
		for post in userDict[friend].posts:
			if post.id == targId:
				post.addComment(counter, currentUser, commentText)
				stdStuff.objListToFile(userDict, stdStuff.directory,
								stdStuff.userFile, isDict=True)
				stdStuff.setCounter(counter)
				return


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
			body += "Logged in as: " + username
			body += """<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
<a href="profile.py">Go back to profile</a>
"""
			body += displayInboxWidget(c)
			body += displayGroupWidget(c)
			if "expandButton" in form:
				temp = int(form.getvalue("expandButton"))
				lol = open(stdStuff.directory + stdStuff.postIdFile, "w")
				lol.write(str(temp))
				lol.close()

			lol = open(stdStuff.directory + stdStuff.postIdFile, "r")
			targId = int(lol.read())
			lol.close()
			'''
			if "downVote" in form or "upVote" in form:
				commentId = int(form.getvalue("commentId"))
				targName = c["username"].value
	
				userList = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile)
	
				for x in userList:
					if x.name == targName:
						if "downVote" in form:
							for index, value in enumerate(x.posts):
								if value.id == targId:
									for index2, value2 in \
									enumerate(value.comments):
										if int(value2.id) == int(commentId):
											value.comments[index2].decreaseScore()
											break
						elif "upVote" in form:
							for index, value in enumerate(x.posts):
								if value.id == targId:
									for index2, value2 in \
									enumerate(value.comments):
										if value2.id == commentId:
											value.comments[index2].increaseScore()
											break
				'''
			if ("downVote" in form) or ("upVote" in form) or ("removeVote" in form):
				targId = int(form.getvalue("postId"))
				commentId = int(form.getvalue("commentId"))
				targName = c["username"].value
				
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				
				name = userDict[targName]
				
				if "downVote" in form:
					for index, value in enumerate(name.posts):
						if value.id == targId:
							for comment in value.comments:
								if comment.id == commentId:
									if not(targName in \
									comment.votedUsers.keys()) or\
									comment.votedUsers[targName] == "noVote":
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
									comment.votedUsers[targName] == "noVote":
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
				
				
				stdStuff.objListToFile(userDict, stdStuff.directory,
									stdStuff.userFile, isDict=True)



			if "done" in form:
				writeComment(targId, username, form.getvalue("comment"))

			body += displayPost(targId, c["username"].value, "", "", "", "")
			body += poster()

			body += """<a href="profile.py">Go back to profile</a>"""
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











