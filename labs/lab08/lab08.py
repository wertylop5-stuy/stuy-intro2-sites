#!/usr/bin/python
print "content-type: text/html\n"

import random

def startPage(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def endPage():
	return makeTabs(1) + "</body>\n</html>"

def makeTabs(num):
	result = ""
	for x in range(0, num):
		result += "    "
	return result

def makeElem(data, tabs):
	return makeTabs(tabs) + "<td>" + str(data) + "</td>"

#######################I wish I didn't have to use global variables
g_distinctWords = 0
hits = []
tally = []

def TallyWords(text):
	global g_distinctWords
	global hits
	global tally
	#Converted form
	textList = []
	
	#special case for dante: remove duoble dashes
	text = " ".join(text.split("--"))
	
	#remove whitespace
	textList = text.split()
	
	#stores useless punctuation, need extra test for apostrophe
	punct = ["!", "?", ":", ";", "/", ",", ".", '"', "(", ")", "-"]
	punctStr = '''!?:;/,."'()-'''
	
	#so stuff isn't too long
	q = ""
	#(smartly) removes punctuation
	for x in range(0, len(textList)):
		q = textList[x]
		
		if len(q) > 0:
			q = q.strip(punctStr)
			#prelim check for special case of ' after a "s"
			'''if len(q) > 2:
				if q[len(q) - 2] == "s" and q[len(q) - 1] == "'":
					q += "!"
					q = q.strip("'").strip("!")
				#else:'''
			#q = q.strip("'")
			textList[x] = q
	
	#These two correspond with each other
	#hits = []
	#tally = []
	
	#Stores index of existing word in hits
	tempIndex = 0
	
	for x in textList:
		
		if not(x.lower() in hits):
			hits.append(x.lower())
			tally.append(1)
			g_distinctWords += 1
		else:
			tempIndex = hits.index(x.lower())
			tally[tempIndex] += 1
	
	#print hits
	#fancyPrint(hits, tally)
	#return hits, tally

def fancyPrint(listA, listB):
	for x in range(0, len(listA)):
		#print listA[x], ":", listB[x]
		print makeTabs(3) + "<tr>"
		print makeElem(listA[x], 4)
		print makeElem(listB[x], 4)
		print makeTabs(3) + "</tr>"
	#print ""

def findOneTime(listA, listB):
	res = []
	for x in range(0, len(listA)):
		if listB[x] == 1:
			res.append(listA[x])
	return res

###STream stuff
randomRes = random.randint(0, 1)
fileName = ""
if randomRes:
	filename = "dante.txt"
else:
	#filename = "bigmac.txt"
	filename = "dante.txt"

inStream = open(filename, "r")
bookWords = inStream.read()
###End STream stuff

print startPage("Counting")

#set up tallied values
TallyWords(bookWords)

totalTally = 0
for x in tally:
	totalTally += x

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total words
print makeTabs(2) + "<p>" + "Total words: " + \
str( totalTally) + "</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~distinct words
print makeTabs(2) + "<p>" + "Distinct words: " + \
str(g_distinctWords) + "</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~words occurring once
oneWords = findOneTime(hits, tally)
print makeTabs(2) + "<p>" + "Words occurring once: " + \
str( len(oneWords)) + "</p>"









###########	TEH MASTER TABLE!!!!!1!!1!1!11! ###########
print makeTabs(2) + '<table>'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~first one hundred one time words
print makeTabs(3) + "<tr>"
print makeTabs(4) + "<td>"
print makeTabs(5) + '<table>'
for x in oneWords[:100]:
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + x + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + "</table>"
print makeTabs(4) + "</td>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Most common words (lolrip)
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
	
	while curPos != end:
		if li[curPos] <= pivot:
			curPos += 1
			smallBound += 1
		else:
			curPos += 1
			break
	while curPos != end:
		if li[curPos] <= pivot:
			swap(li, smallBound, curPos, hitIn)
			smallBound += 1
		curPos += 1
	
	swap(li, smallBound, end, hitIn)
	return smallBound

def quickSort(li, start, end, hitIn):
	mid = 0
	if end - start > 0:
		mid = partition(li, start, end, hitIn)
		if mid != 1:
			quickSort(li, start, mid - 1, hitIn)
			quickSort(li, mid + 1, end, hitIn)


def lowestElem(li):
	res = 999999
	resInd = 0
	for x in range(0, len(li)):
		if li[x] < res:
			res = li[x]
			resInd = x
	return resInd

#first getting only the ten highest

#my quicksort is flawed in that trying to sort tally
#all at once will result in too many recursions
highNums = []
highWords = []
tempInd = 0
for x in range(0, len(hits)):
	if len(highNums) == 10:
		tempInd = lowestElem(highNums)
		if tally[x] > highNums[tempInd]:
			highNums[tempInd] = tally[x]
			highWords[tempInd] = hits[x]
	else:
		highNums.append(tally[x])
		highWords.append(hits[x])

#print highNums

#not sure why, but need to sort twice
quickSort(highNums, 0, len(highNums) - 1, highWords)
quickSort(highNums, 0, len(highNums) - 1, highWords)
#print highNums

'''for x in range(9, -1, -1):
	print makeTabs(2) + "<p>" + str(highWords[x]) + \
	" " + str(highNums[x]) + "</p>"'''
	
print makeTabs(4) + "<td>"
print makeTabs(5) + "<table border='1'>"
for x in range(9, -1, -1):
	print makeTabs(6) + "<tr>"
	print makeTabs(7) + "<td>" + str(highWords[x]) + \
	" " + str(highNums[x]) + "</td>"
print makeTabs(5) + "</table>"
print makeTabs(4) + "</td>"



#giant table
print makeTabs(4) + "<td>"
print makeTabs(5) + '<table border="1">'

for x in range(0, len(hits)):
	print makeTabs(6) + '<tr>'
	print makeTabs(7) + '<td>' + hits[x] + "</td>"
	print makeTabs(7) + '<td>' + str(tally[x]) + "</td>"
	print makeTabs(6) + '</tr>'
print makeTabs(5) + '</table>'
print makeTabs(4) + "</td>"

###########	TEH MASTER TABLE cLOSE!!!!!1!!1!1!11! ###########
print makeTabs(3) + '</tr>'
print makeTabs(2) + '</table>'








print endPage()




