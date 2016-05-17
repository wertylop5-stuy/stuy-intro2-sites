#!/usr/bin/python
print "content-type: text/html\n"
import sys
import cgitb
import cgi
sys.path.insert(0, "../modules")
import htmlFuncts
import loginFuncts

cgitb.enable()

form = cgi.FieldStorage()

print htmlFuncts.startPageN("Login")

print """
<form method="GET" action="login.py">
	Username: <input name="username" type="textfield">
	<br>
	Password: <input name="pass" type="password">
	<br>
	<input name="done" type="submit" value="yay">
</form>
"""

if "done" in form:
	direct = "data/"
	data = "users.txt"
	logFile = "loggedIn.txt"
	
	loginFuncts.login(
			loginFuncts.fixEntry(form.getvalue("username")).lower(),
			loginFuncts.fixEntry(form.getvalue("pass")),
			direct,
			data,
			logFile)
	
print "<a href=mainpage.py?user=" + \
		loginFuncts.fixEntry(form.getvalue("username")).lower() + \
		"

print htmlFuncts.endPage()
