#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"
directory = "data/"
f = open(directory+"users.txt",'w')
f.close()
f = open(directory+"loggedin.txt",'w')
f.close()
print "Completed attempt<br>"
