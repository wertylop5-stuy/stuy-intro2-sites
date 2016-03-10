#!/usr/bin/python
print "content-type: text/html\n"

def makeHtmlHead():
	print "<!DOCTYPE html>"
	print "<html>"
	print "    <body>"
	print '        <table border="1">'

def makeHtmlFoot():
	print "        </table>"
	print "    </body>"
	print "</html>"

def makeTableData(x):
	return "<td>" + str(x) + "</td>"


makeHtmlHead()
for x in range(1, 1001):
	print "            <tr>" + \
			makeTableData(x) + \
			makeTableData(x ** 2) + \
			"</tr>"
makeHtmlFoot()
