with open("day23.txt", "r") as f:
	i = [int(x) for x in f.readline()]

def play(n,cs):
	m = dict(zip(cs,[cs[(x+1)%len(cs)]for x in range(len(cs))]))
	z = cs[0]
	l=len(cs)
	for _ in range(n):
		a=m[z]
		b=m[a]
		c=m[b]
		d=z-1
		while d in [a,b,c,0]:
			d=l if d==0 else d-1
		m[z],m[d],m[c]=m[c],a,m[d]
		z=m[z]
	return m

r1=play(100,[x for x in i])
part1=""
x=r1[1]
while x!=1:
	part1+=str(x)
	x=r1[x]
print(part1)

r2=play(10000000,i+list(range(len(i)+1,1000001)))
a=r2[1]
b=r2[a]
part2=a*b
print(a,b,part2)


