with open("day11.txt", "r") as f:
	i = [[y for y in x] for x in f.read().split("\n")]

def iter(t,cs,l):
	nt = [[y for y in x] for x in t]
	for y in range(len(t)):
		for x in range(len(t[y])):
			if t[y][x] != ".":
				n = 0
				for z,c in cs.items():
					if c(t,x,y):
						n += 1
				if t[y][x] == "L" and n == 0:
					nt[y][x] = "#"
				if t[y][x] == "#" and n >= l:
					nt[y][x] = "L"
	return nt

def eq(a,b):
	for y in range(len(a)):
		for x in range(len(a[y])):
			if a[y][x] != b[y][x]:
				return False
	return True

def loop(i,cs,l):
	pi = i
	ni = iter(i,cs,l)
	while not eq(pi, ni):
		pi = ni
		ni = iter(ni,cs,l)
	return ni

def num(i):
	n = 0
	for y in range(len(i)):
		for x in range(len(i[y])):
			if i[y][x] == "#":
				n += 1
	return n

def lf(l):
	for a in l:
		if a == "#":
			return True
		elif a == "L":
			return False
	return False

checks1 = {
	"tl": lambda t,x,y: y-1 >= 0 and x-1 >= 0 and t[y-1][x-1] == "#",
	"l": lambda t,x,y: x-1 > -1 and t[y][x-1] == "#",
	"bl": lambda t,x,y: y+1 < len(t) and x-1 >= 0 and t[y+1][x-1] == "#",
	"b": lambda t,x,y: y+1 < len(t) and t[y+1][x] == "#",
	"br": lambda t,x,y: y+1 < len(t) and x+1 < len(t[y+1]) and t[y+1][x+1] == "#",
	"r": lambda t,x,y: x+1 < len(t[y]) and t[y][x+1] == "#",
	"tr": lambda t,x,y: y-1 >= 0 and x+1 < len(t[y-1]) and t[y-1][x+1] == "#",
	"t": lambda t,x,y: y-1 >= 0 and t[y-1][x] == "#",
}

checks2 = {
	"tl": lambda t,x,y: lf([t[y-z-1][x-z-1] for z in range(min(x,y))]),
	"l": lambda t,x,y: lf([t[y][x-z-1] for z in range(x)]),
	"bl": lambda t,x,y: lf([t[y+z+1][x-z-1] for z in range(min(x,len(t)-1-y))]),
	"b": lambda t,x,y: lf([t[y+z+1][x] for z in range(len(t)-1-y)]),
	"br": lambda t,x,y: lf([t[y+z+1][x+z+1] for z in range(min(len(t[y])-1-x,len(t)-1-y))]),
	"r": lambda t,x,y: lf([t[y][x+z+1] for z in range(len(t[y])-1-x)]),
	"tr": lambda t,x,y: lf([t[y-z-1][x+z+1] for z in range(min(len(t[y])-1-x,y))]),
	"t": lambda t,x,y: lf([t[y-z-1][x] for z in range(y)]),
}

part1 = num(loop(i, checks1, 4))
print(part1)
part2 = num(loop(i, checks2, 5))
print(part2)
