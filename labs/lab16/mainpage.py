#!/usr/bin/python
print "content-type: text/html\n"
import sys
import cgitb
import cgi
sys.path.insert(0, "../modules")
import htmlFuncts
import loginFuncts

cgitb.enable()

form = cgi.FieldStorage()

print htmlFuncts.startPageN("Main")

print 

print htmlFuncts.endPage()
