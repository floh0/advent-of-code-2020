import re

with open("day5.txt", "r") as f:
	i = f.readlines()

r = 128
c = 8

sr = re.compile(r"([F|B]+)([L|R]+)")

def foo(m,M,l):
	d = (M-m)//2+m
	if l == "F" or l == "L":
		return m,d
	if l == "B" or l == "R":
		return d+1,M

def seat(s):
	rm = sr.match(s)
	f,e = rm.group(1), rm.group(2)
	x0,x1 = 0,r-1
	y0,y1 = 0,c-1
	for x in f:
		x0,x1 = foo(x0,x1,x)
	for y in e:
		y0,y1 = foo(y0,y1,y)
	return x0,y0

def id(x,y):
	return x*8+y

part1 = [id(x,y) for (x,y) in [seat(s) for s in i]]
print(max(part1))

def findmissing(t):
	z = [0 for a in range(len(t)+1)]
	m = min(t)
	for a in t:
		z[a-m] = 1
	for a in range(len(z)):
		if z[a] == 0:
			return a+m

print(findmissing(part1))

