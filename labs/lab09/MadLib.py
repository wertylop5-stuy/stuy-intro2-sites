import random

def replaceSpeechPart(target, partOfSpeech, dataArray):
	result = target
	hit = result.find(partOfSpeech)
	temp = ""
	while hit != -1:
		temp = dataArray[random.randint(0, len(dataArray) - 1)]
		result = result[:hit] + temp + result[hit + len(partOfSpeech):]
		#print res
		hit = result.find(partOfSpeech)
	return result


#storyString will have NOUN, ADJ, etc. scattered
#find the first instance of one of these
	#and match it to the coresponding word array
#return a string with the characters before the
	#hit appended with a random word, then the 
	#rest of the string appended
def madlibs(storyString, nounList, verbList, adjectiveList):
	#final string to return
	res = storyString
	hit = 0
	res = replaceSpeechPart(res, "NOUN", nounList)
	res = replaceSpeechPart(res, "VERB", verbList)
	res = replaceSpeechPart(res, "ADJECTIVE", adjectiveList)
	return res



print madlibs("hello NOUN NOUN NON VERB ADJ ECTIVE ADJECTIVE VERB hu ADJECTIVE", \
["operand", "yu"], ["running", "walking"], ["green", "smelly"])

print madlibs('''To VERB, or not to VERB--that is the NOUN:
Whether 'tis nobler in the NOUN to VERB
The NOUNs and NOUNs of ADJECTIVE fortune
Or to take NOUNs against a sea of NOUNs
And by opposing end them. To VERB, to VERB--
No more--and by a VERB to say we end
The heartache, and the thousand ADJECTIVE VERB
That flesh is heir to. ''', \
['fish','computer','Iphone','jaguar','mapo tofu'], \
['run','spin','talk','hit','jig','shave','cut','rap'], \
['silent','big','small','hairy','rich','amazing','outrageous','preposterous'])
