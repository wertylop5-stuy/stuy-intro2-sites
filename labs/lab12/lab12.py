#!/usr/bin/python
print "content-type: text/html\n"
import cgi
import sys
sys.path.insert(0, "../modules")
#from modules
import htmlFuncts
import dataToTable

import cgitb
cgitb.enable()

print htmlFuncts.startPage("Searching :)")

form = cgi.FieldStorage()

#this will intially start up, since
#nothing has been queried yet
if len(form) == 0:
	print "<h1>file search</h1>"
	
	#the actual form
	print """
<form method="GET" action="lab12.py">
Find by name: <input name="findByName" type="checkbox">
<br>
Search term: <input name="qString" type="textfield">
<br>
<h3>Find by:</h3>
First name: <input name="searchType" type="radio" value="first">
<br>
Last name: <input name="searchType" type="radio" value="last">
<br>
Email: <input name="searchType" type="radio" value="email">
<br>
<input name="search" type="submit" value="go">
</form>
"""
#search has been queried
else:
	#begin open file
	tableStream = open("MOCK_DATA.csv", "r")
	tableString = tableStream.read().strip(",")
	tableStream.close()
	#end open file
	
	#print tableString
	dataTable = dataToTable.makeList(tableString)
	#print dataTable
	#print form
	
	if "findByName" in form:
		
	else:
		
	





print htmlFuncts.endPage()










