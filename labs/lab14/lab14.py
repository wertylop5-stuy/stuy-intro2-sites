#!/usr/bin/python
print "content-type: text/html\n"
import sys
sys.path.insert(0, "../modules")
import htmlFuncts
from htmlFuncts import *
import dataToTable
import sortAlg

g_distinctWords = 0

def TallyWords(text):
	global g_distinctWords
	#Converted form
	textList = []
	
	#special case for dante: remove double dashes
	text = " ".join(text.split("--"))
	
	#remove whitespace
	textList = text.split()
	
	#stores useless punctuation, need extra test for apostrophe
	punct = ["!", "?", ":", ";", "/", ",", ".", \
	'"', "(", ")", "-", "[", "]", "<", ">"]
	punctStr = '''!?:;/,."'()-[]<>@#$%^&*'''
	
	#so stuff isn't too long
	q = ""
	#(smartly) removes punctuation
	for x in range(0, len(textList)):
		q = textList[x]
		
		if len(q) > 0:
			q = q.strip(punctStr)
			#prelim check for special case of ' after a "s"
			if len(q) > 2:
				if q[len(q) - 2] == "s" and q[len(q) - 1] == "'":
					q += "!"
					q = q.strip("'").strip("!")
				#else:
			#q = q.strip("'")
			textList[x] = q
	
	for x in range(len(textList)):
		textList[x] = textList[x].lower()
	
	#Stores index of existing word in hits
	tempIndex = 0
	
	#now with dictionaries!!1!1!
	tallies = {}
	
	for x in textList:
		if len(x) > 0:
			if not(x in tallies.keys()):
				tallies[x] = 1
				
				g_distinctWords += 1
			else:
				tallies[x] += 1
	return tallies

#go through a
#if x not in b, then put into b with value 0
def fillMissing(a, b):
	for x in a.keys():
		if not(x in b.keys()):
			b[x] = 0


########################################## Stream stuff
filename = "hamlet.txt"
fileStream = open("res/" + filename, "r")
fileText = fileStream.read()
fileStream.close()

filename2 = "othello.txt"
fileStream2 = open("res/" + filename2, "r")
fileText2 = fileStream2.read()
fileStream2.close()
########################################## End Stream stuff
tally = TallyWords(fileText)
tally2 = TallyWords(fileText2)

fillMissing(tally, tally2)
fillMissing(tally2, tally)

print htmlFuncts.startPage("Pair")

################### TABLE START ###################
print "<table>"
print "<tr>"

#### First one
keyList = []
valList = []
for x in tally:
	keyList.append(x)
	'''valList.append(tally[x])'''
keyList.sort()
for x in keyList:
	valList.append(tally[x])


print "one"
print "<td>"
print makeTabs(5) + '<table border="1">'
for x in range(len(keyList)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList[x]) + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + '</table>'
print "</td>"


#### Second one
keyList2 = []
valList2 = []
for x in tally2:
	keyList2.append(x)
	'''valList2.append(tally2[x])'''

keyList2.sort()
for x in keyList2:
	valList2.append(tally2[x])

print "two"
print "<td>"
print makeTabs(5) + '<table border="1">'
for x in range(len(keyList2)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList2[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList2[x]) + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + '</table>'
print "</td>"









print "</tr>"
print "</table>"
print htmlFuncts.endPage()



















