with open("day6.txt", "r") as f:
	i = [x.split("\n") for x in "".join(f.readlines()).split("\n\n")]

def foo(t, f):
	m = {}
	for a in t:
		for b in a:
			if b in m:
				m[b] += 1
			else:
				m[b] = 1
	return [m for a,b in m.items() if f(b)]

part1 = sum([len(foo(a, lambda x: True)) for a in i])
print(part1)

part2 = sum([len(foo(a, lambda x: x == len(a))) for a in i])
print(part2)

	