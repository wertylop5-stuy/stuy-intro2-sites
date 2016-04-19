#!/usr/bin/python
print "content-type: text/html\n"
#TODO
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
	#the 1 in VERB1
	tempNum = 0
	
	
	hit = result.find(partOfSpeech)
	while hit != -1:
		#if not end of string
		if result[hit:] != "":
			if result[hit + len(partOfSpeech)].isdigit():
				#temp takes value of whole hit including end number
				temp = result[hit:hit + len(partOfSpeech) + 1]
				if not(temp in prevValues):
					prevValues.append(temp)
					temp2 = dataArray[random.randint(0, \
					len(dataArray) - 1)]
					
					prevFind.append(temp2)
					
					#yes, this is destructive. probs a bad idea
					dataArray.remove(temp2)
				
				#only the end number of the hit
				tempNum = result[hit + len(partOfSpeech)]
				
				result = result.replace(partOfSpeech + tempNum, prevFind[int(tempNum) - 1])
			
			#could refactor this, but...
			else:
				temp = dataArray[random.randint(0, len(dataArray) - 1)]
				#dangerous
				dataArray.remove(temp)
				
				result = result[:hit] + temp + \
				result[hit + len(partOfSpeech):]
				hit = result.find(partOfSpeech)
		else:
			temp = dataArray[random.randint(0, len(dataArray) - 1)]
			#dangerous
			dataArray.remove(temp)
			
			result = result[:hit] + temp + \
			result[hit + len(partOfSpeech):]
		hit = result.find(partOfSpeech)
	return result
	
def madlibs(storyString, nounList, verbList, adjectiveList, \
properNounList, adverbList):
	#final string to return
	res = storyString
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

'''storyString = madlibs("NOUN VERB, ADJECTIVE:; PROPERnOUN []r ADvERB", \
["pizza", "donut"], ["running", "walking"], ["green", "yellow"], \
["Rick", "David"], ["quickly", "slowly"])'''
'''storyResult = madlibs("""
NOUN1 NOUN2, NOUN1 NOUN2.
VERB1 VERB1 VERB VERB1 VERB2 VERB2
ADJECTIVE1 ADJECTIVE ADJECTIVE2 ADJECTIVE1
PROPERnOUN PROPERnOUN1 PROPERnOUN1 PROPERnOUN2
""", \
["pizza", "donut", "cactus"], ["running", "walking", "swimming"], ["red", "green", "yellow"], \
["Rick", "David", "Morty"], ["heavenly", "quickly", "slowly"])'''

storyRoll = random.randint(0, 1)
storyString = ""
inStream = None
bbb = ""

if storyRoll == 1:
	bbb = "Romeo and Juliet"
	inStream = open("stories/story0.txt", "r")
	storyString = inStream.read()
	inStream.close()
else:
	bbb = "Wuthering Heights"
	inStream = open("stories/story1.txt", "r")
	storyString = inStream.read()
	inStream.close()

noun = ["laser gun", "lightsaber", "wormhole", "infinite improbability drive", "portal", \
"space-time continuum", "starship"]
adj = ["interstellar", "quantum", "universal", "otherworldy", "galactic"]
verb = ["fly", "blast", "warp", "teleport"]
proper = ["Ender", "Ford Prefect", "Obi Wan Kenobi", "Bugger"]
adverb =["silently", "slowly"]

storyResult = madlibs(storyString, noun, verb, adj, proper, adverb)

print makeTabs(2) + "<h1>" + "STORY TIMMMMEEEE!!!!!1!1" + "</h1>"
print makeTabs(2) + "<h3>" + bbb + "!!!!!1!1" + "</h3>"

print makeTabs(2) + "<p id='storyText'>" + storyResult + "</p>"

print makeTabs(2) + "<hr>"

print makeTabs(2) + "<h6>" + "If you are curious!" + "</h6>"
print makeTabs(2) + "<h6>" + storyString + "</h6>"
print makeTabs(2) + "<div id='ship'>"
print makeTabs(3) + "<img src='img/spaceship.png' />"
print makeTabs(2) + "</div>"

print endPage()









