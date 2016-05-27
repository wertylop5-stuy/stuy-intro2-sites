#!/usr/bin/python
#This file is to view an expanded file
#TODO start reading from comment file

print 'content-type: text/html'
print ''
import cgitb,cgi,sys,os,Cookie
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff

head = '''<!DOCTYPE html>
<html>
<head><title>Login page</title>
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
<form action = "profile.py" method = "GET">
Text: <textarea name="comment" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" value = "Make comment">
</form>'''

def displayPost(postObj, titleTag, bodyTag, userTag, commentTag):
	postResult = ""
	postResult += 	stdStuff.makeTag(userTag, postObj.id) + \
					stdStuff.makeTag(userTag, postObj.user) + \
					stdStuff.makeTag(titleTag, postObj.title) + \
					stdStuff.makeTag(bodyTag, postObj.text)
	
	postResult += displayComments(postObj.comments, userTag, commentTag)
	
	postResult += '''<br>
<br>
<br>
<br>
<form action = "postExpanded.py" method = "GET">
Text: <textarea name="comment" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" name="done" value = "done">
</form>'''
	
	return postResult

def displayComments(commentList, userTag, bodyTag):
	res = ""
	for comment in commentList:
		res += 	stdStuff.makeTag(userTag, comment.user) + \
				stdStuff.makeTag(bodyTag, comment.text)
	return res

def writeComment(commentText, cookie, targId):
	allPosts = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.postFile)
	for index, value in enumerate(allPosts):
		if value.id == targId:
			allPosts[index].addComment(cookie['username'].value,
										commentText)
	commentWStream = open(stdStuff.directory + stdStuff.postFile, "w")
	for x in allPosts:
		pickle.dump(x, commentWStream)
	commentWStream.close()

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
			allPosts = stdStuff.objFileToList(stdStuff.directory,
										 stdStuff.postFile)
			
			if "expandButton" in form:
				temp = int(form.getvalue("expandButton"))
				lol = open(stdStuff.directory + stdStuff.postIdFile, "w")
				lol.write(str(temp))
				lol.close()
			
			lol = open(stdStuff.directory + stdStuff.postIdFile, "r")
			targId = int(lol.read())
			lol.close()
			
			
			if "done" in form:
				writeComment(form.getvalue("comment"), c, targId)
			
			for x in allPosts:
				if x.id == targId:
					body += displayPost(x, "h1", "p", "h3", "h6")
					break

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











