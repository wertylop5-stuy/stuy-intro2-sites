#! /usr/bin/python
import sys,pickle,cgitb,cgi,os,Cookie
print "content-type: text/html\n"
cgitb.enable()
form = cgi.FieldStorage()

sys.path.insert(0, "../modules")
import stdStuff

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


head = \
'''
<!DOCTYPE html>
<html>
	<head><title>Search</title>
	</head>
	<body>
	<form method="GET" action="homepage.py">
<input name="logOut" type="submit" value="Log out">
</form>
<form method="GET" action="addFriend.py">
<input name="addFriend" type="submit" value="Add a friend">
</form>
	<a href = "profile.py">Back to Profile </a>
	<br>
	<form>
		Search for people: <input type = "text" name = "user">
		<input type = "submit" value = "Commence Search">
	</form>
'''

body = ''

foot = '''</body>
<html>'''

print head


if len(form) > 0:
	
	searchUser = form.getvalue('user')
	found = False
	userList = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)
	'''for x in userList:
		if x.name == c["username"].value:
			user = x'''
	print "<h1>Searched Name: " + searchUser + "</h1>"
	#print userList

	
	for x in userList:
		if x.name == searchUser:
			body += x.displayPosts()
			found = True
	if found:
		#Add Friend option
		print '''<a href = 'search.py?user=''' + searchUser + '''&add=friend'>Add Friend</a>'''    

	if 'add' in form:
		#Later repalce with send friend request
		if searchUser == c['username'].value:
			print 'You cannot be friends with yourself ;=;<br>'
		elif not(searchUser in user.friends):
		       user.addFriend(searchUser)
		       print 'Added friend<br>'
		elif searchUser in user.friends:
			print "Friend is already in friend list<br>"

	if len(body) == 0 and found:
		print "User has not posted anything yet!"
	elif len(body) == 0:
		print "User is not found."
	
	
print body
print foot
