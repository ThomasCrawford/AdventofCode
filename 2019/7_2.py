from itertools import permutations

class Amp:
    def __init__(self,in1, idnum):
        self.cursor = 0
        self.inputs = [in1]
        with open("input7.txt") as file:
            for line in file:
                self.data = [int(x) for x in line.strip().split(',')]
        self.active = True
        self.idnum = idnum


    def set_target(self, other):
        self.target = other

    def step(self):
        code = self.data[self.cursor]
        opcode = code%100

        try:
            i = self.cursor + 1 if (code%1000)//100 == 1 else self.data[self.cursor + 1]
            d1 = self.data[i]
        except IndexError:
            pass
        try:
            i = self.cursor + 2 if (code%10000)//1000 == 1 else self.data[self.cursor + 2]
            d2 = self.data[i]
        except IndexError:
            pass
        try:
            i = self.cursor + 3 if (code%100000)//10000 == 1 else self.data[self.cursor + 3]
            d3 = self.data[i]
        except IndexError:
            pass

        if opcode == 1:
            self.data[self.data[self.cursor + 3]] = d1 + d2
            self.cursor += 4
        elif opcode == 2:
            self.data[self.data[self.cursor + 3]] = d1 * d2
            self.cursor += 4
        elif opcode == 3: # Input
            if self.inputs:
                self.data[self.data[self.cursor + 1]] = self.inputs.pop(0)
                self.cursor += 2
        elif opcode == 4: #Output
            self.target.inputs.append(d1)
            self.cursor += 2
        elif opcode == 5: #Jump if True
            if d1:
                self.cursor = d2
            else:
                self.cursor += 3
        elif opcode == 6: # Jump if False
            if not d1:
                self.cursor = d2
            else:
                self.cursor += 3
        elif opcode == 7: # Less than
            self.data[self.data[self.cursor + 3]] = 1 if d1 < d2 else 0
            self.cursor += 4
        elif opcode == 8: # Equals
            self.data[self.data[self.cursor + 3]] = 1 if d1 == d2 else 0
            self.cursor += 4
        elif opcode == 99:
            self.active = False
        else:
            raise Exception(f'Opcode error: {opcode}')


def calc_thrust(sequence):
    amps = {}
    for i,x in enumerate(sequence):
        amps[i] = Amp(x, i)
    amps[0].inputs.append(0) # first amp gets input 0
    for i in amps:
        amps[i].target = amps[(i+1)%5]

    while amps[4].active:
        for i in range(5):
            if amps[i].active:
                amps[i].step()

    return amps[0].inputs[0]



possible = [calc_thrust(x) for x in permutations(range(5,10))]
print(max(possible))