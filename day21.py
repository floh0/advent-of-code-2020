import re

with open("day21.txt","r") as f:
	i = f.readlines()

r = re.compile(r"([a-z ]+) \(contains ([a-z, ]+)\)")

aw = []

for e in i:
	rm = r.match(e)
	w,a = rm.group(1).split(" "),rm.group(2).split(", ")
	aw.append((a,w))

at = set([y for x,_ in aw for y in x if y])
wa = [y for _,x in aw for y in x if y]
wt = set(wa)

m = {k:{j for j in at} for k in wt}

for a,w in aw:
	for k in wt:
		if k not in w:
			for j in a:
				if j in m[k]:
					m[k].remove(j)

part1 = sum([sum([1 for e in wa if e == k]) for k,v in m.items() if not v])
print(part1)

m = {k:v for k,v in m.items() if v}
ma = {}
while len(m) > 0:
	l = {k:list(v)[0] for k,v in m.items() if len(v) == 1}
	m = {k:[w for w in v if w not in l.values()] for k,v in m.items() if k not in l}
	ma = {**ma, **l}

part2 = ",".join([x for x,_ in sorted(list(ma.items()),key=lambda x: x[1])])
print(part2)