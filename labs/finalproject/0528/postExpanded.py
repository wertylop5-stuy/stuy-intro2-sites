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
					res += post.displayComments()
			break
	return res
'''
def writeComment(commentText, cookie, targId):
	allPosts = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.postFile)
	for index, value in enumerate(allPosts):
		if value.id == targId:
			allPosts[index].addComment(cookie['username'].value,
										commentText)
	commentWStream = open(stdStuff.directory + stdStuff.postFile, "wb")
	for x in allPosts:
		pickle.dump(x, commentWStream)
	commentWStream.close()
'''

def writeComment(targId, cookie, commentText):
	targName = cookie["username"].value
	allUsers = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.userFile)
	counter = stdStuff.getCounter()
	
	for index, value in enumerate(allUsers):
		if value.name == targName:
			for index2, value2 in enumerate(value.posts):
				if int(value2.id) == int(targId):
					value.posts[index2].addComment(counter, targName, targId)
	stdStuff.objListToFile(stdStuff.directory, stdStuff.userFile)
	stdStuff.setCounter(counter)

def authenticate(u,ID,IP):
    loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == username:
            return a[1]==str(ID) and a[2]==IP
    return False


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











