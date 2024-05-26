import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Generator:

    data = []

    @classmethod
    def load_data(cls):
        with open("input_23.txt") as file:
            for line in file:
                line = line.strip().split()
                cls.data.append(line)

    def __init__(self, val = 0):
        self.registers = {}
        self.registers['position'] = 0
        self.terminated = False
        self.mul_count = 0
        for line in Generator.data:
            if not line[1].isnumeric():
                self.registers[line[1]] = 0
        self.registers['a'] = val

    def get_value(self, letter):
        if letter in self.registers:
            return self.registers[letter]
        else:
            return int(letter)

    def step(self,line):
        match line[0]:
            case 'set':
                self.registers[line[1]] = int(self.get_value(line[2]))
            case 'sub':
                self.registers[line[1]] -= self.get_value(line[2])
            case 'mul':
                self.mul_count += 1
                self.registers[line[1]] *= self.get_value(line[2])
            case 'jnz':
                if self.get_value(line[1]) != 0:
                    self.registers['position'] += self.get_value(line[2])
                    if self.registers['position'] >= len(Generator.data):
                        self.terminated = True
                    return self.registers

        self.registers['position'] += 1
        if self.registers['position'] >= len(Generator.data):
            loc = self.registers['position']
            self.terminated = True
        return self.registers

    def run(self):
        while not self.terminated:
            logging.debug(f"{self.registers}")
            l = Generator.data[self.registers['position']]
            self.registers = self.step(l)


Generator.load_data()
gen1 = Generator()
gen1.run()
print(gen1.mul_count)

gen2 = Generator(1)
gen2.run()
print(gen2.registers['h'])


