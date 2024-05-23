import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class Generator:

    data = []

    @classmethod
    def load_data(cls):
        with open("input_18.txt") as file:
            for line in file:
                line = line.strip().split()
                cls.data.append(line)

    reg = {}
    condition = threading.Condition()

    def __init__(self,gen_id):
        self.registers = {}
        self.registers['position'] = 0
        self.buffer = []
        self.id = gen_id
        self.send_count = 0
        self.receive_count = 0
        self.terminated = False
        self.waiting = False
        Generator.reg[self.id] = self
        for line in Generator.data:
            if not line[1].isnumeric():
                self.registers[line[1]] = 0
        self.registers['p'] = self.id

    def set_target(self,other_gen):
        self.target = Generator.reg[other_gen]

    def receive(self, value):
        with Generator.condition:
            self.buffer.append(value)

    def get_value(self, letter):
        if letter in self.registers:
            return self.registers[letter]
        else:
            return int(letter)

    def get_from_buffer(self):
        with Generator.condition:
            self.waiting = True
            while not self.buffer:
                if all([gen.waiting or gen.terminated for gen in Generator.reg.values()]):
                    self.terminated = True
                    Generator.condition.notify_all()
                    return None
                Generator.condition.wait()
            self.waiting = False
            return self.buffer.pop(0)

        

    def step(self,line):
        match line[0]:
            case 'set':
                self.registers[line[1]] = int(self.get_value(line[2]))
            case 'add':
                self.registers[line[1]] += self.get_value(line[2])
            case 'mul':
                self.registers[line[1]] *= self.get_value(line[2])
            case 'mod':
                self.registers[line[1]] %= self.get_value(line[2])
            case 'jgz':
                if self.get_value(line[1]) > 0:
                    self.registers['position'] += self.get_value(line[2])
                    if self.registers['position'] >= len(Generator.data):
                        self.terminated = True
                    return self.registers
            case 'snd':
                with Generator.condition:
                    self.target.receive(self.get_value(line[1]))
                    self.send_count += 1
                    Generator.condition.notify_all()
            case 'rcv':
                with Generator.condition:
                    self.receive_count +=1
                    buffer_value = self.get_from_buffer()
                    if buffer_value:
                        self.registers[line[1]] = buffer_value

        self.registers['position'] += 1
        if self.registers['position'] >= len(Generator.data):
            loc = self.registers['position']
            self.terminated = True
        return self.registers

    def run(self):
        while not self.terminated:
            logging.debug(f"Generator {self.id} executing at position {self.registers['position']}")
            l = Generator.data[self.registers['position']]
            self.registers = self.step(l)


Generator.load_data()
gen0 = Generator(0)
gen1 = Generator(1)
gen0.set_target(1)
gen1.set_target(0)

thread0 = threading.Thread(target = gen0.run)
thread1 = threading.Thread(target = gen1.run)

thread0.start()
thread1.start()

thread0.join()
thread1.join()


print(gen1.send_count)




