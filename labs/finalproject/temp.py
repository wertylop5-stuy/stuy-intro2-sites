import pickle,sys
sys.path.insert(0, "modules/")
import stdStuff

thingy = open("data/posts.txt", "r")

res = []

try:
	while True:
		res.append(pickle.load(thingy))
except EOFError:
	pass
finally:
	thingy.close()

for x in res:
	print x.id, x.score
