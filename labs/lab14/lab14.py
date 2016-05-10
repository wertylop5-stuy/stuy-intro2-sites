#!/usr/bin/python
print "content-type: text/html\n"
#TODO fix negatives

import sys
sys.path.insert(0, "../modules")
import htmlFuncts
from htmlFuncts import *
import dataToTable
import sortAlg

g_distinctWords = 0
g_totWords = 0

def TallyWords(text):
	global g_distinctWords
	global g_totWords
	g_totWords = 0
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
			g_totWords += 1
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

#list of lists
#format: [["word", 5], ["two", 0]]
#dictOne is required

#one arg returns that as a list of lists
#two arg returns words, but numbers are subtracted
def dictToList(	dictOne, 
				totalCount, 
				dictOneName = "",
				totalCount2 = 0,
				dictTwo = None,
				dictTwoName = ""):
	res = []
	temp = []
	keyStore = []
	keyStore = dictOne.keys()
	keyStore.sort()
	
	#fun stuff, only 2 columns
	#first column is higher book name instead of word
	#second is difference in percentage
	if dictTwo:
		for x in keyStore:
			if dictOne[x] > dictTwo[x]:
				temp.append(dictOneName)
				temp.append(
							str(
							round(
							(((dictOne[x] / float(totalCount)) * 100) -
							((dictTwo[x] / float(totalCount2)) * 100)),
							4)
							) + "%"
							)
			else:
				temp.append(dictTwoName)
				temp.append(
							str(
							round(
							(((dictTwo[x] / float(totalCount2)) * 100) 
							-
							(dictOne[x] / float(totalCount)) * 100),
							4)
							) + "%"
							)
			res.append(temp)
			temp = []
	else:
		for x in keyStore:
			temp.append(x)
			temp.append(dictOne[x])
			temp.append(
						str(
						round(
						((dictOne[x] / float(totalCount)) * 100),
						4)
						) +"%"
						)
			
			res.append(temp)
			temp = []
	return res


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
count = g_totWords
tally2 = TallyWords(fileText2)
count2 = g_totWords

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

keyList.sort()
for x in keyList:
	valList.append(tally[x])


print "<td>"
print "hamlet"
print makeTabs(5) + '<table border="1">'
'''
for x in range(len(keyList)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList[x]) + "</td>"
	print makeTabs(6) + '</tr>'
'''
print count
print dataToTable.makeTableBody(dictToList(tally, count))

print makeTabs(5) + '</table>'
print "</td>"


#### Second one
keyList2 = []
valList2 = []
for x in tally2:
	keyList2.append(x)

keyList2.sort()
for x in keyList2:
	valList2.append(tally2[x])

print "<td>"
print "othello"
print makeTabs(5) + '<table border="1">'
'''
for x in range(len(keyList2)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList2[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList2[x]) + "</td>"
	print makeTabs(6) + '</tr>'
'''
print count2
print dataToTable.makeTableBody(dictToList(tally2, count2))

print makeTabs(5) + '</table>'
print "</td>"



print "<td>"
print "both"
print makeTabs(5) + '<table border="1">'

print dataToTable.makeTableBody(dictToList(tally, count, 
								"hamlet",
								count2,
								tally2,
								"othello"))

print makeTabs(5) + '</table>'
print "</td>"








print "</tr>"
print "</table>"
print htmlFuncts.endPage()



















