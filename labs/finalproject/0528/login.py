#!/usr/bin/python

#do not print things yet!
import cgi,cgitb,hashlib,Cookie,pickle,sys
cgitb.enable()
form = cgi.FieldStorage()

sys.path.insert(0, "../modules")
import stdStuff

# set some constants so we can replace numbers up here
USER_EXPIRE_TIME =     60 * 60 # 1 hour
#PASSWORD_EXPIRE_TIME = 60 * 1  # 1 minutes
PASSWORD_EXPIRE_TIME = 60 * 60

# create the cookie with a dummy value
c=Cookie.SimpleCookie()
c['loaded']='True'

#set up your page in pieces, do not print in your code, just
#append to the body if you want to see text.
head = '''
<html>
<head><title>Login page</title>
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''


    

def authenticate(u,p):
	hashedP = hashlib.sha256(password).hexdigest()
	userReadStream = open(stdStuff.directory + stdStuff.userFile, "r")
	userList = []
	try:
		while True:
			userList.append(pickle.load(userReadStream))
	except EOFError:
		pass
	finally:
		userReadStream.close()
	
	for x in userList:
		if hashedP == x.password:
			return True
	return False



#writeOrReplace writes a logged in user to a text file
#this should only be called after a user authenticates
def writeOrReplace(filename,username,number,IP):
    #check if you need to remove old values
    f = open(filename,'r').read().split("\n");
    data = [each.split(',') for each in f]
    write = False
    for i in range(len(data))[::-1]:
        if data[i]==['']:
            write = True
            data.pop(i)
        elif data[i][0]==username:
            data.pop(i)
            write = True
    ##remove a line if needed
    if write:
        res = ""
        for each in data:
            res+= ",".join(each)+"\n"
        f = open(filename,'w')
        f.write(res)
        f.close()
    #append the line to the file
    f = open(filename,'a')
    f.write(username+","+str(number)+","+str(IP)+"\n")
    f.close()
    
def createCookie(c,username,ID):
    c['username']=username
    c['ID']=ID
    c['username']['expires']=USER_EXPIRE_TIME
    c['ID']['expires']=PASSWORD_EXPIRE_TIME

    
if 'username' in form and 'password' in form:
    username = form.getvalue('username')
    password = form.getvalue('password')
    if authenticate(username,password):
        import os,random
        IP = os.environ['REMOTE_ADDR']
        ID = random.randint(1000000,9999000)
        
        #print some debug info at the top of the page:
        #body += "Success!<br>"
        #body += "Random Number: "+str(ID)+"<br>"
        #body += "IP: "+ IP + "<br>"

        #write to a file
        writeOrReplace(stdStuff.directory + stdStuff.logFile,username,ID,IP)

        #create a cookie:
        createCookie(c,username,ID)
        ##debug statements
        #body+= "cookie created<br>"
        #for each in c:
        #    body+= each+":"+c[each].value+"<br>"

        #attach a link:
        body+='<a href="profile.py">Go To Profile Page</a><br>'
    else:
        body += "Failed to authenticate"
else:
    body = '''
    <h1>Log in:</h1>
    <form action="login.py">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="log in">
    '''
                    


#print the cookie first, then content type, then the page
print c
print 'content-type: text/html\n'
print head
print body
print foot
