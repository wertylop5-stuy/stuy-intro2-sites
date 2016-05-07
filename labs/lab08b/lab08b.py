#!/usr/bin/python
print "content-type: text/html\n"
#TODO get dictionary working

import random

def startPage(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(2) + "<link rel='stylesheet' href='pretty.css'>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def endPage():
	return makeTabs(1) + "</body>\n</html>"

def makeTabs(num):
	result = ""
	for x in range(0, num):
		result += "    "
	return result

#I wish I didn't have to use global variables
g_distinctWords = 0
hits = []
tally = []

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
	
	print textList
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

def fancyPrint(listA, listB):
	for x in range(0, len(listA)):
		print makeTabs(3) + "<tr>"
		print makeElem(listA[x], 4)
		print makeElem(listB[x], 4)
		print makeTabs(3) + "</tr>"

def findOneTime(listA, listB):
	res = []
	for x in range(0, len(listA)):
		if listB[x] == 1:
			res.append(listA[x])
	return res

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

def lowestElem(li):
	res = 999999
	resInd = 0
	for x in range(0, len(li)):
		if li[x] < res:
			res = li[x]
			resInd = x
	return resInd

########################################## Stream stuff
randomRes = random.randint(0, 1)
fileName = ""
if randomRes:
	filename = "dante.txt"
else:
	filename = "bigmac.txt"

inStream = open(filename, "r")
bookWords = inStream.read()
inStream.close()
########################################## End Stream stuff

title = "Counting: " + filename
print startPage(title)

#set up tallied values
finalDict = TallyWords(bookWords)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sorting
keyList = []
valList = []
for x in finalDict:
	keyList.append(x)
	valList.append(finalDict[x])
print finalDict
quickSort(keyList, 0, len(keyList) - 1, valList)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Giant table
print makeTabs(4) + "<td>"
print makeTabs(5) + '<table border="1">'

for x in range(len(keyList)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + keyList[x] + "</td>"
	print makeTabs(7) + '<td>' + str(valList[x]) + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + '</table>'
print makeTabs(4) + "</td>"

###########	TEH MASTER TABLE cLOSE!!!!!1!!1!1!11! ###########
print makeTabs(3) + '</tr>'
print makeTabs(2) + '</table>'




print endPage()
