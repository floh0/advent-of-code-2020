with open("day10.txt", "r") as f:
	i = [int(x) for x in f.readlines()]

li = len(i)
si = sorted(i)
a = 0
b = si[li-1]+3

ni = [a] + si + [b]

ci = [ni[x+1]-ni[x] for x in range(li+1)]

n1 = 0
n3 = 0
for n in ci:
	if n == 1:
		n1 += 1
	elif n == 3:
		n3 += 1

part1 = n1*n3
print(n1, n3, part1)

g = []
acc = 0
for x in range(len(ci)):
	if ci[x] == 3:
		g.append(acc)
		acc = 0
	else:
		acc += 1

print(ci)
print(g)

1 1 1 1
2 1 1
1 2 1
1 1 2
2 2
3 1
1 3

1 1 1
2 1
1 2
3

1 1
2

0 -> 1
1 -> 1
2 -> 2
3 -> 4


