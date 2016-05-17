import hashlib
import random
import os
### ALL FUNCTIONS EXPECT LOWERCASE USERNAME
### ALL FUNCTIONS EXPECT FIXED PASSWORDS 
### (EXCEPT FOR THE fixPassword FUNCTION)

def dataWipe(direct, fileN):
	temp = open(direct + fileN, "w")
	temp.write("")
	temp.close()
	print "Wipe successful"

#removes illegal characters
def fixEntry(entry):
	forbidden = "<>/\,"
	res = entry
	res = res.strip(forbidden)
	for char in forbidden:
		while char in res:
			res = res[:res.find(char)] + \
					res[res.find(char) + 1:]
	return res

#pass in directory name and file name
#legacy: only works with user names
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

#pass in directory name and file name
#newer one that can access all data
def getFileData(directory, fileN):
	temp = open(directory + fileN, "r")
	s = temp.read()
	temp.close()
	
	strippedData = s.split("\n")
	strippedData.pop()
	#removes the rest of the string after comma
	for index, data in enumerate(strippedData):
		print data
		strippedData[index] = data.split(",")
		print strippedData[index]
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
					hashlib.sha256(passW).hexdigest() + 
					"\n")
		stream.close()

#validate username and password
def validateEntry(user, password, directory, fileN):
	userList = getUsersFromFile(directory, fileN)
	if not(user in userList):
		print "Login failed"
		return False
	
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
		return True
	else:
		print "Login failed"
		return False

def login(user, password, directory, fileN, logFile):
	#check if good login
	if validateEntry(user, password, directory, fileN):
		loginStream = open(directory + logFile, "w")
		randNum = random.randint(0, 90000000)
		ip = os.environ["REMOTE_ADDR"]
		
		loginStream.write(user + ",")
		loginStream.write(str(randNum) + ",")
		loginStream.write(ip)
		
		loginStream.close()
		return randNum












