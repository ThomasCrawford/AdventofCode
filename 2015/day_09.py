from functools import lru_cache
import networkx as nx
import matplotlib.pyplot as plt


def add_info(a,b,d):
	if a not in dists:
		dists[a] = dict()
	dists[a][b] = d

dists = {}
with open("input_09.txt") as file:
	for line in file:
		locs, d = line.strip().split(' = ')
		d = int(d)
		a, b = locs.split(' to ')
		add_info(a,b,d)
		add_info(b,a,d)


cache = set()

@lru_cache
def f(p, remaining):
	if not remaining:
		return 0
	else:
		poss = [ dists[p][new_p] + \
				f(new_p, tuple([x for x in remaining if x != new_p])) \
				for new_p in remaining]
		out = min(poss)
		return out

@lru_cache
def f2(p, remaining):
	if not remaining:
		return 0
	else:
		poss = [ dists[p][new_p] + \
				f2(new_p, tuple([x for x in remaining if x != new_p])) \
				for new_p in remaining]
		out = max(poss)
		return out


answer = min([f(p, tuple([x for x in dists if x != p])) for p in dists])
answer2 = max([f2(p, tuple([x for x in dists if x != p])) for p in dists])

print(f'Part 1: {answer}')
print(f'Part 2: {answer2}')

