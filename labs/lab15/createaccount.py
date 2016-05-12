#!/usr/bin/python
print "content-type: text/html\n"
import sys
import cgitb
import cgi
sys.path.insert(0, "../modules")
import htmlFuncts

cgitb.enable()

print htmlFuncts.startPageN("Create an account")

form = cgi.FieldStorage()

print """
<form method="GET" action="createaccount.py">
	Username: <input name="username" type="textfield">
	<br>
	Password: <input name="pass" type="password">
	<br>
	<input name="done" type="submit" value="yay">
</form>
"""

def dataWipe(direct, fileN):
	temp = open(direct + fileN, "w")
	temp.write("")
	temp.close()
	print "Wipe successful"

def getUsersFromFile(fileN):
	strippedData = fileN.split("\n")
	#removes the rest of the string after comma
	for index, value in enumerate(strippedData):
		strippedData[index] = value[:value.find(",")]
	strippedData.pop()
	return strippedData

#split form by comma
#if newline in element, pop it
#if username in resulting list, ignore
#else, add it
def addUser(form, directory, fileN, user, passW):
	stream = None
	userList = getUsersFromFile(form)
	if not(user in userList):
		stream = open(directory + fileN, "a")
		stream.write(
			form.getvalue("username") + "," +
			form.getvalue("pass") + "\n"
			)
		stream.close()


if "done" in form:
	direct = "data/"
	data = "usernames.txt"
	userAppendStream = open(direct + data, "a")
	#userWriteStream = open(direct + data, "w")
	userReadStream = open(direct + data, "r")
	
	#dataWipe(direct, data)
	
	usernameList = userReadStream.read()
	usernameList = usernameList.split("\n")
	
	if not(form.getvalue("username") in usernameList):
		userAppendStream.write(
			form.getvalue("username") + "," +
			form.getvalue("pass") + "\n"
			)
	
	userAppendStream.close()
	#userWriteStream.close()
	userReadStream.close()


print htmlFuncts.endPage()
