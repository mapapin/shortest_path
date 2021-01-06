import os

i = 0
global row
row = []
n = int(input("Please type number of rows : "))
while i < n:
	row.append(list(input()))
	i += 1


def	print_slt(ret):
	global row
	solution = list(row)
	for i, elem in enumerate(ret.list_coord):
		if i != 0:
			solution[elem[0]][elem[1]] = '+'
	os.system('clear')
	for ligne in solution:
			for case in ligne:	
				if case == '0':
					print(f"\033[32m.\033[39m", end='')
				if case == '#':
					print(f"\033[33m{case}\033[39m", end='')
				if case == '.':
					print(case, end='')
				if case == 'B':
					print(f"\033[34m{case}\033[39m", end='')
				if case == 'A':
					print(f"\033[34m{case}\033[39m", end='')
				if case == '+':
					print(f"\033[31m{case}\033[39m", end='')
			print('')

	



def	find_child():
	global row
	y = 0
	while y < len(row):
		x = 0
		while x < len(row[0]):
			if row[y][x] == 'A':
				return ([y, x])
			x += 1
		y += 1
	return None





class	Node:
	def __init__(self):
		self.dist = 0
		self.coord = [0, 0]
		self.list_coord = []






def	expend(current):

	global row

	ret = []	

	if (current.coord[0] != 0):
		if row[current.coord[0] - 1][current.coord[1]] == '.' or row[current.coord[0] - 1][current.coord[1]] == 'B':
			new = Node()
			new.dist = current.dist + 1
			new.coord = [current.coord[0] - 1, current.coord[1]]
			ret.append(new)
			new.list_coord = list(current.list_coord)
			new.list_coord.append(current.coord)
			if row[current.coord[0] - 1][current.coord[1]] != 'B':
				row[current.coord[0] - 1][current.coord[1]] = '0'
	if (current.coord[0] < len(row) - 1):
		if row[current.coord[0] + 1][current.coord[1]] == '.' or row[current.coord[0] + 1][current.coord[1]] == 'B':
			new = Node()
			new.dist = current.dist + 1
			new.coord = [current.coord[0] + 1, current.coord[1]]
			ret.append(new)
			new.list_coord = list(current.list_coord)
			new.list_coord.append(current.coord)
			if row[current.coord[0] + 1][current.coord[1]] != 'B':
				row[current.coord[0] + 1][current.coord[1]] = '0'
	if (current.coord[1] != 0):
		if row[current.coord[0]][current.coord[1] - 1] == '.' or row[current.coord[0]][current.coord[1] - 1] == 'B':
			new = Node()
			new.dist = current.dist + 1
			new.coord = [current.coord[0], current.coord[1] - 1]
			ret.append(new)
			new.list_coord = list(current.list_coord)
			new.list_coord.append(current.coord)
			if row[current.coord[0]][current.coord[1] - 1] != 'B':
				row[current.coord[0]][current.coord[1] - 1] = '0'
	if (current.coord[1] < len(row) - 1):
		if row[current.coord[0]][current.coord[1] + 1] == '.' or row[current.coord[0]][current.coord[1] + 1] == 'B':
			new = Node()
			new.dist = current.dist + 1
			new.coord = [current.coord[0], current.coord[1] + 1]
			ret.append(new)
			new.list_coord = list(current.list_coord)
			new.list_coord.append(current.coord)
			if row[current.coord[0]][current.coord[1] + 1] != 'B':
				row[current.coord[0]][current.coord[1] + 1] = '0'

	return (ret)	






def bfs(begin):
	global row
	q = []
	new = Node()
	new.coord = begin
	q.append(new)
	while q:
		node = q.pop(0)
		if row[node.coord[0]][node.coord[1]] == 'B':
			return node
		else:
			for elem in expend(node):
				q.insert(len(q), elem)
	return None







begin = find_child()
ret = bfs(begin)







if ret == None:
	print("No solution")
else:
	print_slt(ret)
