#!/usr/bin/python
print 'content-type: text/html\n'
#TODO include \n in posts, friends, fix up post displaying and upvotes
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
	return '''<form action = "profile.py" method = "GET">
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
			x.addPost( stdStuff.Post(
							counter, 
							cookie["username"].value,
							formThing.getvalue("postTitle"),
							formThing.getvalue('textBody')))
			break
	
	stdStuff.setCounter(counter)
	stdStuff.objListToFile(userList, stdStuff.directory, stdStuff.userFile)

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"
'''
#reads in posts
def displayPost(postObj, titleTag, bodyTag, userTag, commentTag=""):
	postResult = ""
	
	postResult += """<table>
<tr>
	<td>""" + str(postObj.score) + """</td>
	<td>
"""
	
	postResult +=	makeTag(userTag, postObj.id) + \
					makeTag(userTag, postObj.user) + \
					makeTag(titleTag, postObj.title) + \
					makeTag(bodyTag, postObj.text)
	
	postResult += "<a href='profile.py?downVote=lol&postId="+\
	str(postObj.id) + "'>Down Vote</a><br>"
	
	postResult += "<a href='profile.py?upVote=lol&postId="+\
	str(postObj.id) + "'>Up Vote</a><br>"
	
	postResult += """<a href='postExpanded.py?expandButton=""" + \
	str(postObj.id) + "'>Comment </a>"
	
	postResult += """</td>
	</tr>
</table>
"""
	
	return postResult
'''
'''
def makePage():
	res = str(poster())
	
	#not sure why it doesnt work
	postList = stdStuff.objFileToList(stdStuff.directory, stdStuff.postFile)
	#print len(postList)
	for post in postList:
		res += displayPost(post, "h1", "p", "h6")
	
	return res
'''
def makePage(cookie):
	res = str(poster())
	
	userList = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)
	
	for x in userList:
		if x.name == cookie["username"].value:
			for post in x.posts:
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
	
				res += """<a href='postExpanded.py?expandButton=""" + \
	str(post.id) + "'>Comment </a>"
	
				res += """</td>
	</tr>
</table>
"""
			break
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
			body += """<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="logOut" type="submit" value="Log out">
</form>
"""
			if "postTitle" in form:
				writePost(c, form)
			
			if "downVote" in form or "upVote" in form:
				targId = int(form.getvalue("postId"))
				targName = c["username"].value
				
				userDict = stdStuff.objFileToList(stdStuff.directory,
									stdStuff.userFile, byName=True)
				'''
				for x in userList:
					if x.name == targName:
						if "downVote" in form:
							for index, value in enumerate(x.posts):
								if value.id == targId:
									x.posts[index].decreaseScore()
									break
						elif "upVote" in form:
							for index, value in enumerate(x.posts):
								if value.id == targId:
									x.posts[index].increaseScore()
									break
						stdStuff.objListToFile(userList, stdStuff.directory,
												 stdStuff.userFile)
					break
				'''
				
				if "downVote" in form:
					for index, value in enumerate(userDict[targName].posts):
						if value.id == targId:
							userDict[targName].posts[index].decreaseScore()
							break
				elif "upVote" in form:
					for index, value in enumerate(userDict[targName].posts):
						if value.id == targId:
							userDict[targName].posts[index].decreaseScore()
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
