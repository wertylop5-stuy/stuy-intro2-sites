#!/usr/bin/python
print "content-type: text/html\n"


#TODO DO AN INSERTION SORT OR SOMETHING
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



filename = "dante.txt"
inStream = open(filename, "r")
bookWords = inStream.read()

#print "Lots of text"
#print bookWords[:200]

'''print "List of text"
print bookWords.split()[:100]'''


print startPage("Counting Dante")

#set up tallied values
TallyWords(bookWords[170:])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total words
print makeTabs(2) + "<p>" + str( len( bookWords[27:].split())) + "</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~distinct words
print makeTabs(2) + "<p>" + str(g_distinctWords) + "</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~words occurring once
oneWords = findOneTime(hits, tally)
print makeTabs(2) + "<p>" + str( len(oneWords)) + "</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~first one hundred one time words
print makeTabs(2) + '<table>'
for x in oneWords[:100]:
	print makeTabs(3) + '<tr>'
	print makeTabs(4) + '<td>' + x + "</td>"
	print makeTabs(3) + '</tr>'
print ""
print ""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Most common words (lolrip)
'''common = []
highestNums = []
for x in range(0, len(hits)):
	if len(highestNums) == 10:
		if tally[x] 
	else:
		common.append(hits[x])
		highestNums.append(tally[x])'''

'''def swap(li, start, end, hitIn):
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
			quickSort(li, mid + 1, end, hitIn)'''

#print makeTabs(2) + '<table border="1">'
#giant table

#print makeTabs(2) + '</table>'

'''mostCommonTally = tally
mostCommonHits = hits
#quickSort(mostCommonTally, 0, len(mostCommonTally) - 1, mostCommonHits)
d = [1, 3, 9, 1, 4, 7, 8, 2, 6]
e = [1, 3, 9, 1, 4, 7, 8, 2, 6]
partition(d, 0, len(d) - 1, e)
print d, e'''

'''for x in range(0, 10):
	print makeTabs(2) + "<p>" + mostCommonHits[x] + "</p>"'''


def lowestElem(li):
	res = 999999
	resInd = 0
	for x in range(0, len(li)):
		if li[x] < res:
			res = li[x]
			resInd = x
	return resInd

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

for x in range(0, 10):
	print makeTabs(2) + "<p>" + str(highWords[x]) + "</p>"
















print makeTabs(2) + "</table>"
print endPage()




