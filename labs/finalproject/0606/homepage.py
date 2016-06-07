#!/usr/bin/python
print 'content-type: text/html'
print ''

import cgitb,cgi,sys,os,Cookie,pickle
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff

form = cgi.FieldStorage()

head = '''<!DOCTYPE html>
<html>
<head><title>Homepage</title>
</head>
<body>
   '''
body = """<form method="GET" action="createaccount.py">
			<input name="new" type="submit" value="Create Account">
		</form>
		
		<form method="GET" action="login.py">
			<input name="login" type="submit" value="Login">
		</form>
"""
foot = '''
</body>
</html>
'''

if "logOut" in form:
	logStream = open(stdStuff.directory + stdStuff.logFile, "w")
	logStream.write("")
	logStream.close()


print head
print body
print foot
