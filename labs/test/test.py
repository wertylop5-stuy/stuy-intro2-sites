def fixPassword(password):
	res = password
	res = res.strip(",")
	while "," in res:
		res = res[:res.find(",")] + \
				res[res.find(",") + 1:]
	return res

print fixPassword(",")
