import re

with open("day7.txt", "r") as f:
	i = f.readlines()

r1 = re.compile(r"([a-z\s]+) bags contain ([0-9a-z,\s]+)\.")
r2 = re.compile(r"([0-9]+) ([a-z\s]+) bags?")

graph = {}

for bag in i:
	x = r1.match(bag)
	curr,children = x.group(1),x.group(2)
	if curr not in graph:
		graph[curr] = ({}, {})
	if children != "no other bags":
		for child in children.split(", "):
			y = r2.match(child)
			num,color = y.group(1),y.group(2)
			if color not in graph:
				graph[color] = ({}, {})
			graph[curr][0][color] = int(num)
			graph[color][1][curr] = int(num)

def findparents(bag, graph, acc):
	parents = graph[bag][1]
	if parents:
		for parent in parents:
			if parent not in acc:
				acc = acc.union(findparents(parent, graph, {parent}))
	return acc

part1 = findparents("shiny gold", graph, set())
print(part1)
print(len(part1))

def count(bag, graph, acc):
	children = graph[bag][0]
	if children:
		for child,num in children.items():
			acc += num*count(child, graph, 1)
		return acc
	else:
		return 1

part2 = count("shiny gold", graph, 0)
print(part2)





