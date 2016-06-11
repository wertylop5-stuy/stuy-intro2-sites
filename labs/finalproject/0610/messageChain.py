#!/usr/bin/python
print 'content-type: text/html\n'
import Cookie,os,cgi,pickle,sys,cgitb,hashlib
cgitb.enable()

sys.path.insert(0, "../modules")
import stdStuff

head = '''<!DOCTYPE html>
<html>
<head><title>All replies</title>
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

def poster():
	return '''<form action = "inbox.py" method = "GET">
Recipient: <input name="messageTarget" type="textfield" value="Watch your casing!">
<br>
Title: <input name="messageTitle" type="textfield">
<br>
Text: <textarea name="messageBody" rows="10" cols="15">
</textarea>
<br>
<input name="sendMessage" type="submit" value="Send Message">
</form>'''



def displayMessageAndReplies(userDict, currentUser, postId):
	res = ""
	
	#stores the "from: user" and message
	messagePairings = {}
	for message in userDict[currentUser].inbox.messages:
		if message.id == postId:
			res += stdStuff.makeTag("h6", message.id)
			res += stdStuff.makeTag("h2", message.title)
			
			for reply in message.replies:
				res += stdStuff.makeTag("h6", "From: " + reply.srcUser)
				res += stdStuff.makeTag("p", reply.text)
				res += "<br>"
			
			res += '''<form action = "messageChain.py" method = "GET">
Reply: <textarea name="replyBody" rows="10" cols="15">
</textarea>
<br>
<input name="postId" type="hidden" value="''' + str(message.id) + '''">
<input name="reply" type="submit" value="Reply">
</form>'''
	
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

def makePage(c):
	res = ""
	res += displayGroupWidget(c)
	#res += poster()
	#res += "<br><br>"
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
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
<a href="profile.py">Go back to profile</a>
<a href="inbox.py">Go back to inbox</a>
"""
			body += makePage(c)
			
			if "reply" in form:
				replyId = int(form.getvalue("postId"))
				
				for message in userDict[currentUser].inbox.messages:
					if message.id == replyId:
						message.reply(
						stdStuff.deleteBrackets(form.getvalue("replyBody")),
						userDict, currentUser)
						
						stdStuff.objListToFile(userDict,
										stdStuff.directory,
										stdStuff.userFile,
										isDict=True)
						break
			
			if "postId" in form:
				postId = int(form.getvalue("postId"))
				body += displayMessageAndReplies(userDict,
										currentUser,
										postId)
			
			body += '<a href="profile.py">Go back to profile</a>'
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



