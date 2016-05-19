#!/usr/bin/python
print "content-type: text/html\n"
import sys
import cgitb
import cgi
sys.path.insert(0, "../modules")
import htmlFuncts
import loginFuncts
import os

cgitb.enable()

form = cgi.FieldStorage()

print htmlFuncts.startPageN("Main")

direct = "data/"
logFile = "loggedIn.txt"
dataList = loginFuncts.getFileData(direct, logFile)
ip = os.environ["REMOTE_ADDR"]

for x in dataList:
	if form.getvalue("user") == x[0] and \
		form.getvalue("id") == x[1] and \
		ip == x[2]:
		print "logged in"
	else:
		print "<a href='login.py'>Go log in</a>"

print htmlFuncts.endPage()
