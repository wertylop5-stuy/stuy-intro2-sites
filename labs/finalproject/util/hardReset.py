#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"

directory = "../data/"

filesToWipe = ["comments.txt", "loggedin.txt", "postId.txt", "posts.txt",
		"users.txt", "groups.txt", "currentGroup.txt",
		"groupsName.txt"]

for f in filesToWipe:
	with open(directory + f,'w') as wipeStream:
		wipeStream.write("")

with open(directory + "counter.txt", "w") as derp:
	derp.write("0")


print "Completed attempt<br>"
