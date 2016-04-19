#!/usr/bin/python
print "content-type: text/html\n"
import sys
sys.path.insert(0, "../modules")

import htmlFuncts
from htmlFuncts import makeTabs

def makeList(s):
	ans = s.split("\n")
	temp = []
	for x in range(len(ans) - 1):
		temp = ans.pop(0).split(",")
		ans.append(temp)
	fixCommas(ans)
	return ans[1:]

def makeTableBody(L):
	res = ""
	for x in L:
		res += "<tr>"
		for y in x:
			res += "<td>" + str(y) + "</td>"
		res += "</tr>\n"
	return res.strip()

#Mr. K's function
#take a list of lists of strings join
#any inner commas between quotes.
def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
            res = ''
            #if you see an open double quote pop and 
            #concatenate them until you see a close quote.
            if inner[i][0]=='"':
                while inner[i][-1] != '"' and i<len(inner):
                    res += inner[i]+","
                    inner.pop(i)
                #when you find the close quote,
                #replace it with the completed string.
                inner[i]=(res+inner[i]).strip('"')
            i+=1

def appendTotal(data):
	tempThingy = False
	for mini in data:
		if not tempThingy:
			tempThingy = True
			mini.append("Total avg. score")
			continue
		if mini[3].isdigit() and mini[4].isdigit() \
		and mini[5].isdigit:
			mini.append( str( int(mini[3]) + int(mini[4]) + int(mini[5])))

def findStudentTotal(data):
	count = 0
	tempThingy = False
	for mini in data:
		if not tempThingy:
			tempThingy = True
			continue
		if mini[2].isdigit():
			count += int(mini[2])
	return count
		

################## BEGIN HTML STUFF ##################
dataStream = open("SAT.csv", "r")
text = dataStream.read()
dataStream.close()

satData = makeList(text)
appendTotal(satData)

print makeTabs(2) + "<h1>" + "Total students: " + \
str( findStudentTotal(satData[:5])) + "</h1>"

print htmlFuncts.startPage("SAT things")


print makeTabs(2) + "<table>"

#satData holds the table of tables
print makeTableBody(satData[:5])

print "</table>"






print htmlFuncts.endPage()




