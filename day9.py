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

