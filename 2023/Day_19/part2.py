def process_part_txt(string):
	values = string.strip("{}\n").split(",")
	return [int(n) for i,n in (value.split("=") for value in values)]

def process_rule_txt(string):
	key, rules = string.split("{")
	conditions = rules.strip("}\n").split(",")
	workflows[key] = [condition.split(":") for condition in conditions]

# helper function to count 4-tuples
def count_in_ranges(conds):
	# print(conds)
	min_value = 1
	max_value = 4000
	for cond in conds:
		if cond[1]:
			if cond[0][1]==">":
				min_value = max(min_value, int(cond[0][2:])+1)
			else:
				max_value = min(max_value, int(cond[0][2:])-1)
		else:
			if cond[0][1]=="<":
				min_value = max(min_value, int(cond[0][2:]))
			else:
				max_value = min(max_value, int(cond[0][2:]))
	return max_value - min_value + 1

# returns number of 4-tuples of integers that meet restrictions
def count_comb(restrictions):
	x_con, m_con, a_con, s_con = [],[],[],[]
	for con in restrictions:
		match con[0][0]:
			case "x": x_con.append(con)
			case "m": m_con.append(con)
			case "a": a_con.append(con)
			case "s": s_con.append(con)
	how_many = 1
	for specific_letter in [x_con, m_con, a_con, s_con]:
		how_many = how_many*count_in_ranges(specific_letter)
	return how_many

# The driving recursive function
def check_both(workflow, rules_so_far):
	if len(workflow)==1:
		if workflow[0][0] == "R":
			return 0
		elif workflow[0][0] == "A":
			return count_comb(rules_so_far)
		else:
			return check_both(workflows[workflow[0][0]], rules_so_far)
	else:
		rule, target = workflow[0]
		try_false = check_both(workflow[1:],rules_so_far + [[rule, False]])
		if target == "R":
			try_true = 0
		elif target == "A":
			try_true = count_comb(rules_so_far + [[rule,True]])
		else:
			try_true = check_both(workflows[target], rules_so_far + [[rule,True]])
		return try_true + try_false


#parse
workflows = {}
parts = []
with open("input.txt") as file:
	parts_section = False
	for line in file:
		if not line.strip():
			parts_section = True
		elif not parts_section:
			process_rule_txt(line)
		else:
			parts.append(process_part_txt(line))

# go through the binary tree
print(check_both(workflows["in"],[]))


