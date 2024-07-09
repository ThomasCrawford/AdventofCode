
import cmath

class Cart:
    def __init__(self, p, d):
        self.p = p
        self.d = d
        self.r = 0

    def move(self):
        self.p += self.d
        match data[self.p]:
            case "/":
                self.d = -1j *self.d.conjugate()
            case "\\":
                self.d = 1j * self.d.conjugate()
            case "+":
                self.d *= turn[self.r%3]
                self.r +=1

def sort(cart):
    return (cart.p.imag, cart.p.real)

def step(carts):
    carts = sorted(carts, key=sort)
    positions = {}
    for cart in carts:
        positions[cart.p] = cart
    new_carts = []

    while carts:
        cart = carts.pop(0)
        del positions[cart.p]
        cart.move()
        if cart.p in positions:
            carts = [x for x in carts if x.p != cart.p]
            new_carts = [x for x in new_carts if x.p != cart.p]
        else:
            positions[cart.p] = cart
            new_carts.append(cart)
    return new_carts


#position, direction
carts = []

directions = {"v":1j, "^": -1j, "<": -1, ">": 1}
turn = {0: -1j, 1: 1, 2: 1j}

data = {}
with open("input_13.txt") as file:
    for k, line in enumerate(file):
        for i, v in enumerate(line):
            if v in directions:
                carts.append(Cart(i + k *1j, directions[v]))
                v = "|" if v in ["v","^"] else "-"
            data[i+k*1j] = v

#Part 2
while len(carts) >1:
    carts = step(carts)
print(f'Part 2: {int(carts[0].p.real)},{int(carts[0].p.imag)}')
