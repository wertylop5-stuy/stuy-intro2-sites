#!/usr/bin/python
#This file is to view an expanded file
#TODO start reading from comment file
print 'content-type: text/html'
print ''
import cgitb, cgi,sys
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff


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


def displayPost(titleTag, bodyTag, userTag, commentTag=""):
	postStream = open(stdStuff.directory + stdStuff.postFile, "r")
	allPosts = postStream.read()
	postStream.close()

	listOfPosts = allPosts.split(stdStuff.splitPost)
	listOfPosts.pop()
	
	postResult = ""
	if len(allPosts) > 0:
			for post in listOfPosts:
				listTemp = post.split(stdStuff.splitChar)
				
				if not(postID == listTemp[0]):
					continue
				postResult += stdStuff.makeTag(userTag, listTemp[0])
				postResult += stdStuff.makeTag(userTag, listTemp[1])
				postResult += stdStuff.makeTag(titleTag, listTemp[2])
				postResult += stdStuff.makeTag(bodyTag, listTemp[3])
				
				return postResult

if len(form) > 0:
	print displayPost("h1", "p", "h6")
print head
print body
print foot











