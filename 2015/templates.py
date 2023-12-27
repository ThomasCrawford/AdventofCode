import re

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

data = []
with open("input_00.txt") as file:
    for line in file:
        name, speed, duration, rest = re.match(regex, line.strip()).groups()


