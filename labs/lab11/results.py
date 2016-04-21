#!/usr/bin/python
print "content-type: text/html\n"
import sys
sys.path.insert(0, "../modules")
from htmlFuncts import *

import cgitb
cgitb.enable()

import cgi

form = cgi.FieldStorage()
#print form

print startPage("Results")

if "oneLiner" in form:
	print makeTabs(2) + "<p>" + "Hey " + \
	form.getvalue("oneLiner").capitalize() + \
	"</p>"
else:
	print "Please fill out the hey field"
	sys.exit(0)

if "clicky" in form and "clicky2" in form:
	print "clickies~!!!!!<br>"
elif "clicky" in form or "clicky2" in form:
	print "Only one clicky<br>"
else:
	print "Y U no like clickies?<br>"

if "grade" in form:
	print "you are in grade " + form.getvalue("grade") +\
	"<br>"
if form.getvalue("grade") == "9":
	print "freshie ;)" + "<br>"

if "dude" in form:
	print "That's so " + form.getvalue("dude")
else:
	print "Indicate if Fresh or rad?<br>"
	sys.exit(0)

if "essay" in form:
	print "you like writing huh?<br>"

if "val1" in form and "val2" in form:
	print "first: " + form.getvalue("val1")
	print "second: " + form.getvalue("val2")
	print "sum: " + str(int(form.getvalue("val1")) + int(form.getvalue("val2")))
	
	if "root" in form:
		print "root of first: " + str( sqrt( float( form.getvalue("val1"))))
		print "root of second: " + str( sqrt( float( form.getvalue("val2"))))


print endPage()

