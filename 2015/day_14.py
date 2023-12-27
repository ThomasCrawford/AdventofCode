import re

time = 2503

def how_far(speed, dur, rest, time):
    cycle = dur + rest
    dist_per_cycle = speed*dur 
    cycles = time // cycle
    # print(speed, dur, rest, time, cycle, dist_per_cycle, cycles, cycles*dist_per_cycle, )
    return cycles*dist_per_cycle + min(dur, time%cycle)*speed


regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

data = []
with open("input_14.txt") as file:
    for line in file:
        name, speed, duration, rest = re.match(regex, line.strip()).groups()
        data.append([name, int(speed), int(duration), int(rest)])
names = list(set([x[0] for x in data]))


times = []
for deer in data:
    name, speed, duration, rest = deer
    d = how_far(speed, duration, rest, time)
    times.append(d)
print(f'Part 1: {max(times)}')




## Part 2:
# deer = [name, speed, duration, rest, position, score]


for deer in data:
    deer.append(0)
    deer.append(0)


for i in range(time):
    for deer in data:
        if i%(deer[2]+deer[3]) < deer[2]:
            deer[4] += deer[1]
    furthest = max([deer[4] for deer in data])
    for deer in data:
        if deer[4] == furthest:
            deer[5] += 1

print(f'Part 2: {max([deer[5] for deer in data])}')