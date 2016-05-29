#! /usr/bin/python
import sys,pickle,cgitb

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

for x in thing:
	body += x.displayPosts()





print "content-type: text/html\n"
print head
print body
print foot
