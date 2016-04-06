#!/usr/bin/python
print "content-type: text/html\n"

import random

def startPage(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def endPage():
	return makeTabs(1) + "</body>\n</html>"

def numToWords9(i):
	if i == 0:
		return ""
	elif i == 1:
		return "one"
	elif i == 2:
		return "two"
	elif i == 3:
		return "three"
	elif i == 4:
		return "four"
	elif i == 5:
		return "five"
	elif i == 6:
		return "six"
	elif i == 7:
		return "seven"
	elif i == 8:
		return "eight"
	elif i == 9:
		return "nine"

def numTeens(i):
	if i == 10:
		return "ten"
	elif i == 11:
		return "eleven"
	elif i == 12:
		return "twelve"
	elif i == 13:
		return "thirteen"
	elif i == 14:
		return "fourteen"
	elif i == 15:
		return "fifteen"
	elif i == 16:
		return "sixteen"
	elif i == 17:
		return "seventeen"
	elif i == 18:
		return "eighteen"
	elif i == 19:
		return "nineteen"

def numTensPlace(i):
	if i == 2:
		return "twenty"
	elif i == 3:
		return "thirty"
	elif i == 4:
		return "fourty"
	elif i == 5:
		return "fifty"
	elif i == 6:
		return "sixty"
	elif i == 7:
		return "seventy"
	elif i == 8:
		return "eighty"
	elif i == 9:
		return "ninety"

def placeTable(i):
	if i == 0:
		return ""
	elif i == 1:
		return " thousand "
	elif i == 2:
		return " million "
	elif i == 3:
		return " billion "
	elif i == 4:
		return " trillion "
	elif i == 5:
		return " quadillion "
	elif i == 6:
		return " quintillion "
	elif i == 7:
		return " sextillion "
	elif i == 8:
		return " septillion "
	elif i == 9:
		return " octillion "
	elif i == 10:
		return " nonillion "
	elif i == 11:
		return " decillion "
	elif i == 12:
		return " undecillion "
	elif i == 13:
		return " duodecillion "
	elif i == 14:
		return " tredecillion "
	elif i == 15:
		return " quattuordecillion "
	elif i == 16:
		return " quindecillion "
	elif i == 17:
		return " sexdecillion "
	elif i == 18:
		return " septendecillion "
	elif i == 19:
		return " octodecillion "
	elif i == 20:
		return " novemdecillion "

def numToWords99(i):
	if i < 10:
		return numToWords9(i)
	elif i >= 10 and i <= 19:
		return numTeens(i)
	elif i >= 20 and i <= 99:
		tens = i / 10
		ones = i % 10
		if ones == 0:
			return numTensPlace(tens)
		else:
			return numTensPlace(tens) + " " + numToWords9(ones)

def numToWords999(i):
	if i < 10:
		return numToWords9(i)
	elif i >= 10 and i <= 19:
		return numTeens(i)
	elif i >= 20 and i <= 99:
		return numToWords99(i)
	elif i >= 100 and i <= 999:
		hundreds = i / 100
		tens = (i / 10) % 10
		ones = i % 10
		return numToWords9(hundreds) + " hundred " + \
		numToWords99(tens * 10 + ones) 

def numToWordsBig(x):
	if x < 10:
		return numToWords9(x)
	elif x >= 10 and x <= 19:
		return numTeens(x)
	elif x >= 20 and x <= 99:
		return numToWords99(x)
	elif x >= 100 and x <= 999:
		return numToWords999(x)
	elif x >= 1000 and x <= 999999:
		thousands = x / 1000
		hundreds = x % 1000
		return numToWords999(thousands) + " thousand " + \
		numToWords999(hundreds)
	elif x >= 1000000 and x <= 999999999:
		millions = x / 1000000
		thousands = (x / 1000) % 1000
		hundreds = x % 1000
		result = numToWords999(millions) + " million "
		if thousands != 0:
			result += numToWords999(thousands) + " thousand "
		return result + numToWords999(hundreds)

def numToString(x):
    if x<0:
        return "negative "+numToString(abs(x))
    if x==0:
        return "zero"
    else:
        return numToWordsBigR(x, 0)

def numToWordsBigR(x, place):
	if x <= 999:
		return numToWords999(x) + placeTable(place)
	else:
		if x % 1000 != 0:
			return numToWordsBigR(x / 1000, place + 1) + \
			numToWords999(x % 1000) + placeTable(place)
		else:
			return numToWordsBigR(x / 1000, place + 1)

def makeTabs(num):
	result = ""
	for x in range(0, num):
		result += "    "
	return result

def makeTag(tag, elem):
	return "<" + tag + ">" + elem + "</" + tag + ">"

print startPage("numbers")

print makeTabs(2) + '<table border="1">'
x = random.randint(-999, 999)
y = random.randint(-999999, 999999)
z = random.randint(-999999999, 999999999)
print makeTabs(3) + "<tr>\n" + makeTabs(4) + makeTag("th", "Number") + \
makeTag("th", "How To Say The Number") + "\n" + makeTabs(3) + "</tr>\n"

print makeTabs(3) + "<tr>\n" + makeTabs(4) + makeTag("td", str(x)) + \
makeTag("td", numToString(x)) + "\n" + makeTabs(3) + "</tr>\n"

print makeTabs(3) + "<tr>\n" + makeTabs(4) + makeTag("td", str(y)) + \
makeTag("td", numToString(y)) + "\n" + makeTabs(3) + "</tr>\n"

print makeTabs(3) + "<tr>\n" + makeTabs(4) + makeTag("td", str(z)) + \
makeTag("td", numToString(z)) + "\n" + makeTabs(3) + "</tr>\n"

print makeTabs(2) + "</table>\n"





print endPage()




