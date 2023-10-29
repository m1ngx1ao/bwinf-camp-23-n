import itertools as it
import beet as bt

def get_best(colors: set[str], minimum_colors: set[str],
		score_combinations: dict[tuple[str, str], int]) -> tuple[int, tuple[str, ...]]:
	BEET_SIZE = 9
	beet = ['???'] * BEET_SIZE
	other_colors = {c for c in colors if c not in minimum_colors}
	highscore = -1
	highscore_beet = tuple(beet)
	counter = 0
	for minimum_colors_pos in it.combinations(range(BEET_SIZE), r=len(minimum_colors)):
		candidates_pos = [bi for bi in range(BEET_SIZE) if bi not in minimum_colors_pos]
		for mc_permutation in it.permutations(minimum_colors):
			candidates = [
				list(other_colors)
				for _ in range(len(candidates_pos))
			]
			for mc_p, mcp_c in zip(minimum_colors_pos, mc_permutation):
				beet[mc_p] = mcp_c
				for oci, occ in zip(candidates_pos, candidates):
					if oci > mc_p:
						occ.append(mcp_c)
			for candidate_colors in it.product(*candidates):
				counter += 1
				if counter % 100_000 == 0:
					print(f'... {counter / 1_000_000}M tries ...')
				for cc_p, cc in zip(candidates_pos, candidate_colors):
					beet[cc_p] = cc
				beet_tuple = tuple(beet)
				s = bt.get_score(beet_tuple, score_combinations)
				if s > highscore:
					highscore = s
					highscore_beet = beet_tuple
					print(highscore)
					bt.printout(highscore_beet)
	print(f'Iterations: {counter}')
	return (highscore, highscore_beet)

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