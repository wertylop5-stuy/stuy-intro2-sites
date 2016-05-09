def dictToList(dictOne, totalCount, dictTwo = None):
	res = []
	temp = []
	
	if dictTwo:
		pass
	else:
		for x in dictOne.keys():
			print x
			temp.append(x)
			temp.append(dictOne[x])
			temp.append(dictOne[x] / float(totalCount))
			
			res.append(temp)
			temp = []
	return res

print dictToList({"a":5, "y":10, 6:15}, 30)
