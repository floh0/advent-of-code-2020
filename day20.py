with open("day20.txt", "r") as f:
	i = [x.split("\n") for x in "".join(f.readlines()).split("\n\n")]

m,t,b,l,r = {},{},{},{},{}
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
		if x != e and t[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
			c[x]["t"].append(e)
	for x in b:
		if x != e and b[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
			c[x]["b"].append(e)
	for x in l:
		if x != e and l[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
			c[x]["l"].append(e)
	for x in r:
		if x != e and r[x] in [b[e], b[e][::-1], t[e], t[e][::-1], l[e], l[e][::-1], r[e], r[e][::-1]]:
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
if c[e]["b"]:
	q[c[e]["b"][0]] = (0,-1)
if c[e]["l"]:
	q[c[e]["l"][0]] = (-1,0)
if c[e]["r"]:
	q[c[e]["r"][0]] = (1,0)
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

def rotate(q):
	qn = [[x for x in y] for y in q]
	for y in range(len(q)):
		qy = len(q[y])
		for x in range(qy):
			qn[y][x] = q[qy-1-x][y]
	return ["".join(x) for x in qn]

def flip(q):
	return [x[::-1] for x in q]

qqq = [[[] for _ in range(12)] for _ in range(12)]

for y in range(len(qq)):
	for x in range(len(qq[y])):
		if x == 0:
			t = m[qq[y][x]]
			if y == 0:
				qqq[y][x] = m[qq[y][x]]
			elif qqq[y-1][x][-1] == t[0]:
				qqq[y][x] = t
			elif qqq[y-1][x][-1] == t[0][::-1]:
				qqq[y][x] = flip(t)
			elif qqq[y-1][x][-1] == "".join([z[0] for z in t][::-1]):
				qqq[y][x] = rotate(t)
			elif qqq[y-1][x][-1] == "".join([z[0] for z in t]):
				qqq[y][x] = flip(rotate(t))
			elif qqq[y-1][x][-1] == t[-1][::-1]:
				qqq[y][x] = rotate(rotate(t))
			elif qqq[y-1][x][-1] == t[-1]:
				qqq[y][x] = flip(rotate(rotate(t)))
			elif qqq[y-1][x][-1] == "".join([z[-1] for z in t]):
				qqq[y][x] = rotate(rotate(rotate(t)))
			elif qqq[y-1][x][-1] == "".join([z[-1] for z in t][::-1]):
				qqq[y][x] = flip(rotate(rotate(rotate(t))))
		else:
			t = m[qq[y][x]]
			tt = "".join([z[-1] for z in qqq[y][x-1]])
			if tt == t[0]:
				qqq[y][x] = flip(rotate(t))
			elif tt == t[0][::-1]:
				qqq[y][x] = flip(rotate(flip(t)))
			elif tt == "".join([z[0] for z in t][::-1]):
				qqq[y][x] = flip(rotate(rotate(t)))
			elif tt == "".join([z[0] for z in t]):
				qqq[y][x] = t
			elif tt == t[-1][::-1]:
				qqq[y][x] = rotate(flip(t))
			elif tt == t[-1]:
				qqq[y][x] = rotate(t)
			elif tt == "".join([z[-1] for z in t]):
				qqq[y][x] = flip(t)
			elif tt == "".join([z[-1] for z in t][::-1]):
				qqq[y][x] = rotate(rotate(t))

qqqq = [[[z[1:-1] for z in x[1:-1]] for x in y] for y in qqq]

fp = []
for y in range(len(qqqq)):
	for z in range(len(qqqq[y][0])):
		s = ""
		for x in range(len(qqqq[y])):
			s += qqqq[y][x][z]
		fp.append(s)

#            1111111111
#  01234567890123456789
# 0                  # 
# 1#    ##    ##    ###
# 2 #  #  #  #  #  #   
def findmonster(x,y,fp):
	for e in [fp[y][x+18], fp[y+1][x], fp[y+1][x+5], fp[y+1][x+6], fp[y+1][x+11], fp[y+1][x+12], fp[y+1][x+17], fp[y+1][x+18], fp[y+1][x+19], fp[y+2][x+1], fp[y+2][x+4], fp[y+2][x+7], fp[y+2][x+10], fp[y+2][x+13], fp[y+2][x+16]]:
		if e != "#":
			return False
	return True

for fpp in [fp, rotate(fp),rotate(rotate(fp)),rotate(rotate(rotate(fp))),flip(fp),flip(rotate(fp)),flip(rotate(rotate(fp))),flip(rotate(rotate(rotate(fp))))]:
	nm = 0
	for y in range(len(fpp)-2):
		for x in range(len(fpp)-19):
			if findmonster(x,y,fpp):
				nm += 1
	if nm > 0:
		part2 = sum([1 if ee == "#" else 0 for e in fpp for ee in e])-nm*15
		print(part2)

for x in fp:
	print(x)
