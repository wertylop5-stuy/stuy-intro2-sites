#!/usr/bin/python
print "content-type: text/html\n"

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

def TallyWords(text):
	#Converted form
	textList = []
	
	#remove whitespace
	textList = text.split()
	
	#stores useless punctuation, need extra test for apostrophe
	punct = ["!", "?", ":", ";", "/", ",", ".", '"']
	punctStr = '!?:;/,."'
	
	#so stuff isn't too long
	q = ""
	#(smartly) removes punctuation
	for x in range(0, len(textList)):
		q = textList[x]
		
		q = q.strip(punctStr)
		#prelim check for special case of ' after a "s"
		if q[len(q) - 2] == "s" and q[len(q) - 1] == "'":
			q += "!"
			q = q.strip("'").strip("!")
		else:
			q = q.strip("'")
		textList[x] = q
	
	#These two correspond with each other
	hits = []
	tally = []
	
	#Stores index of existing word in hits
	tempIndex = 0
	
	for x in textList:
		if not(x.lower() in hits):
			hits.append(x.lower())
			tally.append(1)
		else:
			tempIndex = hits.index(x.lower())
			tally[tempIndex] += 1
	
	fancyPrint(hits, tally)
	#return hits, tally

def fancyPrint(listA, listB):
	for x in range(0, len(listA)):
		#print listA[x], ":", listB[x]
		print makeTabs(3) + "<tr>"
		print makeElem(listA[x], 4)
		print makeElem(listB[x], 4)
		print makeTabs(3) + "</tr>"
	print ""





filename = "dante.txt"
inStream = open(filename, "r")
bookWords = inStream.read()

#print "Lots of text"
#print bookWords[:200]

'''print "List of text"
print bookWords.split()[:100]'''


print startPage("Counting Dante")
print makeTabs(2) + '<table border="1">'



print TallyWords(bookWords[170:])
























