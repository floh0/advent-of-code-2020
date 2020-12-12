import re

with open("day12.txt", "r") as f:
	i = f.readlines()

r = re.compile("([NSEWLRF])([0-9]+)")

p = ["E", "S", "W", "N"]

def manhattan(m):
	x = abs(m["N"]-m["S"])
	y = abs(m["E"]-m["W"])
	return x+y

def compute(i,f,c):
	m = {
		"N": 0, "S": 0, "E": 0, "W": 0
	}
	for e in i:
		rm = r.match(e)
		d,v = rm.group(1),int(rm.group(2))
		m,c = f(c,m,d,v)
	return m

def mpart1(c,m,d,v):
	if d in m:
		m[d] += v
	elif d == "R":
		c = (c+v//90)%4
	elif d == "L":
		c = (c-v//90)%4
	elif d == "F":
		m[p[c]] += v
	return m,c

def mpart2(w,m,d,v):
	if d in w:
		w[d] += v
	elif d == "R":
		for _ in range((v//90)%4):
			w["N"],w["S"],w["E"],w["W"]=w["W"],w["E"],w["N"],w["S"]
	elif d == "L":
		for _ in range((v//90)%4):
			w["N"],w["S"],w["E"],w["W"]=w["E"],w["W"],w["S"],w["N"]
	elif d == "F":
		for _ in range(v):
			m["N"] += w["N"]
			m["S"] += w["S"]
			m["E"] += w["E"]
			m["W"] += w["W"]
	return m,w

part1 = manhattan(compute(i,mpart1,0))
print(part1)
part2 = manhattan(compute(i,mpart2,{"N":1,"S":0,"E":10,"W":0}))
print(part2)

