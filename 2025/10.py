import re
import itertools


def is_valid1(indicator, buttonset):
    for i,light in enumerate(indicator[0]):
        count = len([x for x in buttonset if i in x])
        if light == "." and count%2==1:
            return False
        elif light == "#" and count%2==0:
            return False
    return True


def min_presses1 (line):
    indicator,buttons,_ = line
    for press_count in range(len(indicator[0])+1):
        for buttonset in itertools.combinations(buttons,press_count):
            if is_valid1(indicator, buttonset):
                return press_count
    raise ValueError(f"Failed to find solution in {line}")

data = []
with open("10.txt") as file:
    for line in file:
        indicator = re.findall(r'\[([.#]+)\]', line)
        buttons = [[int(x) for x in button.split(",")] for button in re.findall(r'\((.*?)\)',line)]
        joltage = [int(x) for x in re.findall(r'\{(.*?)\}',line)[0].split(",")]
        data.append([indicator,buttons,joltage])


ans1 = sum([min_presses1(line) for line in data])
print(ans1)

#Part 2
import sympy as sp


def solve_matrix(line):
    _, buttons, joltage = line
    A = []
    for i in range(len(joltage)):
        A.append([1 if i in x else 0 for x in buttons ])
    A=sp.Matrix(A)
    b=sp.Matrix(joltage)
    m, n = A.shape

    x = sp.symbols(f'x0:{n}')

    sol, = list(sp.linsolve((A, b),x))
    free_vars = list(sol.free_symbols)
    vec = sp.lambdify(free_vars, sol, "math")
    best = float("inf")


    values_to_try = itertools.product(range(max(joltage)+1), repeat=len(free_vars))
    for values in values_to_try:
        candidate = vec(*values)
        if any(c < -0.0001 for c in candidate):
            continue
        if any(abs(c-round(c)) > 0.0001 for c in candidate):
            continue
        if sum(candidate)< best:
            best = sum(candidate)
    return best



ans2 = sum([solve_matrix(line) for line in data])
print(ans2)





