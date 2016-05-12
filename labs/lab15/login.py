#!/usr/bin/python
print "content-type: text/html\n"
import sys
import cgitb
import cgi
sys.path.insert(0, "../modules")
import htmlFuncts

cgitb.enable()

print htmlFuncts.startPageN("Login")



print htmlFuncts.endPage()
