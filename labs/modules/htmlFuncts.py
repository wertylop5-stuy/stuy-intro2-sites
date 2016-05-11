def startPage(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(2) + "<link rel='stylesheet' href='pretty.css'>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def startPageN(title):
	return "<!DOCTYPE html>\n<html>\n" + makeTabs(1) + \
	"<head>\n" + makeTabs(2) + "<title>" + title + "</title>\n" + \
	makeTabs(2) + "<link rel='stylesheet' href='stylesheet.css'>\n" + \
	makeTabs(1) + "</head>\n" + makeTabs(1) + "<body>"

def endPage():
	return makeTabs(1) + "</body>\n</html>"

def makeTabs(num):
	result = ""
	for x in range(0, num):
		result += "    "
	return result
