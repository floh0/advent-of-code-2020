with open("day25.txt", "r") as f:
	c = int(f.readline())
	d = int(f.readline())

clf,dlf = False,False
v,i = 1,1
while not clf or not dlf:
	v = (v*7)%20201227
	if v == c:
		cl,clf = i,True
	if v == d:
		dl,dlf = i,True
	i += 1

v = 1
for i in range(dl):
	v = (v*c)%20201227
print(v)
v = 1
for i in range(cl):
	v = (v*d)%20201227
print(v)