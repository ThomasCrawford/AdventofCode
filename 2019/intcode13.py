from typing import List

class Intcode:
    def __init__(self,data: List[int], inputs: List[int], idnum = 1):
        self.cursor = 0
        self.inputs = inputs
        self.data = data
        self.data += [0]*10000
        self.active = True
        self.idnum = idnum
        self.offset = 0
        self.output = []
        self.waiting = False

    def step(self):
        code = self.data[self.cursor]
        opcode = code%100

        m1 = (code%1000)//100
        m2 = (code%10000)//1000
        m3 = (code%100000)//10000

        def get_value(mode, index):
            if mode == 1:
                return self.data[self.cursor + index]
            elif mode == 0:
                return self.data[self.data[self.cursor + index]]
            elif mode == 2:
                return self.data[self.data[self.cursor + index] + self.offset] 

        def get_address(mode, index):
            if mode == 1:
                return self.cursor + index
            elif mode == 0:
                return self.data[self.cursor + index]
            elif mode == 2:
                return self.data[self.cursor + index] + self.offset


        if opcode == 1: # Addition
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            address = get_address(m3, 3)
            self.data[address] = d1 + d2
            self.cursor += 4

        elif opcode == 2: # Multiplication
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            address = get_address(m3, 3)
            self.data[address] = d1 * d2
            self.cursor += 4

        elif opcode == 3: # Input
            if self.inputs:
                address = get_address(m1, 1)
                self.data[address] = self.inputs.pop(0)
                self.cursor += 2
            else:
                self.waiting = True

        elif opcode == 4: #Output
            d1 = get_value(m1, 1)
            # print(f'OUTPUT: {d1}')
            self.output.append(d1)
            self.cursor += 2

        elif opcode == 5: #Jump if True
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            if d1 != 0:
                self.cursor = d2
            else:
                self.cursor += 3

        elif opcode == 6: #Jump if False
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            if d1 == 0:
                self.cursor = d2
            else:
                self.cursor += 3

        elif opcode == 7: # Less than
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            address = get_address(m3, 3)
            self.data[address] = 1 if d1 < d2 else 0
            self.cursor += 4

        elif opcode == 8: # Equals
            d1 = get_value(m1, 1)
            d2 = get_value(m2, 2)
            address = get_address(m3, 3)
            self.data[address] = 1 if d1 == d2 else 0
            self.cursor += 4

        elif opcode == 9: # Adjust relative base
            d1 = get_value(m1, 1)
            self.offset += d1
            self.cursor += 2

        elif opcode == 99:
            # print(self.output)
            # print(f"Bot {self.idnum} no longer active")
            self.active = False

        else:
            raise Exception(f'Opcode error: {opcode}')

    def run(self):
        self.waiting = False
        while not self.waiting and self.active:
            self.step()
        if not self.active:
            return False
        out = list(self.output)
        self.output = []
        return out

    def input(self, x):
        self.inputs.append(x)

