from ply import lex
from ply import yacc
import re

with open("day19.txt", "r") as f:
	i = "".join(f.readlines()).split("\n\n")

ii = i[0].split("\n")

rf = re.compile(r"([0-9]+): (((?:[0-9]+(?:(?: |(?: \| ))[0-9]+)*))|(?:\"[a-z]\"))")
ra = re.compile(r"\"([a-z])\"")
rr = re.compile(r"[0-9]+(?: [0-9]+)*")

mi = {}
ti = {}
for a in ii:
	x = rf.match(a)
	a,b = x.group(1),x.group(2)
	y = ra.match(b)
	if y:
		ti[a] = y.group(1)
	else:
		z = rr.findall(b)
		if z:
			mi[a] = [w.split(" ") for w in z]

def buildregex(n,m,t,f):
	if n in t:
		return t[n]
	else:
		s = "("
		for a in range(len(m[n])):
			s += "("
			b = ["(" + buildregex(b,m,t,f) + ")" for b in m[n][a]]
			if n in f:
				s += f[n](b)
			else:
				s += "".join(b)
			s += ")"
			if a < len(m[n])-1:
				s += "|"
		s += ")"
		return s

def count(rr):
	c = 0
	for e in i[1].split("\n"):
		if rr.match(e):
			c += 1
	return c

part1 = count(re.compile("^"+buildregex("0",mi,ti,{})+"$"))
print(part1)

f = {
	"8": lambda t: t[0]+"+",
	"11": lambda t: "|".join(["("+"".join(["((%s){%s})" % (a,i) for a in t])+")" for i in range(1,10)])
}
part2 = count(re.compile("^"+buildregex("0",mi,ti,f)+"$"))
print(part2)