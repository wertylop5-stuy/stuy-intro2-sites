#!/usr/bin/python
#TODO 
print "content-type: text/html\n"
import cgi
import sys
import math

sys.path.insert(0, "../modules")
#user defined
import htmlFuncts
import dataToTable

import cgitb
cgitb.enable()

def searchByName(L, name, searchCol):
	res = []
	#lel = False
	for inner in L:
		#handles the header portion of the list
		'''if not lel:
			lel = True
			res.append(inner)
			continue'''
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
<form method="GET" action="lab13.py">
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
	cgiParts = "&"
	#begin open file
	tableStream = open("MOCK_DATA.csv", "r")
	tableString = tableStream.read()
	tableStream.close()
	#end open file
	
	dataTable = dataToTable.makeList(tableString)
	header = []
	header.insert(0, dataTable.pop(0))
	
	#the result table
	finalTable = dataTable
	
	#search by name
	if "findByName" in form and not(form.getvalue("qString") is None):
		cgiParts += \
		"findByName=on" + "&" + \
		"qString=" + form.getvalue("qString") + "&" + \
		"searchType=" + form.getvalue("searchType") + "&"
		
		if form.getvalue("searchType") == "first":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 1)
		elif form.getvalue("searchType") == "last":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 2)
		elif form.getvalue("searchType") == "email":
			finalTable = searchByName(finalTable, form.getvalue("qString"), 3)
	
	#search by state
	if "findByState" in form:
		cgiParts += \
		"findByState=on" + "&" + \
		"qState=" + form.getvalue("qState") + "&"
		finalTable = searchByName(finalTable, form.getvalue("qState"), 4)
	
	#displays only certain amount of elements
	page = 0
	if "page" in form:
		page = int(form.getvalue("page"))
	resPerPage = 10
	if "resPerPage" in form:
		resPerPage = int(form.getvalue("resPerPage"))
	
	#save space
	tableStart = resPerPage * page
	
	#result table
	print "<table>\n" + \
	dataToTable.makeTableHeader(header) + \
	dataToTable.makeTableBody(
	finalTable[tableStart:tableStart + resPerPage]) + \
	"</table>"
	
	#previous and next links
	
	#prev
	if page > 0:
		print "<a id='prev' href='lab13.py?page=" + str(page - 1) + \
		"&resPerPage=" + str(resPerPage) + cgiParts + "'>prev</a>"
	
	#next
	if float(len(finalTable) / resPerPage) % resPerPage == 0:
		if page + 1 < math.ceil(len(finalTable) / resPerPage):
			print "<a id='next' href='lab13.py?page=" + str(page + 1) + \
			"&resPerPage=" + str(resPerPage) + cgiParts + "'>next</a>"
	else:
		if page < math.ceil(len(finalTable) / resPerPage):
			print "<a id='next' href='lab13.py?page=" + str(page + 1) + \
			"&resPerPage=" + str(resPerPage) + cgiParts + "'>next</a>"
	

print htmlFuncts.endPage()












