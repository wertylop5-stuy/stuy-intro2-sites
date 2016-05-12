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

print htmlFuncts.startPageN("Create an account")

print """
<form method="GET" action="createaccount.py">
	Username: <input name="username" type="textfield">
	<br>
	Password: <input name="pass" type="password">
	<br>
	Commas will be removed from passwords
	<br>
	<input name="done" type="submit" value="yay">
</form>
"""

if "done" in form:
	direct = "data/"
	data = "users.txt"
	
	## wipe data
	loginFuncts.dataWipe(direct, data)
	
	loginFuncts.addUser(direct, data, form.getvalue("username"), 
			form.getvalue("pass"))


print htmlFuncts.endPage()
