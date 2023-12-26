import numpy as np
from scipy.optimize import minimize


def minimum_distance_between_lines(stone1, stone2):
    a1, d1 = stone1
    a2, d2 = stone2
    cross_prod = np.cross(d1, d2)
    numerator = np.abs(np.dot(a2 - a1, cross_prod))
    denominator = np.linalg.norm(cross_prod)
    # Handle the case when lines are parallel (denominator is zero)
    if denominator == 0:
        return np.linalg.norm(np.cross(a2 - a1, d1)) / np.linalg.norm(d1)
    return numerator / denominator


data = []
with open('input.txt') as file:
    for line in file:
        p , d = line.strip().split('@')
        p = np.array([int(x) for x in p.strip().split(',')])
        d = np.array([int(x) for x in d.strip().split(',')])
        data.append([p,d])
height = len(data)


def shift_by(stone, d_shift):
    p, d = stone
    return [p,d+d_shift]

# rock_d = np.array([1,1,1])
def func(d):
    rock_d = np.array(d)
    for i, stone in enumerate(data):
        for other_stone_index in range(i+1,height):
            other_stone = data[other_stone_index]
            return minimum_distance_between_lines(shift_by(stone,rock_d), shift_by(other_stone,rock_d))

root = minimize(func,[0,0,0])
print(root.message)
print(root.x)
print(func(root.x))

# def f(rock):
#     x0, y0, z0, dx0, dy0, dz0 = rock
#     rock = [np.array([x0,y0,z0]),np.array([dx0,dy0,dz0])]
#     error = 0
#     for stone in data:
#         error += minimum_distance_between_lines(rock, stone)**2
#     return error



# root = minimize(f,[319768494554521,319768494554521,319768494554521,947991376007,947991376007,947991376007], method = 'BFGS')
# print(root.message)
# print(root.x)
# print(f(root.x))

# root = minimize(f,[1,1,1,1,1,1], method = 'CG')
# print(root.x)
# print(f([1,1,1,1,1,1]))
# print(f(root.x))

# print(f([24, 13, 10,-3, 1, 2]))
# print(f([-99,54,92,7.751,-2.584,-5.168]))


