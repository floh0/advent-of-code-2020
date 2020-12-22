with open("day22.txt", "r") as f:
	i = [[int(y) for y in x[10:].split("\n")] for x in "".join(f.readlines()).split("\n\n")]

def play(p1,p2,cw,g):
	while len(p1) > 0 and len(p2) > 0:
		if g(p1,p2):
			return p1,[]
		c1,p1 = p1[0],p1[1:]
		c2,p2 = p2[0],p2[1:]
		if cw(c1,c2,p1,p2) == 1:
			p1 = p1 + [c1,c2]
		else:
			p2 = p2 + [c2,c1]
	return p1,p2

def score(p):
	n,s = 1,0
	for c in p[::-1]:
		s += n*c
		n += 1
	return s	

p1,p2 = play(i[0],i[1],lambda c1,c2,p1,p2: 1 if c1>c2 else 2,lambda x,y: False)
part1 = score(p1 if p1 else p2)
print(part1)

def winner(c1,c2,p1,p2,c):
	if c1 <= len(p1) and c2 <= len(p2):
		s = set()
		p1,p2 = play(p1[:c1],p2[:c2],lambda x,y,z,w: winner(x,y,z,w,s), lambda x,y:game(x,y,s))
		return 1 if p1 else 2
	else:
		return 1 if c1>c2 else 2

def game(p1,p2,c):
	k = hash((tuple(p1),tuple(p2)))
	if k in c:
		return True
	else:
		c.add(k)
		return False

s = set()
p1,p2 = play(i[0],i[1],lambda x,y,z,w: winner(x,y,z,w,s), lambda x,y:game(x,y,s))
part2 = score(p1 if p1 else p2)
print(part2)