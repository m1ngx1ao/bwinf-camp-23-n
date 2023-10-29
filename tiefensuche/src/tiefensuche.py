from input_reader import adjacency_list

def get_neighbors(vertex: int):
	_, edges = adjacency_list()
	return [v_from for v_to, v_from in edges if v_to == vertex]

def is_reachable(v_from: int, v_to: int) -> bool:
	return get_path(v_from, v_to) is not None

def get_path(v_from: int, v_to: int) -> list[int] | None:
	return __get_path(v_from, v_to, set())

def __get_path(v_from: int, v_to: int, visited: set[int]) -> list[int] | None:
	if v_from == v_to:
		return [v_from]
	if v_from in visited:
		return None
	visited.add(v_from)
	for neighbor in get_neighbors(v_from):
		path = __get_path(neighbor, v_to, visited)
		if path is not None:
			return [v_from] + path 
	return None

assert [1, 2, 6] == get_neighbors(7)

assert is_reachable(4, 11)
assert is_reachable(10, 11)

assert get_path(7, 10) == [7, 1, 3, 4, 10]
assert get_path(9, 4) == [9, 3, 4]
assert get_path(7, 13) is None