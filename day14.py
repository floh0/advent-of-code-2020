import re

r = re.compile("(mask|mem)(?:\[([0-9]+)\])? = ([0-9X]+)")

with open("day14.txt", "r") as f:
	i = [(m.group(1),int(m.group(2)) if m.group(2) else 0,m.group(3)) for m in [r.match(x) for x in f.readlines()]]

M = max(i,key=lambda x:x[1])[1]
mem = [0 for _ in range(M+1)]

def build(m):
	m1=int("".join(["0" if b == "0" else "1" for b in m]),2)
	m2=int("".join(["1" if b == "1" else "0" for b in m]),2)
	return m1,m2

m1,m2 = 0,0
for a,b,c in i:
	if a == "mask":
		m1,m2 = build(c)
	else:
		mem[b] = (m1&int(c))|m2

part1 = sum(mem)
print(part1)