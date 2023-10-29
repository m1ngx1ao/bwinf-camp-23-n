import copy

# graph data structures (vertices are int)
# v = number of vertices
# e = number of edges

# set of vertices + set of edges
# tuple[set[int], set[tuple[int, int]]]
# ({23, 41, ..., 12}, {(23, 3), (23, 7), (41, 7), (41, 8), ...]}
# Check edge: O(log(e))
# Add vertix without connection: O(log(v))
# Remove vertix: O(log(v) + e)

# list of vertices + matrix of adjacencies
# tuple[list[int], list[list[bool]]]
# ([41, 23], [[False, True], [True, False]])
# Check edge: O(v)
# Add vertix without connection: O(v)
# Remove vertix: O(v)

# for each vertix, list of adjacencies
# {23: {3, 7}, 41: {7, 8}, ...}
# dict[int, set[int]]
# Check edge: O(log(v))
# Add vertix without connection: O(1)
# Remove vertix: O(v * log(v))

#def reader(datei_name):
#	f = open(datei_name)
#	zeilen_str = f.readlines()
#	f.close
#	zeilen_int = []
#	zeilen_int.append([
#		[int(num) for num in zeile_str.rstrip().split(" ")]
#		for zeile_str in zeilen_str
#		])
#	zeilen = zeilen_int[0]
#	return zeilen
#
#def make_matrix():
#	zeilen = reader('input.txt')
#	matrix = [] # list[list[int]]
#	liste = []
#	for _ in range(zeilen[0][0]):						   # trois fois la meme chose?
#		liste.append([])							# trois fois la meme chose?
#	for v in range(zeilen[0][0]):						   # trois fois la meme chose?
#		liste[v] = 0							# trois fois la meme chose?
#	for _ in range(zeilen[0][0]):						   # trois fois la meme chose?
#		matrix.append(copy.deepcopy(liste))
#	for zeile in zeilen[1:]:
#		matrix[zeile[0] - 1][zeile[1] - 1] = matrix[zeile[1] - 1][zeile[0] - 1] = 1
#	return matrix

def get_graph() -> dict[int, set[int]]:
	with open('td-graphen/input.txt', 'r') as f:
		lines = [
			[int(index) for index in line.strip().split(',')]
			for line in f.readlines()
		]
		f.close()
	return {
		line[0]: set(edge for edge in line[1:])
		for line in lines
	}

g = get_graph()
# {23: {3, 7}, 41: {7, 8}, ...}
print(g)