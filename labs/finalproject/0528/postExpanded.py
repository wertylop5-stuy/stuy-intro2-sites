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

def displayPost(id, cookie, titleTag, bodyTag, userTag, commentTag):
	res = ""
	userList = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)
	
	for x in userList:
		if x.name == cookie["username"].value:
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
						
						res += "<a href='postExpanded.py?downVote=lol&commentId="+\
	str(comment.id) + "'&postId='" + str(post.id) + "'>Down Vote</a><br>"
						
						res += "<a href='postExpanded.py?upVote=lol&commentId="+\
	str(comment.id) + "'&postId='" + str(post.id) + "'>Up Vote</a><br>"
						
						res += """</td>
	</tr>
</table>
"""
						
			break
	return res

def writeComment(targId, cookie, commentText):
	targName = cookie["username"].value
	allUsers = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.userFile)
	counter = stdStuff.getCounter()
	
	for index, value in enumerate(allUsers):
		if value.name == targName:
			for index2, value2 in enumerate(value.posts):
				if int(value2.id) == int(targId):
					value.posts[index2].addComment(counter, targName, commentText)
	stdStuff.objListToFile(allUsers, stdStuff.directory, stdStuff.userFile)
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
"""
			if "expandButton" in form:
				temp = int(form.getvalue("expandButton"))
				lol = open(stdStuff.directory + stdStuff.postIdFile, "w")
				lol.write(str(temp))
				lol.close()

			lol = open(stdStuff.directory + stdStuff.postIdFile, "r")
			targId = int(lol.read())
			lol.close()

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
									enumerate(value[index].comments):
										if int(value2.id) == int(commentId):
											value.comments[index2].decreaseScore()
											break
						elif "upVote" in form:
							for index, value in enumerate(x.posts):
								if value.id == targId:
									for index2, value2 in \
									enumerate(value[index].comments):
										if value2.id == commentId:
											value.comments[index2].increaseScore()
											break
				stdStuff.objListToFile(userList,
									stdStuff.directory, stdStuff.userFile)



			if "done" in form:
				writeComment(targId, c, form.getvalue("comment"))

			body += displayPost(targId, c, "", "", "", "")
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











