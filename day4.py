import re

with open("day4.txt", "r") as f:
	input = ("\n".join(f.readlines())).split("\n\n\n")

hgtr = re.compile(r"^([0-9]+)(cm|in)$")
hclr = re.compile(r"^\#[0-9a-f]{6}$")
eclr = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
pidr = re.compile(r"^[0-9]{9}$")

def hgt(x):
	m = hgtr.match(x)
	if m:
		a,b = m.group(1), m.group(2)
		c = int(a)
		if b == "cm":
			return c >= 150 and c <= 193
		if b == "in":
			return c >= 59 and c <= 76
	else:
		return False

m = {
"byr": lambda x: int(x) >= 1920 and int(x) <= 2002,
"iyr": lambda x: int(x) >= 2010 and int(x) <= 2020,
"eyr": lambda x: int(x) >= 2020 and int(x) <= 2030,
"hgt": hgt,
"hcl": lambda x: hclr.match(x),
"ecl": lambda x: eclr.match(x),
"pid": lambda x: pidr.match(x)
}

r = re.compile(r"([a-z]{3})\:([^\n\s]+)", re.MULTILINE)

def v(i):
	for a,f in m.items():
		if a not in i or not f(i[a]):
			return False
	return True

i = 0

for x in input:
	y = {a:b for a,b in r.findall(x)}
	if v(y):
		i += 1

print(i)



