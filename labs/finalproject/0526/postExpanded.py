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

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    ##print all the data in the cookie
    #body+= "<h1>cookie data</h1>"
    #for each in c:
    #    body += each+":"+str(c[each].value)+"<br>"


    
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']
        
        if authenticate(username,ID,IP):
            body+=makePage()
        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+= 'Go Login <a href="login.py">here</a><br>'
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go Login <a href="login.py">here</a><br>'
else:
    body+= 'You seem new<br>\n'
    body+='Go Login <a href="login.py">here</a><br>'

















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

def getIndexOfID(L, idNum):
	'''get the index in a list '''

def writeComment(commentText, c):
	"""writes comment to file"""
	commentStream = open(stdStuff.directory + stdStuff.commentFile, "r")
	commentString = commentStream.read()
	commentStream.close()
	
	listOfComments = commentString.split(stdStuff.postChar)
	for index, value in enumerate(listOfComments):
		g[index] = value.split(".")
		while "" in g[index]:
			g[index].remove("")

	
	

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
	writeComment(form.getvalue("comment"), c)
print body
print foot











