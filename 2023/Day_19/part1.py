def process_part_txt(string):
	values = string.strip("{}\n").split(",")
	return [int(n) for i,n in (value.split("=") for value in values)]

def process_rule_txt(string):
	key, rules = string.split("{")
	conditions = rules.strip("}\n").split(",")
	workflow[key] = [condition.split(":") for condition in conditions]

def step(loc,part):
	x,m,a,s = part
	for con,result in workflow[loc][:-1]:
		if eval(con): return result
	return workflow[loc][-1][0]
def check(part):
	loc = "in"
	while loc != "A" and loc != "R":
		loc = step(loc,part)
	if loc == "A":
		return True
	elif loc == "R":
		return False
	else:
		raise Exception(f"workflow finished at {loc} rather than A or R")



workflow = {}
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

answer = 0
for part in parts:
	if check(part):
		print(part)
		answer += sum(part)
print(answer)

