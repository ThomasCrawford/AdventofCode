source = "input9.txt"

class Amp:
    def __init__(self,in1, idnum):
        self.cursor = 0
        self.inputs = [in1]
        with open(source) as file:
            for line in file:
                self.data = [int(x) for x in line.strip().split(',')]
        self.data += [0]*10000
        self.active = True
        # self.idnum = idnum
        self.offset = 0

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

        elif opcode == 4: #Output
            d1 = get_value(m1, 1)
            print(f'OUTPUT: {d1}')
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
            self.active = False

        else:
            raise Exception(f'Opcode error: {opcode}')

a = Amp(1,1)
while a.active:
    a.step()


a = Amp(2,1)
while a.active:
    a.step()
