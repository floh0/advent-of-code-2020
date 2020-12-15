with open("day15.txt", "r") as f:
	i = [int(x) for x in f.readline().split(",")]

def find(num,init):
	m = {}
	n = 1
	l = None
	for x in init:
		if l is not None:
			m[l] = n
		l = x
		n += 1
	while n <= num:
		if l in m:
			nl = n-m[l]
		else:
			nl = 0
		m[l] = n
		l = nl
		n += 1
	return l

part1 = find(2020,i)
print(part1)
part2 = find(30000000,i)
print(part2)