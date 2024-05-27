import re


def step(p, state, tape):
    v = '0' if p not in tape else tape[p]
    tape[p] = rules[state][v][0]
    if rules[state][v][1] == 'right':
        p += 1
    else:
        p -= 1
    state = rules[state][v][2]
    return p,state,tape




text = ""
rules = {}
with open("input_25.txt") as file:
    for line in file:
        text += line

re_init = r'Begin in state (\w)'
re_count = r'Perform a diagnostic checksum after (\d+) steps'
re_state = (r'In state (\w+):\n' +
                   r'  If the current value is 0:\n' +
                   r'    - Write the value (\d+).\n' +
                   r'    - Move one slot to the (left|right).\n' +
                   r'    - Continue with state (\w+).\n' +
                   r'  If the current value is 1:\n' +
                   r'    - Write the value (\d+).\n' +
                   r'    - Move one slot to the (left|right).\n' +
                   r'    - Continue with state (\w+).')

p = 0
tape = {}
tape[0] = "0"
state = re.findall(re_init,text)[0]
step_count = int(re.findall(re_count,text)[0])
for s in re.findall(re_state,text):
    rules[s[0]] = {}
    rules[s[0]]['0'] = s[1:4]
    rules[s[0]]['1'] = s[4:7]

# print(tape)

for i in range(step_count):
    p, state, tape = step(p,state,tape)

checksum = list(tape.values()).count("1")
print(checksum)


