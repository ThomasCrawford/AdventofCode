import cmath


def new_position(cart):
    p, d, r = cart
    p += d
    match data[p]:
        case "/":
            d = -1j * d.conjugate()
        case "\\":
            d = 1j * d.conjugate()
        case "+":
            d *= turn[r%3]
            r +=1
    return [p,d,r]

#Step function for part 1
def step(carts):
    new_carts = []
    positions = set(cart[0] for cart in carts)
    for cart in sorted(carts, key=sort):
        positions.remove(cart[0])
        new_cart = new_position(cart)
        if new_cart[0] in positions:
            raise Exception(int(new_cart[0].real), int(new_cart[0].imag))
        positions.add(new_cart[0])
        new_carts.append(new_cart)
    return new_carts


def sort(cart):
    return (cart[0].imag, cart[0].real)

#position, direction
carts = []

directions = {"v":1j, "^": -1j, "<": -1, ">": 1}
turn = {0: -1j, 1: 1, 2: 1j}


data = {}
with open("input_13.txt") as file:
    for k, line in enumerate(file):
        for i, v in enumerate(line):
            if v in directions:
                carts.append([i + k *1j, directions[v], 0])
                if v in ["v", "^"]:
                    v = "|"
                else:
                    v = "-"
            data[i+k*1j] = v

#Part 1
try:
    for i in range(1000):
        carts = step(carts)
except Exception as e:
    print(f'Part 1: {e}')

