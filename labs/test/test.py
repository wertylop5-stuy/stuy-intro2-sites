def dictToList(	dictOne, 
				totalCount, 
				dictOneName = "",
				dictTwo = None,
				dictTwoName = ""):
	res = []
	temp = []
	
	#fun stuff, only 2 columns
	#first column is higher book name instead of word
	#second is difference in percentage
	if dictTwo:
		for x in dictOne.keys():
			if dictOne[x] > dictTwo[x]:
				temp.append(dictOneName)
				temp.append(
							(dictOne[x] / float(totalCount)) -
							(dictTwo[x] / float(totalCount)))
			else:
				temp.append(dictTwoName)
				temp.append(
							(dictTwo[x] / float(totalCount)) -
							(dictOne[x] / float(totalCount)))
			res.append(temp)
			temp = []
	else:
		for x in dictOne.keys():
			print x
			temp.append(x)
			temp.append(dictOne[x])
			temp.append(dictOne[x] / float(totalCount))
			
			res.append(temp)
			temp = []
	return res

print dictToList({"a":1, "b":2}, 3, "first", {"a":3, "b":0}, "sec")
