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

def foo(t, acc):
	if t not in acc:
		acc.append(t)
	for x in range(len(t)-1):
		a = sum(t[x:x+2])
		if a <= 3:
			nt = t[:x] + [a] + t[x+2:]
			foo(nt, acc)
	return acc

def bar(n):
	return len(foo([1 for x in range(n)], []))

acc = 0
part2 = 1
for x in range(len(ci)):
	if ci[x] == 3:
		part2 *= bar(acc)
		acc = 0
	else:
		acc += 1

print(part2)



