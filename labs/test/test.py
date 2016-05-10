def invertDict(d):
	res = {}
	
	#for dupe handling
	carry = 0
	letter = ord('a')
	tempKey = ""
	
	for x in d.keys():
		if not(d[x] in res):
			res[ d[x] ] = x
		#fun stuff
		else:
			tempKey = str(d[x])
			#puts a carry # of z before the letter
			if letter > ord('z'):
				letter = ord('a')
				carry += 1
			tempKey += ('z' * carry) + chr(letter)
			print tempKey
			letter += 1
			
			res[tempKey] = x
	return res

def mostCommon(dictX, keyOut, valOut):
	dictTemp = invertDict(dictX)
	#values is numbers, keys is words
	values = []
	keys = []
	
	#for extracting numbers from dupes
	tempChar = ""
	tempPos = 0
	tempList = []
	tempNum = 0
	
	#for making the final number
	counter = 1
	
	original = ""
	
	
	for x in dictTemp.keys():
		if str(x).isdigit():
			values.append(int(x))
			keys.append(dictTemp[x])
		#handle the tailing letters
		else:
			while tempPos < len(x) and x[tempPos].isdigit():
				tempChar = x[tempPos]
				tempPos += 1
				tempList.append(tempChar)
			tempPos = 0
			
			while len(tempList) > 0:
				 tempNum += int(tempList.pop()) * (10 ** counter)
				 counter += 1
			counter = 1
			
			values.append(tempNum)
			keys.append(dictTemp[x])
			
		#bad idea, huge amounts of lag
		values.sort()
		keys = []
		for y in values:
			print y
			keys.append(dictTemp[x])
	
	keyOut.extend(keys)
	valOut.extend(values)

a = []
b = []

mostCommon({
"a":194,
"b":194,
"c":198,
"d":200,
"e":202,
"f":204,
"g":194,
"h":208,
"i":210,
"j":212,
"k":214,
"l":216,
"m":218,
"n":220,
"o":222,
"p":224,
"q":226,
"r":228,
"s":230,
"t":232,
"u":234,
"v":236,
"w":238,
"x":240,
"y":242,
"z":244,
}, a, b)

print a
print b











'''
for x in range(ord('a'), ord('z') + 1):
	print "\"" + chr(x)+ "\"" + ":" + str(x * 2) + ","
'''



