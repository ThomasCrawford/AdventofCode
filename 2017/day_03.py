import math, cmath

seed = 361527
# seed = 23

def get_coords(n):
    ring = math.ceil(math.sqrt(n))//2
    remainder = n - (2*ring-1)**2
    side = (remainder -1) // (2*ring)
    r = (remainder -1) % (2*ring)
    if side == 0:
        return ring  + (r - ring +1)*1j
    elif side == 1:
        return ring - r -1  + (ring)*1j
    elif side == 2:
        return - ring  + (ring - r -1)*1j
    elif side == 3:
        return r - ring +1 + (-ring )*1j

def nbhd(z):
    directions = [1, 1 + 1j, 1j, -1 + 1j, -1 , -1 -1j, -1j, 1 -1j]
    return [z+d for d in directions]


def main():
    coords1 = get_coords(seed)
    ans1 = abs(coords1.real) + abs(coords1.imag)
    print(f'Part 1: {int(ans1)}')

    values = {}
    values[0] = 1
    for i in range(2,seed+1):
        coord = get_coords(i)
        v = sum([values[nb] for nb in nbhd(coord) if nb in values])
        values[coord] = v
        if v >= seed:
            print(f'Part 2: {v}')
            quit()
main()
