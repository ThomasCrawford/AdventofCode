
# import pdb

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

def f(board, groups):
	# print (f"Calling f on {board} and {groups}")
	if sum(groups) > len(board) or board.count("#") > sum(groups):
		# print(f"Board is {board} and groups are {groups}, return 0")
		return 0
	if not groups:
		# print (f"Groups are empty, return 1")
		return 1
	if board[0] == ".":
		return f(board[1:],groups)
	elif board[0] == "#":
		if room_for_block(board, groups[0]):
			return f(board[groups[0]+1:],groups[1:])
		else:
			# print(f"Board is {board} and groups are {groups} -- no room!, return 0")
			return 0
	elif board[0] == "?":
		if room_for_block(board, groups[0]): #if ? is a #, is there room for the block? 
			return f(board[1:],groups) + f(board[groups[0]+1:],groups[1:]) #turn the ? into a . or a # (if there's room)
		else:
			return f(board[1:],groups) #just . if there's not room

answer = 0
with open("input.txt") as file:
	for line in file:
		start_board, start_groups = line.split()
		start_groups = [int(x) for x in start_groups.split(",")]
		print(start_board, start_groups, f(start_board,start_groups))
		answer += f(start_board,start_groups)
print(answer)


