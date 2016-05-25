#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb, cgi
cgitb.enable()

#This file is to view an expanded file
form = cgi.FieldStorage()
