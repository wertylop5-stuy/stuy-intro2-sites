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

def searchByName(L, name, searchCol):
	res = []
	lel = False
	for inner in L:
		#handles the header portion of the list
		if not lel:
			lel = True
			res.append(inner)
			continue
		if name.lower() in inner[searchCol].lower():
			res.append(inner)
	return res


print htmlFuncts.startPage("Searching :)")

form = cgi.FieldStorage()

#this will intially start up, since
#nothing has been queried yet
if len(form) == 0:
	print "<h1>file search</h1>"
	
	#the actual form
	print """
<form method="GET" action="lab12.py">
<br>
Search term: <input name="qString" type="textfield">
<h3>Find by:</h3>
name: <input name="findByName" type="checkbox">
<br>
First name: <input name="searchType" type="radio" value="first">
<br>
Last name: <input name="searchType" type="radio" value="last">
<br>
Email: <input name="searchType" type="radio" value="email">
<br>
<br>
<br>
state: <input name="findByState" type="checkbox">
<br>
<select name="qState" size="1">
	<option>Alabama</option>
	<option>Alaska</option>
	<option>Arizona</option>
	<option>Arkansas</option>
	<option>California</option>
	<option>Colorado</option>
	<option>Connecticut</option>
	<option>Delaware</option>
	<option>Florida</option>
	<option>Georgia</option>
	<option>Hawaii</option>
	<option>Idaho</option>
	<option>Illinois</option>
	<option>Indiana</option>
	<option>Iowa</option>
	<option>Kansas</option>
	<option>Kentucky</option>
	<option>Louisiana</option>
	<option>Maine</option>
	<option>Maryland</option>
	<option>Massachusetts</option>
	<option>Michigan</option>
	<option>Minnesota</option>
	<option>Mississippi</option>
	<option>Missouri</option>
	<option>Montana</option>
	<option>Nebraska</option>
	<option>Nevada</option>
	<option>New Hampshire</option>
	<option>New Jersey</option>
	<option>New Mexico</option>
	<option>New York</option>
	<option>North Carolina</option>
	<option>North Dakota</option>
	<option>Ohio</option>
	<option>Oklahoma</option>
	<option>Oregon</option>
	<option>Pennsylvania</option>
	<option>Rhode Island</option>
	<option>South Carolina</option>
	<option>South Dakota</option>
	<option>Tennessee</option>
	<option>Texas</option>
	<option>Utah</option>
	<option>Vermont</option>
	<option>Virginia</option>
	<option>Washington</option>
	<option>West Virginia</option>
	<option>Wisconsin</option>
	<option>Wyoming</option>
	<option>District of Columbia</option>
</select>
<br>
<input name="search" type="submit" value="go">
</form>
"""
#search has been queried
else:
	#begin open file
	tableStream = open("MOCK_DATA.csv", "r")
	tableString = tableStream.read()
	tableStream.close()
	#end open file
	
	dataTable = dataToTable.makeList(tableString)
	
	#the result table
	finalTable = dataTable
	
	#it should also include state search
	if "findByName" in form:
		if form.getvalue("searchType") == "first":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 1)
		elif form.getvalue("searchType") == "last":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 2)
		elif form.getvalue("searchType") == "email":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 3)
	if "findByState" in form:
		finalTable = searchByName(finalTable, form.getvalue("qString"), 4)
	
	
	print "<table>\n" + dataToTable.makeTableBody(finalTable) + \
	"</table>"

print htmlFuncts.endPage()










