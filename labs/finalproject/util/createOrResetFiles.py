#!/usr/bin/python
print 'content-type: text/html'
print ''
import cgitb
cgitb.enable()
print "Attempt to write file<br>"

directory = "../data/"
fileN = "counter.txt"

f = open(directory + fileN,'w')
#f.write("0")
f.close()

print "Completed attempt<br>"
