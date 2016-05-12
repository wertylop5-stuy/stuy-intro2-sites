import hashlib
### ALL FUNCTIONS EXPECT LOWERCASE USERNAME


def dataWipe(direct, fileN):
	temp = open(direct + fileN, "w")
	temp.write("")
	temp.close()
	print "Wipe successful"

#removes commas
def fixPassword(password):
	res = password
	res = res.strip(",")
	while "," in res:
		res = res[:res.find(",")] + \
				res[res.find(",") + 1:]
	return res

#pass in directory name and file name
def getUsersFromFile(directory, fileN):
	temp = open(directory + fileN, "r")
	s = temp.read()
	temp.close()
	
	strippedData = s.split("\n")
	#removes the rest of the string after comma
	for index, value in enumerate(strippedData):
		strippedData[index] = value[:value.find(",")]
	strippedData.pop()
	return strippedData

#split form by comma
#if newline in element, pop it
#if username in resulting list, ignore
#else, add it
def addUser(directory, fileN, user, passW):
	stream = None
	userList = getUsersFromFile(directory, fileN)
	if not(user in userList):
		stream = open(directory + fileN, "a")
		stream.write(user + "," + 
					hashlib.sha256( fixPassword(passW) ).hexdigest() + 
					"\n")
		stream.close()

#validate username and password
def validateEntry(user, password, directory, fileN):
	userList = getUsersFromFile(directory, fileN)
	if not(user in userList):
		print "Login failed"
		return
	
	dataStream = open(directory + fileN, "r")
	rawText = dataStream.read()
	dataStream.close()
	
	userIndex = userList.index(user)
	loginPairs = rawText.split("\n")
	
	#still a username,password pair
	target = loginPairs[userIndex]
	target = target.split(",")
	
	if hashlib.sha256(password).hexdigest() == target[1]:
		print "Login success"
	else:
		print "Login failed"
	
	return














