#! /usr/bin/python
import sys,pickle

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


testInbox = stdStuff.Inbox("hello")





print "content-type: text/html\n"
print head
print body
print foot
