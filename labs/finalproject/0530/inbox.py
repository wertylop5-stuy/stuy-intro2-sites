#!/usr/bin/python
print 'content-type: text/html\n'
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

#gordons code
def poster():
	return '''<form action = "inbox.py" method = "GET">
Recipient: <input name="messageTarget" type="textfield" value="Watch your casing!">
<br>
Title: <input name="messageTitle" type="textfield">
<br>
Text: <textarea name="messageBody" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" value = "Send Message">
</form>'''

def displayMessages(cookie):
	res = ""
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	res += userDict[currentUser].inbox.listMessages()
	return res



def makePage(cookie):
	res = ""
	res += poster()
	res += displayMessages(cookie)
	
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
<input name="addFriend" type="submit" value="Add a friend">
</form>
"""
			
			
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




