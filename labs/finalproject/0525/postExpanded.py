#!/usr/bin/python
#This file is to view an expanded file
#TODO start reading from comment file
print 'content-type: text/html'
print ''
import cgitb, cgi
cgitb.enable()

directory = "../data/"
userFile = "users.txt"
logFile = "loggedin.txt"
postFile = "posts.txt"
counterFile = "counter.txt"
commentFile = "comments.txt"

splitChar = chr(182)
splitPost = chr(208)


head = '''
<html>
<head><title>Login page</title>
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''


form = cgi.FieldStorage()

postID = form.getvalue("expandButton")


def makeTag(tag, text):
	return "<" + tag + ">" + str(text) + "</" + tag + ">"


def displayPost(titleTag, bodyTag, userTag, commentTag=""):
	postStream = open(directory + postFile, "r")
	allPosts = postStream.read()
	postStream.close()

	listOfPosts = allPosts.split(splitPost)
	listOfPosts.pop()
	print listOfPosts
	
	postResult = ""
	if len(allPosts) > 0:
			for post in listOfPosts:
				listTemp = post.split(splitChar)
				
				if not(postID == listTemp[0]):
					continue
				postResult += makeTag(userTag, listTemp[0])
				postResult += makeTag(userTag, listTemp[1])
				postResult += makeTag(titleTag, listTemp[2])
				postResult += makeTag(bodyTag, listTemp[3])
				
				return postResult

if len(form) > 0:
	print displayPost("h1", "p", "h6")
print head
print body
print foot











