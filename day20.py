with open("day20.txt", "r") as f:
	i = [x.split("\n") for x in "".join(f.readlines()).split("\n\n")]

t = {}
b = {}
l = {}
r = {}

m = {}
for a in i:
	m[a[0][5:-1]] = a[1:]

for x,y in m.items():
	t[x] = y[0]
	b[x] = y[-1][::-1]
	l[x] = "".join([z[0] for z in y][::-1])
	r[x] = "".join([z[-1] for z in y])

c = {x:{"t":[],"b":[],"l":[],"r":[]} for x in m}
for e in m:
	for x in t:
		if x != e:
			if t[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
				c[x]["t"].append(e)
	for x in b:
		if x != e:
			if b[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
				c[x]["b"].append(e)
	for x in l:
		if x != e:
			if l[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
				c[x]["l"].append(e)
	for x in r:
		if x != e:
			if r[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
				c[x]["r"].append(e)


part1 = 1
for x,y in c.items():
	if sum([0 if z else 1 for _,z in y.items()]) > 1:
		part1 *= int(x)
		e = x
print(part1)

q = {e: (0,0)}
if c[e]["t"]:
	q[c[e]["t"][0]] = (0,1)
	ly = -1 
if c[e]["b"]:
	q[c[e]["b"][0]] = (0,-1)
	lx = 1
if c[e]["l"]:
	q[c[e]["l"][0]] = (-1,0)
	ly = 1
if c[e]["r"]:
	q[c[e]["r"][0]] = (1,0)
	ly = -1
c = {k:v for k,v in c.items() if k != e}

while len(c) > 0:
	if len([x for x in list(c) if x in q]) > 0:
		e = [x for x in list(c) if x in q][0]
		x,y = q[e]
		if c[e]["l"] and c[e]["r"] and c[e]["r"][0] in q:
			nx,ny = q[c[e]["r"][0]]
			q[c[e]["l"][0]] = (2*x-nx,2*y-ny)
		if c[e]["r"] and c[e]["l"] and c[e]["l"][0] in q:
			nx,ny = q[c[e]["l"][0]]
			q[c[e]["r"][0]] = (2*x-nx,2*y-ny)
		if c[e]["t"] and c[e]["b"] and c[e]["b"][0] in q:
			nx,ny = q[c[e]["b"][0]]
			q[c[e]["t"][0]] = (2*x-nx,2*y-ny)
		if c[e]["b"] and c[e]["t"] and c[e]["t"][0] in q:
			nx,ny = q[c[e]["t"][0]]
			q[c[e]["b"][0]] = (2*x-nx,2*y-ny)
		c = {k:v for k,v in c.items() if k != e}
	else:
		for x,y in c.items():
			n = 0
			if y["t"] and y["t"][0] in q:
				n += 1
			if y["b"] and y["b"][0] in q:
				n += 1	
			if y["l"] and y["l"][0] in q:
				n += 1	
			if y["r"] and y["r"][0] in q:
				n += 1
			if n >= 2:
				e = x
		x = max([x for _,(x,y) in q.items() if abs(x) == abs(y)])
		dx,adx = max([(x,abs(x)) for _,(x,_) in q.items()], key=lambda x:x[1])
		dy,ady = max([(y,abs(y)) for _,(_,y) in q.items()], key=lambda x:x[1])
		q[e] = (x+int(dx/adx),x+int(dy/ady))

qq = [[0 for _ in range(12)] for _ in range(12)]
for u,(x,y) in q.items():
	qq[abs(y)][abs(x)] = u


