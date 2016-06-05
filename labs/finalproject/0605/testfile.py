#! /usr/bin/python
import sys,pickle,cgitb
print "content-type: text/html\n"
cgitb.enable()

sys.path.insert(0, "../modules")
import stdStuff


head = \
'''
<!DOCTYPE html>
<html>
	<head><title>Profile</title>
	</head>
	<body>
'''

body = ""
foot = \
'''
	</body>
</html>
'''


thing = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile, byName=True)

stdStuff.objListToFile(thing, stdStuff.directory, stdStuff.userFile, isDict=True)

lol = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile, byName=True)
for x in lol:
	print lol[x].password



print head
print body
print foot
