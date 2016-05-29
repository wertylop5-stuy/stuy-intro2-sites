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


thing = stdStuff.objFileToList(stdStuff.directory, stdStuff.userFile)

for user in thing:
	print "g"
	print user.name
	body += user.displayPosts()





print head
print body
print foot
