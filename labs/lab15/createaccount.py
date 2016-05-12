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


#pass in directory name and file name
def getUsersFromFile(directory, fileN):
	temp = open(directory + fileN, "r")
	s = temp.read()
	temp.close()
	
	strippedData = s.split("\n")
	#removes the rest of the string after comma
	for index, value in enumerate(strippedData):
		strippedData[index] = value[:value.find(",")]
	strippedData.pop()
	return strippedData

#split form by comma
#if newline in element, pop it
#if username in resulting list, ignore
#else, add it
def addUser(directory, fileN, user, passW):
	stream = None
	userList = getUsersFromFile(directory, fileN)
	if not(user in userList):
		stream = open(directory + fileN, "a")
		stream.write(user + "," +passW + "\n")
		stream.close()


if "done" in form:
	direct = "data/"
	data = "usernames.txt"
	
	addUser(direct, data, form.getvalue("username"), 
			form.getvalue("pass"))
	
	## wipe data
	#dataWipe(direct, data)
	
	
	
	
	


print htmlFuncts.endPage()






















