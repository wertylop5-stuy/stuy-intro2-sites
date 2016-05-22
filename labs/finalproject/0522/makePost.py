#!/usr/bin/python
print "content-type: text/html\n"
#TODO Implement the post file writing thing

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

directory = "../data/"
postFile = "posts.txt"

htmlHead = """<!DOCTYPE html>
<html>
	<head>
		<title>Create a Post</title>
	</head>
"""
print htmlHead
htmlBody = ""
print """
	<body>
		<h1>New Post</h1>
		<form method="GET" action="makePost.py">
			Title: <input name="postTitle" type="textfield">
			<br>
			Text: <textarea name="textBody" rows="10" cols="15">
</textarea>
			<br>
			<input name="done" type="submit" value="Finish">
		</form>
"""
htmlFoot = """
	</body>
</html>
"""
print htmlFoot

if "done" in form:
	postStream = open(directory + postFile, "w")
	postTitle = form.getvalue("postTitle")
	postBody = form.getvalue("textBody")
	
	
	postStream.close()
	print "success"
