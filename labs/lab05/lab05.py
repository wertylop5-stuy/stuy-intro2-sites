#!/usr/bin/python
print "content-type: text/html\n"

###   SETUP STUFF   ###
def startPage(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def endPage():
	return makeTabs(1) + "</body>\n</html>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def makeTabs(num):
	result = ""
	for x in range(0, num):
		result += "    "
	return result

def makeRow(numCols, startVal):
	result = "<tr>"
	for x in range(startVal, numCols + startVal):
		result += "<td>" + str(x) + "</td>"
	return result + "</tr>"

def makeTable(rows, cols, startNum):
	result = "<table>"
	for x in range(0, rows):
		result += "\n"
		result += makeRow(cols, startNum + (x * cols))
	return result + "\n</table>"

###  MODIFIED VERSIONS WITH TABS   ###
def makeRowTabs(numCols, startVal, startTab):
	result = makeTabs(startTab) + "<tr>\n"
	for x in range(startVal, numCols + startVal):
		result += makeTabs(startTab + 1) + "<td>" + str(x) + "</td>\n"
	return result + makeTabs(startTab) + "</tr>"

def makeTableTabs(rows, cols, startNum, startTab):
	result = makeTabs(startTab) + "<table>"
	for x in range(0, rows):
		result += "\n"
		result += makeRowTabs(cols, startNum + (x * cols), startTab + 1)
	return result + "\n" + makeTabs(startTab) + "</table>"

print startPage("ASCII")
print makeTableTabs(14, 16, 32, 2)
print endPage()

