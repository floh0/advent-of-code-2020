with open("day9.txt", "r") as f:
	i = [int(x) for x in f.readlines()]

part1 = 25

def check(index):
	for x in range(index-25,index):
		for y in range(x+1,index):
			if i[x]+i[y] == i[index]:
				return True
	return False

while part1 < len(i) and check(part1):
	part1 += 1

num = i[part1]
print(num, part1)

s = i[:part1]

def continuous(input, size):
	for x in range(len(input)-size+1):
		if sum(input[x:x+size]) == num:
			return input[x:x+size]

for x in range(part1,1,-1):
	part2 = continuous(s, x)
	if part2:
		print(part2)
		print(min(part2),max(part2))
		print(min(part2)+max(part2))
