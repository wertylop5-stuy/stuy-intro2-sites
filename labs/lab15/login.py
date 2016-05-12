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
<form method="GET" action="createaccount.py">
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
	
	loginFuncts.validateEntry(
				form.getvalue("username"),
				loginFuncts.fixPassword(form.getvalue("pass")),
				direct,
				data)

print htmlFuncts.endPage()
