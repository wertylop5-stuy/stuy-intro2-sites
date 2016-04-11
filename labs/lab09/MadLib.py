import random

#storyString will have NOUN, ADJ, etc. scattered
#find the first instance of one of these
	#and match it to the coresponding word array
#return a string with the characters before the
	#hit appended with a random word, then the 
	#rest of the string appended


def madlibs(storyString, nounList, verbList, adjectiveList):
	#final string to return
	res = ""
	hit = 0
	hit = storyString.find("NOUN")
	while hit != 0:
		res = res[:hit] + nounList[random.randint(
		
