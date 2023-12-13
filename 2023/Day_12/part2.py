import functools as ft


def room_for_block(board, block):
	if len(board) == block:
		if "." not in board:
			return True
		else:
			return False
	elif "." not in board[: block] and board[block] != "#":
		return True
	else:
		return False

@ft.lru_cache(maxsize=1000)
def f(board, groups):
	# if dimensions don't line up, no possible solution
	if sum(groups) > len(board) or board.count("#") > sum(groups):
		return 0

	# if there's nothing left to add, we're done, 1 solution
	if not groups:
		return 1

	# starting with a . is identical to skipping it	
	if board[0] == ".":
		return f(board[1:],groups)

	# if we start with a #, the next group has to be at the start, provided it fits
	elif board[0] == "#":
		if room_for_block(board, groups[0]):
			return f(board[groups[0]+1:],groups[1:])
		else:
			return 0

	#if we start with a ?, it could go either way, so check both
	elif board[0] == "?":
		if room_for_block(board, groups[0]): #if ? is a #, is there room for the block? 
			return f(board[1:],groups) + f(board[groups[0]+1:],groups[1:]) #turn the ? into a . or a # (if there's room)
		else:
			return f(board[1:],groups) #just . if there's not room

answer = 0
with open("input.txt") as file:
	for line in file:
		start_board, start_groups = line.split()
		start_board = "?".join([start_board]*5)
		start_groups = tuple([int(x) for x in start_groups.split(",")]*5)
		answer += f(start_board,start_groups)

print(answer)


