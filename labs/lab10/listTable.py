#!/usr/bin/python
print "content-type: text/html\n"

def makeList(s):
	ans = s.split("\n")
	temp = []
	for x in range(len(ans) - 1):
		temp = ans.pop(0).split(",")
		ans.append(temp)
	fixCommas(ans)
	return ans

def makeTableBody(L):
	res = ""
	for x in L:
		res += "<tr>"
		for y in x:
			res += "<td>" + str(y) + "</td>"
		res += "</tr>\n"
	return res.strip()

#Mr. K's function
#take a list of lists of strings join
#any inner commas between quotes.
def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
            res = ''
            #if you see an open double quote pop and 
            #concatenate them until you see a close quote.
            if inner[i][0]=='"':
                while inner[i][-1] != '"' and i<len(inner):
                    res += inner[i]+","
                    inner.pop(i)
                #when you find the close quote,
                #replace it with the completed string.
                inner[i]=(res+inner[i]).strip('"')
            i+=1


################## BEGIN HTML STUFF ##################
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

dataStream = open("SAT.csv", "r")
text = dataStream.read()
dataStream.close()

satData = makeList(text)

print startPage("SAT things")
print makeTabs(2) + "<table>"

#satData holds the table of tables
print makeTableBody(satData[:5])

print "</table>"






print endPage()




