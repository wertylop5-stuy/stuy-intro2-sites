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
<head>
	<title>Homepage</title>
	<link rel="stylesheet" type="text/css" href="../style/homepage.css">
</head>
<body>
   '''
body = """
<div id="homePageTitle">
	<h1>Grape Shooter</h1>
</div>
<div id="homePageButtons">
	<form method="GET" action="createaccount.py">
		<input name="new" type="submit" value="Create Account">
	</form>
		
	<form method="GET" action="login.py">
		<input name="login" type="submit" value="Login">
	</form>
</div>
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
