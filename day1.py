with open("day1.txt", "r") as f:
	t = [int(i) for i in f.readlines()]

def foo(t, f):
	while len(t) > 0:
		h, t = t[0], t[1:]
		for e in t:
			if f(h,e):
				return h, e

while len(t) > 0:
	h, t = t[0], t[1:]
	x = foo(t, lambda x,y: x+y+h == 2020)
	if x:
		(b,c) = x
		print(h,b,c)
		print(h*b*c)


