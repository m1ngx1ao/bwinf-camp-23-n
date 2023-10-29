colors = ['rot', 'tuerkis', 'rosa', 'gelb', 'blau', 'orange', 'gruen']

neighbors = {
	0: {1, 2, 4},
	1: {0, 3, 4, 6},
	2: {0, 4, 5, 7},
	3: {1, 6},
	4: {0, 1, 2, 6, 7, 8},
	5: {2, 7},
	6: {1, 3, 4, 8},
	7: {2, 4, 5, 8},
	8: {4, 6, 7},
}

def get_score(beet: tuple[str, ...], score_combinations: dict[tuple[str, str], int]) -> int:
	punktzahl = 0
	for index_first, color_first in enumerate(beet):
		nachbarn = neighbors[index_first]
		for index_second in nachbarn:
			t = (color_first, beet[index_second])
			if t in score_combinations:
				punktzahl += score_combinations[t]
	return punktzahl

def printout(beet: tuple[str, ...]):
	empty = '          '
	padded_beet = [
		(empty + b + empty)[
			(len(empty) + len(b)) // 2:(len(empty) + len(b)) // 2 + len(empty)
		]
		for b in beet
	]
	print(empty + ' ' + empty + '/' + padded_beet[0] + '\\')
	print(empty + '/' + padded_beet[1] + ' ' + empty + ' ' + padded_beet[2] + '\\')
	print(padded_beet[3] + ' ' + empty + ' ' + padded_beet[4] + ' ' + empty + ' ' + padded_beet[5])
	print(empty + '\\' + padded_beet[6] + ' ' + empty + ' ' + padded_beet[7] + '/')
	print(empty + ' ' + empty + '\\' + padded_beet[8] + '/')