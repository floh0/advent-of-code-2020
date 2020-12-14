import re

r = re.compile("(mask|mem)(?:\[([0-9]+)\])? = ([0-9X]+)")

with open("day14.txt", "r") as f:
	i = [(m.group(1),int(m.group(2)) if m.group(2) else 0,m.group(3)) for m in [r.match(x) for x in f.readlines()]]

def build(m):
	m1=int("".join(["0" if b == "0" else "1" for b in m]),2)
	m2=int("".join(["1" if b == "1" else "0" for b in m]),2)
	return m1,m2

mem = {}
m1,m2 = 0,0
for a,b,c in i:
	if a == "mask":
		m1,m2 = build(c)
	else:
		mem[b] = (m1&int(c))|m2

part1 = sum([x for _,x in mem.items()])
print(part1)

def addresses(m,n):
	x = m.count("X")
	nm = n|int("".join(["1" if b == "1" else "0" for b in m]),2)
	nl = [z for z in "{:036b}".format(nm)]
	for y in range(len(m)):
		if m[y] == "X":
			nl[y] = "X"
	nn = "".join(nl)
	al=[]
	for z in range(2**x):
		a = nn
		for b in ("{:0%sb}"%x).format(z):
			a = re.sub("X",b,a,count=1)
		al.append(int(a,2))
	return al

mem = {}
cm = 0
for a,b,c in i:
	if a == "mask":
		cm = c
	else:
		for a in addresses(cm,b):
			mem[a] = int(c)

part2 = sum([x for _,x in mem.items()])
print(part2)