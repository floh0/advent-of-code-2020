import re

with open("day16.txt", "r") as f:
	i = "".join(f.readlines())

r = re.compile(r"([a-z ]+): ([0-9]+\-[0-9]+ (?:or [0-9]+\-[0-9]+)*)")

si = i.split("\n\n")
mi = {a: [tuple(int(y) for y in x.split("-")) for x in b.split(" or ")] for a,b in r.findall(si[0])}

def isvalid(num,rules):
	for _,rule in rules.items():
		for m,M in rule:
			if num >= m and num <= M:
				return True
	return False

e = []
g = []
ts = [[int(y) for y in x.split(",")] for x in si[2].split("\n")[1:]]
for t in ts:
	v = True
	for n in t:
		if not isvalid(n,mi):
			e.append(n)
			v = False
	if v:
		g.append(t)

part1 = sum(e)
print(part1)

mt = [int(x) for x in si[1].split("\n")[1].split(",")]

def ispossible(num,boundaries):
	for n in num:
		if not True in [n >= m and n <= M for m,M in boundaries]:
			return False
	return True

c = {x:[] for x in mi}
for n,b in mi.items():
	for x in range(len(mt)):
		if ispossible([g[y][x] for y in range(len(g))],b):
			c[n].append(x)

print(c)
