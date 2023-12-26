import re

def parse_instruction(instruction):
	assignment_regex = r'(\d+) -> (\w+)'
	reassignment_regex = r'(\w+) -> (\w+)'
	bitwise_regex = r'(\w+) (AND|OR) (\w+) -> (\w+)'
	shift_regex = r'(\w+) (LSHIFT|RSHIFT) (\d+) -> (\w+)'
	not_regex = r'NOT (\w+) -> (\w+)'
	one_and_regex = r'1 AND (\w+) -> (\w+)'

	if re.match(assignment_regex, instruction):
		value, wire = re.match(assignment_regex, instruction).groups()
		return {'w_type': 'assignment', 'value': int(value), 'operands': [], 'wire': wire}
	elif re.match(one_and_regex, instruction):
		operand, wire = re.match(one_and_regex, instruction).groups()
		return {'w_type': 'one_and', 'operands': [operand], 'wire': wire}
	elif re.match(reassignment_regex, instruction):
		operand, wire = re.match(reassignment_regex, instruction).groups()
		return {'w_type': 'reassignment', 'operands': [operand], 'wire': wire}
	elif re.match(bitwise_regex, instruction):
		operand1, operation, operand2, wire = re.match(bitwise_regex, instruction).groups()
		return {'w_type': 'bitwise', 'operation': operation, 'operands': [operand1, operand2], 'wire': wire}
	elif re.match(shift_regex, instruction):
		operand, operation, value, wire = re.match(shift_regex, instruction).groups()
		return {'w_type': 'shift', 'operation': operation, 'operands': [operand], 'value': int(value), 'wire': wire}
	elif re.match(not_regex, instruction):
		operand, wire = re.match(not_regex, instruction).groups()
		return {'w_type': 'not', 'operands': [operand], 'wire': wire}
	
	else:
		raise ValueError(f"Invalid instruction format {instruction}")

def evaluate(direction):
	match direction['w_type']:
		case 'assignment':
			return direction['value']
		case 'reassignment':
			return done[direction['operands'][0]]

		case 'bitwise':
			match direction['operation']:
				case 'AND':
					return done[direction['operands'][0]] & done[direction['operands'][1]]
				case 'OR':
					return done[direction['operands'][0]] | done[direction['operands'][1]]
		case 'shift':
			match direction['operation']:
				case 'LSHIFT':
					# print(direction)
					# print(done[direction['operands'][0]])
					return done[direction['operands'][0]] << direction['value']
				case 'RSHIFT':
					return done[direction['operands'][0]] >> direction['value']
		case 'not':
			return (~done[direction['operands'][0]])%2**16
		case 'one_and':
			return (1&done[direction['operands'][0]])


data = []
done = {}

with open("input_07.txt") as file:
	for line in file:
		data.append(line.strip())

while 'a' not in done:
	for instruction in data:
		direction = parse_instruction(instruction)
		if all([x in done for x in direction['operands']]):
			done[direction['wire']] = evaluate(direction)
			data.remove(instruction)

part1 = done['a']
print(f'Part 1: {part1}')

data = []
done = {}

with open("input_07.txt") as file:
	for line in file:
		data.append(line.strip())

data = [line if line[-2:]!= ' b' else str(part1) + ' -> b'for line in data]		

while 'a' not in done:
	for instruction in data:
		direction = parse_instruction(instruction)
		if all([x in done for x in direction['operands']]):
			done[direction['wire']] = evaluate(direction)
			data.remove(instruction)

part2 = done['a']
print(f'Part 2: {part2}')



