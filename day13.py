with open("day13.txt", "r") as f:
	w,i = int(f.readline()), f.readline().split(",")

c = []
for e in i:
	if e != "x":
		a = int(e)
		d = a*(1+w//a)
		c.append((a,d))
		
a,b = min(c,key=lambda x:x[1])
part1 = (b-w)*a
print(part1)

def bezout(a,ua,va,b,ub,vb):
	if b == 0:
		return ua,va
	else:
		return bezout(b,ub,vb,a%b,ua-(a//b)*ub,va-(a//b)*vb)

def solve(m):
	n = 1
	for _,e in m:
		n *= e
	r = 0
	for a,e in m:
		nn = n//e
		u,_ = bezout(nn,1,0,e,0,1)
		r += a*u*nn
	return r

m = []
for x in range(len(i)):
	if i[x] != "x":
		m.append((-x,int(i[x])))

part2 = solve(m)
print(part2)