#!/usr/bin/python
#Add authenication 
print 'content-type: text/html\n'
import Cookie,os,cgi,pickle,sys,cgitb,hashlib

cgitb.enable()
form = cgi.FieldStorage()

sys.path.insert(0, "../modules")
import stdStuff

directory = '../data/'

head = '''<!DOCTYPE html>
<html>
<head>
<title>Groups</title>
<link rel="stylesheet" type="text/css" href="../style/groups.css">
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''


def authenticate(u,ID,IP):
	loggedIn = open(stdStuff.directory + stdStuff.logFile,'r').read().split('\n')
	loggedIn = [each.split(',') for each in loggedIn]
	loggedIn.remove([''])
	for a in loggedIn:
		if a[0] == username:
			return a[1]==str(ID) and a[2]==IP
	return False

def displayGroup():
    availableGroups = ''
    groupList = stdStuff.objFileToList(stdStuff.directory, stdStuff.groupFile)
    for name in groupList:
        if (name.visibility == 'public') or (currentUser in name.members):
            availableGroups += '<option>' + str(name.name) + '</option>'
    return availableGroups

def displayInboxWidget(cookie):
	currentUser = cookie["username"].value
	userDict = stdStuff.objFileToList(stdStuff.directory,
								stdStuff.userFile, byName=True)
	
	res = \
"""
<div class="widget" id="inboxWidget">
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

groupStatus = ""
availableGroups = ""
displayGroups = ""

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
		currentUser = c['username'].value
		if authenticate(username,ID,IP):
			### PUT PAGE STUFF HERE
			body += "<div id='userHeader'>"
			body += """
<div id="username">
	<p>Logged in as: """ + \
username + \
"""</p>
</div>"""
			body += """
<div id="userButtons">
	<form method="GET" action="homepage.py">
		<input name="logOut" type="submit" value="Log out">
	</form>
	<form method="GET" action="addFriend.py">
		<input name="addFriend" type="submit" value="Add a friend">
	</form>
	<a href="profile.py">Go back to profile</a>
</div>
</div>
"""
			#for the fixed post
			body += "<div id='userHeader2'></div>"
			
			body += displayInboxWidget(c)
			currentUser = c['username'].value
			
			userDict = stdStuff.objFileToList(stdStuff.directory,
											stdStuff.userFile, byName=True)
			groupDict = stdStuff.objFileToList(stdStuff.directory,
											stdStuff.groupFile, byName=True)
			
			groupList = stdStuff.objFileToList(stdStuff.directory,
												stdStuff.groupFile)
			
			f = open(directory +  stdStuff.currentGroupFile, 'r')
			currentGroup = f.read()
			f.close()

			f = open(directory +  stdStuff.groupsNameFile, 'r')
			groupsName = f.read()
			f.close()
			
			
			#Replace with drop down menu. Kick Meber = 
			#Drop down with memebrs in group only.
			
			#Add member = maybe drop down with public/anyone not in group
			

			createGroup = '''
<div class="group">
<h1>Want To Create A Group?</h1><form method = "GET" action = "groups.py">
			Group Name:<input type = "text" name = "groupName">
			<br>Visibility:
			<select name = "visibility">
					<option>public</option>
					<option>private</option>
			</select>
			<input type = "submit" name = "createGroup" value = "Create Group!">
			</form> 
</div>
			'''
			body += createGroup


			#print displayGroup()
			groupStatus = ''
			if 'createGroup' in form:
				groupName = stdStuff.deleteBrackets(
							form.getvalue('groupName'))
				visibility = form.getvalue('visibility')
				if groupName in groupDict.keys():
					    groupStatus += '<br><p>Group cannot be created. This group name has already been taken.</p>'
				else:
					if groupName == None:
						pass
					else:
						with open(directory + 'groups.txt', "ab") \
						as groupStorage:
							pickle.dump(
									stdStuff.Group(
										groupName,
										visibility,
										currentUser),
									groupStorage)
						
						with open(directory + 'groupsName.txt', "ab") \
						as groupNameList:
							groupNameList.write(groupName)
							
						groupStatus += '<br><p>Group has been made</p>'
				            
						#if "visibility" in form:
						groupList = stdStuff.objFileToList(
									stdStuff.directory,
									stdStuff.groupFile)
						for x in groupList:
							if x == groupName:
								x.changeVisibility(
									str(form.getvalue("visibility")))
			
			
			groupList = stdStuff.objFileToList(stdStuff.directory,
												stdStuff.groupFile)
			
			
			displayGroups += '''
<div class="group">
<br><h1>Want To View Groups?</h1>
Groups:
<form method = "GET" action = "groupsPage.py">
<select name = "displayGroups">''' + displayGroup() + \
'''</select>\n\t''' + \
'''<input type = "submit" name = "groupPicked" value = "View Group">
</form>
</div>'''
			
			if len(groupList) > 0:
					body += displayGroups
			#availableGroups = displayGroup()
			
			#body += displayGroups
			
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
print groupStatus
print foot
