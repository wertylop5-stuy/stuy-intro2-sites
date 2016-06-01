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
	return '''<form action = "addFriend.py" method = "GET">
Find a user: <input name="userTarget" type="textfield" value="Watch your casing!">
<br>
<input name="search" type="submit" value="Find User">
</form>'''

def findUsers(usernameQuery, userDict):
	hits = []
	for user in userDict:
		if usernameQuery in user:
			hits.append(user)
	
	hits.sort()
	return hits

def displayUserList(usernameQuery, userDict):
	res = ""
	res += "<h2>Available users</h2>"
	res += """<form method="GET" action="addFriend.py">"""
	userList = findUsers(usernameQuery, userDict)
	for user in userList:
		res += user + "<input name='" + user + "' type='checkbox'>"
		res += "<br>"
	
	res += "<br><br><br>"
	res += "<input name='requestFriend' type='submit' value='Add selected friends'>"
	res += """</form>"""
	return res

def sendFriendRequest(form, userDict):
	res = "<p>Request sent to: "
	atLeastOne = False
	for element in form:
		if element in userDict:
			atLeastOne = True
			res += element + ", "
	res = res[:len(r) - 1]
	res += "</p>"
	if not(atLeastOne):
		res = "<h2>You didn't select anyone!</h2>"
	return res
	

def makePage():
	res = ""
	res += poster()
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
			currentUser = c["username"].value
			userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
			body += "Logged in as: " + currentUser
			body += """<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<a href="profile.py">Go back to profile</a>
"""
			if "requestFriend" in form:
				body += sendFriendRequest(form, userDict)
			
			body += makePage()
			if "search" in form:
				body += displayUserList(form.getvalue("userTarget"),
										userDict)
			body += """<br><br><a href="profile.py">Go back to profile</a>"""
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







