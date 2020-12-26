import re

with open("day24.txt", "r") as f:
	i = f.readlines()

r = re.compile("se|sw|nw|ne|e|w")
cs = [r.findall(e) for e in i]

m2c = {
	"se": 1-1j,
	"sw": -1-1j,
	"nw": -1+1j,
	"ne": 1+1j,
	"e": 2,
	"w": -2
}

def finalcoord(p):
	z=0
	for x in p:
		z += m2c[x]
	return z

m = {}
for z in [finalcoord(e) for e in cs]:
	if z in m:
		m[z] ^= 1
	else:
		m[z] = 1

part1 = sum([v for _,v in m.items()])
print(part1)

def expand(m):
	mc = {k:v for k,v in m.items()}
	for k in m:
		for _,v in m2c.items():
			if k+v not in mc:
				mc[k+v] = 0
	return mc

def day(m):
	mc = {k:v for k,v in m.items()}
	for k,c in m.items():
		nv = 0
		for _,v in m2c.items():
			if k+v in m and m[k+v] == 1:
				nv += 1
		if c == 1 and (nv == 0 or nv > 2):
			mc[k] = 0
		elif c == 0 and nv == 2:
			mc[k] = 1
	return mc

for _ in range(100):
	m = day(expand(m))

part2 = sum([v for _,v in m.items()])
print(part2)



