#!/usr/bin/python
print "content-type: text/html\n"
import sys
sys.path.insert(0, "../modules")
import htmlFuncts
from htmlFuncts import *
import dataToTable

g_distinctWords = 0

###################### QUICKSORT BEGIN
def swap(li, start, end, hitIn):
	temp = li[start]
	temp2 = hitIn[start]
	
	li[start] = li[end]
	hitIn[start] = hitIn[end]
	
	li[end] = temp
	hitIn[end] = temp2

def partition(li, start, end, hitIn):
	pivot = li[end]
	curPos = start
	
	#keeps track of highest index of lower vals
	smallBound = start
	
	#sets smallbound to the first number smaller than pivot
	while curPos != end:
		if li[curPos] <= pivot:
			curPos += 1
			smallBound += 1
		else:
			curPos += 1
			break
	
	#shifts larger numbers to right side
	while curPos != end:
		if li[curPos] <= pivot:
			swap(li, smallBound, curPos, hitIn)
			smallBound += 1
		curPos += 1
	
	#switch pivot with "middle" elem
	swap(li, smallBound, end, hitIn)
	return smallBound

def quickSort(li, start, end, hitIn):
	mid = 0
	if end - start > 0:
		mid = partition(li, start, end, hitIn)
		if mid != 1:
			quickSort(li, start, mid - 1, hitIn)
			quickSort(li, mid + 1, end, hitIn)
###################### QUICKSORT END

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
#print tally

filename2 = "othello.txt"
fileStream2 = open("res/" + filename2, "r")
fileText2 = fileStream2.read()
fileStream2.close()
#print tally2
########################################## End Stream stuff

'''test = {"a":1, "b":1, "c":3, "e":5}
test2 = {"a":1, "b":1, "d":3}

print test2
fillMissing(test, test2)
print test2'''
tally = TallyWords(fileText)
tally2 = TallyWords(fileText2)

fillMissing(tally, tally2)
fillMissing(tally2, tally)

#### First one
keyList = []
valList = []
for x in tally:
	keyList.append(x)
	valList.append(tally[x])

quickSort(keyList, 0, len(keyList) - 1, valList)

print makeTabs(5) + '<table border="1">'
for x in range(len(keyList)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList[x]) + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + '</table>'


#### Second one
keyList2 = []
valList2 = []
for x in tally2:
	keyList.append(x)
	valList.append(tally2[x])

quickSort(keyList, 0, len(keyList) - 1, valList)









'''
print htmlFuncts.startPage("Pair")

print htmlFuncts.endPage()
'''
