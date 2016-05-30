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
print thing

for x in thing:
	print x
	#print x.value().name



print head
print body
print foot
