#! /usr/bin/python
print "content-type: text/html\n"

class Thing:
	counter = 0

print Thing.counter
Thing.counter += 1
print Thing.counter
