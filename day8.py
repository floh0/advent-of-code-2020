import re

with open("day8.txt", "r") as f:
	i = f.readlines()

r = re.compile(r"(acc|jmp|nop) ([+|-][0-9]+)")

prog = [(m.group(1), int(m.group(2))) for m in [r.match(row) for row in i]]

do = {
	"acc": (lambda x,acc,index: (acc+x,index+1)),
	"nop": (lambda x,acc,index: (acc,index+1)),
	"jmp": (lambda x,acc,index: (acc,index+x))
}

def run(prog):
	acc = 0
	visited = []
	index = 0
	while index < len(prog):
		visited.append(index)
		inst,value = prog[index]
		acc,index = do[inst](value,acc,index)
		if index in visited:
			return False, acc
	return True, acc

_,part1 = run(prog)
print(part1)

swap = lambda x: "jmp" if x == "nop" else "nop"

for x in range(len(prog)):
	if prog[x][0] != "acc":
		prog[x] = (swap(prog[x][0]), prog[x][1])
		terminate,part2=run(prog)
		if terminate:
			print(terminate,part2)
		prog[x] = (swap(prog[x][0]), prog[x][1])



