with open("day3.txt", "r") as f:
	input = [i.strip() for i in f.readlines()]

w,h = len(input[0]),len(input)

def foo(r,d):
	x,y = 0,0
	i = 0
	while y < h:
		if input[y][x] == "#":
			i += 1
		x = (x + r) % w
		y += d
	return i	

a=foo(1,1)
b=foo(3,1) 
c=foo(5,1)
d=foo(7,1)
e=foo(1,2)

print(a,b,c,d,e)
print(a*b*c*d*e)




