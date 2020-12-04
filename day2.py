import re

with open("day2.txt", "r") as f:
	input = f.readlines()

def part1(m,M,l,s):
	a = 0
	for b in s:
		if b == l:
			a += 1
	return a >= m and a <= M

def part2(m,M,l,s):
	return (s[m-1] == l) ^ (s[M-1] == l)

r = re.compile(r"([0-9]+)\-([0-9]+)\s([a-z])\:\s([a-z]+)")

i = 0

for a in input:
	m, M, l, s = r.match(a).group(1,2,3,4)
	if part2(int(m),int(M),l,s):
		i+=1

print(i)
