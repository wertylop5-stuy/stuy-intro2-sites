#!/usr/bin/python
print "content-type: text/html\n"
#TODO finish up the VERB1 detection stuff
import random

#storyString will have NOUN, ADJ, etc. scattered
#find the first instance of one of these
	#and match it to the coresponding word array

#return a string with the characters before the
	#hit appended with a random word, then the 
	#rest of the string appended

#handling speechParts with numbers (lowest number is 1)
	#check if the hit is the last word in the string
		#if it is, normal execution
	
	#else, if the character right after the hit is
		#a number, search an array of previous hits
			#if not initially there, append it and move on
			#if exists, take the value at that index and 
			#replace the hit with ie
def replaceSpeechPart(target, partOfSpeech, dataArray):
	result = target
	
	#handles speechParts with numbers'
	#holds the randomly assigned values
	prevFind = []
	#holds the previously found occurences (ex VERB1)
	prevValues = []
	temp = ""
	temp2 = ""
	
	hit = result.find(partOfSpeech)
	while hit != -1:
		if not(result[hit:] != "") and \
		result[hit + len(partOfSpeech)].isDigit():
			temp = result[hit:hit + len(partOfSpeech)]
			if not(temp in prevValues):
				prevValues.append(temp)
				temp2 = dataArray[random.randint(0, \
				len(dataArray) - 1)]
				
				prevFind.append(temp2)
				
			else:
				
		else:
			temp = dataArray[random.randint(0, len(dataArray) - 1)]
			result = result[:hit] + temp + \
			result[hit + len(partOfSpeech):]
			#print res
			hit = result.find(partOfSpeech)
	return result
	
def madlibs(storyString, nounList, verbList, adjectiveList, \
properNounList, adverbList):
	#final string to return
	res = storyString
	hit = 0
	res = replaceSpeechPart(res, "NOUN", nounList)
	res = replaceSpeechPart(res, "VERB", verbList)
	res = replaceSpeechPart(res, "ADJECTIVE", adjectiveList)
	res = replaceSpeechPart(res, "PROPERnOUN", properNounList)
	res = replaceSpeechPart(res, "ADvERB", adverbList)
	return res



'''print madlibs("hello NOUN NOUN NON VERB ADJ ECTIVE ADJECTIVE VERB hu ADJECTIVE", \
["operand", "yu"], ["running", "walking"], ["green", "smelly"])'''

'''print madlibs("NOUN VERB, ADJECTIVE:; PROPERnOUN []r ADvERB", \
["pizza", "donut"], ["running", "walking"], ["green", "yellow"], \
["Rick", "David"], ["quickly", "slowly"])'''


################### BEGIN WEBSITE ###################
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


print startPage("STORIES!!!!")

storyString = madlibs("NOUN VERB, ADJECTIVE:; PROPERnOUN []r ADvERB", \
["pizza", "donut"], ["running", "walking"], ["green", "yellow"], \
["Rick", "David"], ["quickly", "slowly"])

print makeTabs(2) + "<h1>" + "STORY TIMMMMEEEE!!!!!1!1" + "</h1>"

print makeTabs(2) + "<p id='storyText'>" + storyString + "</p>"


print endPage()









