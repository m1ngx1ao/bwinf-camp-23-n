def building_roads() -> tuple[list[int], list[tuple[int, int]]]:
	with open('td-tiefensuche/input/building_roads_input.txt', 'r') as f:
		zeilen = [
			[int(e) for e in zeile.rstrip().split(' ')]
			for zeile in f.readlines()
		]
		f.close()
	knoten = list(range(1, zeilen[0][0] + 1))
	kanten = [(von, bis) for von, bis in zeilen[1:]]
	return (knoten, kanten)

# ([1, 2, ..., 12], [(1, 3), (1, 7), (2, 7), (2, 8), ...])
def adjacency_list() -> tuple[list[int], list[tuple[int, int]]]:
	# duggy time
	with open('td-tiefensuche/input/tiefensuche_input.txt') as f:
		lines = [
			[int(s) for s in line.strip().split(',')]
			for line in f.readlines()
		]
		f.close()
	vertices = [v for v, *_ in lines]
	edges = [
		(von, bis)
		for von, *bises in lines
		for bis in bises
	]
	return (vertices, edges)

#print(building_roads())
#print(adjacency_list())