import itertools as it
import beet as bt

def get_best(colors: set[str], minimum_colors: set[str],
		score_combinations: dict[tuple[str, str], int]) -> tuple[int, tuple[str, ...]]:
	highscore = 0
	best_beet = ()
	c = 0
	for beet in it.product(colors, repeat=9):
		if all(color in beet for color in minimum_colors):
			c += 1
			if c % 100_000 == 0:
				print(f'{c/1_000_000}M')
			result = bt.get_score(beet, score_combinations)
			if result > highscore:
				highscore = result
				best_beet = beet
				print(highscore)
				bt.printout(best_beet)
	return (highscore, best_beet)
			
cs = set(bt.colors)
min_cols = set(bt.colors[:5])
sc_comb = {
	('rot', 'tuerkis'): 3,
	('rot', 'gruen'): 1,
}
 
def doit():
	score, beet = get_best(cs, min_cols, sc_comb)
	print(score)
	bt.printout(beet)

doit()