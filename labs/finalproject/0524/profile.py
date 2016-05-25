#!/usr/bin/python
#TODO maybe begin multiple users, include \n in posts
import Cookie,os,cgi

import cgitb
cgitb.enable()

head = '''
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

import cgitb,hashlib
cgitb.enable()

directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"

form = cgi.FieldStorage()

def authenticate(u,ID,IP):
    loggedIn = open(directory + logFile,'r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == username:
            return a[1]==str(ID) and a[2]==IP
    return False

#def makePage():
#	return """<form method="GET" action="makePost.py">
#	<input name="makePost" type="submit" value="Create a post">
#	</form>
#"""

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

def writePost(cookie):
	appenedWall = open(directory + postFile, 'a')
	appenedWall.write(cookie["username"].value + \
					splitChar + \
					form.getvalue('postTitle') + \
    				splitChar + \
    				form.getvalue('textBody') + \
    				
    				splitPost)
	appenedWall.close()

def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"

#reads in posts
#later: handle comments
def displayPost(titleTag, bodyTag, userTag, commentTag=""):
	wall = open(directory + postFile, 'r')
	wallRead = wall.read()
	wall.close()
		
	ListOfPosts = (wallRead.split(splitPost))
	ListOfPosts.pop()
	
	listTemp = []
	
	#contains formatted posts
	postResult = ""
	if len(wallRead) > 0:
		for post in ListOfPosts:
			listTemp = post.split(splitChar)
			
			#0 is username, 1 is title, 2 is body
			
			postResult += makeTag(userTag, listTemp[0])
			postResult += makeTag(titleTag, listTemp[1])
			postResult += makeTag(bodyTag, listTemp[2])
			postResult += "<br>"
			
	return postResult

def makePage():
    makePage = str(poster()) + str(displayPost("h1", "p", "h6"))
    return makePage


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
            body+=makePage()
        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+= 'Go Login <a href="login.py">here</a><br>'
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go Login <a href="login.py">here</a><br>'
else:
    body+= 'You seem new<br>\n'
    body+='Go Login <a href="login.py">here</a><br>'

print 'content-type: text/html'
print ''
if len(form) > 0:
    writePost(c)
print head
print body
print foot
