#returns a list
def makeList(s):
	ans = s.split("\n")
	temp = []
	for x in range(len(ans) - 1):
		temp = ans.pop(0).split(",")
		ans.append(temp)
	fixCommas(ans)
	return ans[1:]

#returns an html table in the form of string
def makeTableBody(L):
	res = ""
	tempThingy = False
	for x in L:
		res += "<tr>"
		for y in x:
			if not tempThingy:
				res += "<th>" + str(y) + "</th>"
				continue
			res += "<td>" + str(y) + "</td>"
		tempThingy = True
		res += "</tr>\n"
	return res.strip()

#Mr. K's function
#take a list of lists of strings join
#any inner commas between quotes.
def fixCommas(L):
    for inner in L:
        i=0
        while i < len(inner):
        	if len(inner[i]) <= 1:
        		break
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
