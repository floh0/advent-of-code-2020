with open("day17.txt", "r") as f:
	i = "".join(f.readlines()).split("\n")

m = [[1 if y == "#" else 0 for y in x] for x in i]

def init3d(i):
	m = {}
	for y in range(len(i)):
		for x in range(len(i[y])):
			if x not in m:
				m[x] = {}
			if y not in m[x]:
				m[x][y] = {}
			m[x][y][0] = 1 if i[y][x] == "#" else 0
	return m

def expand3d(m):
	mc = {k:{kk:{kkk:vvv for kkk,vvv in vv.items()} for kk,vv in v.items()} for k,v in m.items()}
	for x,r in m.items():
		for y,rr in r.items():
			for z,rrr in rr.items():
				if rrr == 1:
					for a in [-1,0,1]:
						for b in [-1,0,1]:
							for c in [-1,0,1]:
								xa = x+a
								yb = y+b
								zc = z+c
								if xa not in mc:
									mc[xa] = {}
								if yb not in mc[xa]:
									mc[xa][yb] = {}
								if zc not in mc[xa][yb]:
									mc[xa][yb][zc] = 0

	return mc

def iter3d(m):
	mc = {k:{kk:{kkk:vvv for kkk,vvv in vv.items()} for kk,vv in v.items()} for k,v in m.items()}
	for x,r in m.items():
		for y,rr in r.items():
			for z,rrr in rr.items():
				n = 0
				for a in [-1,0,1]:
					for b in [-1,0,1]:
						for c in [-1,0,1]:
							if a != 0 or b != 0 or c != 0:
								xa = x+a
								yb = y+b
								zc = z+c
								if xa in m and yb in m[xa] and zc in m[xa][yb]:
									n += m[xa][yb][zc]
				if rrr == 0:
					if n == 3:
						mc[x][y][z] = 1
					else:
						mc[x][y][z] = 0
				if rrr == 1:
					if n == 2 or n == 3:
						mc[x][y][z] = 1
					else:
						mc[x][y][z] = 0
	return mc

def sum3d(m):
	return sum([vvv for _,v in m.items() for _,vv in v.items() for _,vvv in vv.items()])

def init4d(i):
	m = {}
	for y in range(len(i)):
		for x in range(len(i[y])):
			if x not in m:
				m[x] = {}
			if y not in m[x]:
				m[x][y] = {}
			if 0 not in m[x][y]:
				m[x][y][0] = {}
			m[x][y][0][0] = 1 if i[y][x] == "#" else 0
	return m

def expand4d(m):
	mc = {k:{kk:{kkk:{kkkk:vvvv for kkkk,vvvv in vvv.items()} for kkk,vvv in vv.items()} for kk,vv in v.items()} for k,v in m.items()}
	for x,r in m.items():
		for y,rr in r.items():
			for z,rrr in rr.items():
				for w,rrrr in rrr.items():
					if rrrr == 1:
						for a in [-1,0,1]:
							for b in [-1,0,1]:
								for c in [-1,0,1]:
									for d in [-1,0,1]:
										xa = x+a
										yb = y+b
										zc = z+c
										wd = w+d
										if xa not in mc:
											mc[xa] = {}
										if yb not in mc[xa]:
											mc[xa][yb] = {}
										if zc not in mc[xa][yb]:
											mc[xa][yb][zc] = {}
										if wd not in mc[xa][yb][zc]:
											mc[xa][yb][zc][wd] = 0

	return mc

def iter4d(m):
	mc = {k:{kk:{kkk:{kkkk:vvvv for kkkk,vvvv in vvv.items()} for kkk,vvv in vv.items()} for kk,vv in v.items()} for k,v in m.items()}
	for x,r in m.items():
		for y,rr in r.items():
			for z,rrr in rr.items():
				for w,rrrr in rrr.items():
					n = 0
					for a in [-1,0,1]:
						for b in [-1,0,1]:
							for c in [-1,0,1]:
								for d in [-1,0,1]:
									if a != 0 or b != 0 or c != 0 or d != 0:
										xa = x+a
										yb = y+b
										zc = z+c
										wd = w+d
										if xa in m and yb in m[xa] and zc in m[xa][yb] and wd in m[xa][yb][zc]:
											n += m[xa][yb][zc][wd]
					if rrrr == 0:
						if n == 3:
							mc[x][y][z][w] = 1
						else:
							mc[x][y][z][w] = 0
					if rrrr == 1:
						if n == 2 or n == 3:
							mc[x][y][z][w] = 1
						else:
							mc[x][y][z][w] = 0
	return mc

def sum4d(m):
	return sum([vvvv for _,v in m.items() for _,vv in v.items() for _,vvv in vv.items() for _,vvvv in vvv.items()])

def solve(i,n,init,iter,expand,sum):
	m=init(i)
	for _ in range(n):
		m = iter(expand(m))
	return sum(m)

print(solve(i,6,init3d,iter3d,expand3d,sum3d))
print(solve(i,6,init4d,iter4d,expand4d,sum4d))

