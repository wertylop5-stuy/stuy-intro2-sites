#!/usr/bin/python
#This file is to view an expanded file
#TODO start reading from comment file
print 'content-type: text/html'
print ''
import cgitb, cgi,sys
cgitb.enable()
sys.path.insert(0, "../modules")
import stdStuff


head = '''<!DOCTYPE html>
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

#gordons code
def poster():
	return '''<br>
<br>
<br>
<br>
<form action = "profile.py" method = "GET">
Text: <textarea name="comment" rows="10" cols="15">
</textarea>
<br>
<input type = "submit" value = "Make comment">
</form>'''

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

def writeComment(commentText):
	"""writes comment to file"""
	

def displayComments():
	commentStream = open(stdStuff.directory + stdStuff.commentFile, "r")
	commentString = commentStream.read()
	commentStream.close()
	
	#never changes
	listOfComments = tuple(commentString.split(stdStuff.postChar))
	
	


body += poster()

print head
if len(form) > 0:
	print displayPost("h1", "p", "h6")
if "comment" in form:
	writeComment(form.getvalue("comment"))
print body
print foot











