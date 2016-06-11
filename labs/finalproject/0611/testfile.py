def deleteBrackets(s):
	res = ""
	res = s.strip("<>")
	
	hit = -1
	while "<" in res:
		hit = res.index("<")
		res = res[:hit] + res[hit + 1:]
	while ">" in res:
		hit = res.index(">")
		res = res[:hit] + res[hit + 1:]
	return res


print deleteBrackets("<><><><herh<34<>rerh>>trejh><><")
