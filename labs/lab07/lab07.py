#!/usr/bin/python
print "content-type: text/html\n"
#to help debug
import cgitb
cgitb.enable()

#needed this
def hasNumber(s):
    return False
    for c in "0123456789":
        if c in s:
            return True;
    return False;

#process a url appliying your function to each word
def modifySite(url,f):
    #to get info from the URL string
    import cgi
    form = cgi.FieldStorage()
    if "url" in form:
        url = form.getvalue('url')
    #to load a web page into a string
    import urllib2
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    #to get the root of the website this is a hacky way for valid urls..
    if("://" in url):
        url = url[:url.find("/",8)+1]
    else:
        url = url[:url.find("/")+1]

    #in case not a valid html page:
    head = "<html><head><title>Random Page?</title></head>\n<body>"
    if "<body" in page:
        head = page.split("<body")[0]
        page = page.split("<body")[1]
        page = "<body>\n"+page[page.find(">")+1:]

    #This is just a quick and dirty solution
    #that will fix SOME broken links and css. (Works on wikis)
    head = head.replace('src="','href="'+url)
    page = page.replace('src="','href="'+url)
    head = head.replace(url+'/',url)
    page = page.replace(url+'/',url)
    head = head.replace('href="/','href="'+url)
    page = page.replace('href="/','href="'+url)
   
    #process the words not in tags.
    tag = False;
    quote = False;
    last =''
    ans = ""
    index = 0;
    start = 0;
    end = 0;
    justended = False;
    line = []
    for c in page:
        if c == "<" and not quote:
            tag = True
            end = index
            justended = True;
        elif c == ">" and not quote:
            tag = False
            ans+=c
            start = index+1
        elif not tag and c =='"':
            quote = not quote
        if tag:
            if(justended):
                justended=False;
                line = page[start:end]
                words = line.split();
                for word in words:
                    prefix =""
                    suffix =""
                    #check for punctuation!
                    if len(word) > 0 and not word[0].isalpha():
                        prefix = word[0]
                        word = word[1:]
                    if len(word) > 0 and not word[-1].isalpha():
                        suffix = word[-1]
                        word = word[:-1]
                    if not hasNumber(word):
                        if len(word) > 0 and word[0]>='A' and word[0]<='Z':
                            word = f(word).capitalize()
                        else:
                            word = f(word)
                    ans+= prefix + word +suffix+" "
            ans+=c
        index += 1
    return head + ans

######################################################
#PLACE YOUR FUNCTIONS HERE:

import random
def modifyWords(s):
	randNum = random.randint(0, 1)
	if randNum:
		return pigLatin(s)
	else:
		return rot13(s)

#pigLatin
def pigLatin(s):
	if len(s) <= 0:
		return s
	elif s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or \
	s[0] == 'o' or s[0] == 'u':
		return s + "hay"
	else:
		return s[1:len(s)] + s[0] + "ay"

#rot13
def rot13char(c):
	val = ord(c)
	if val >= ord('a') and val <= ord('z'):
		return chr( ( ( (val - ord('a')) + 13) % 26) + ord('a'))
	elif val >= ord('A') and val <= ord('Z'):
		return chr( ( ( (val - ord('A')) + 13) % 26) + ord('A'))
	else:
		return c

def rot13(s):
	result = ""
	for x in s:
		result += rot13char(x)
	return result

#romanize
def romanize(s):
    s = s.replace("U","V")
    s = s.replace("u","v")
    return s
#no change
def noChange(s):
    return s
#make silly changes
def addIsh(s):
    return s+"ishkabibble"







url ='https://en.wikipedia.org/wiki/Latin'
######################################################
#which function to use? (notice do not CALL the function, just give the function name!)
function = modifyWords
#Replace noChange to whichever function you would like to be applied to the website:
#e.g.
#function = addIsh
#or
#function = romanize

#this uses 
print modifySite(url,function)

