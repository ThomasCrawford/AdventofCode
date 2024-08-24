from math import log2


def step(p, line):
    if line[0] == "cut":
        m = int(line[-1])
        return (p-m)%N
    elif line[1] == "with":
        m = int(line[-1])
        return (p*m)%N
    elif line[1] == "into":
        return (N-p-1)%N

def run(p, N):
    for line in data:
        p = step(p, line)
    return p



data = []
with open("input22.txt") as file:
    for line in file:
        data.append(line.strip().split())

N = 10007
loc = 2019
ans1 = run(loc, N)
print(ans1)


#Part 2

# COMPOSITIONS OF LINEAR FUNCTIONS ARE LINEAR
# f(x) = a*x + b

# We want to find a function that does m iterations
# f^2(x) = a^2 x + (ab+b)

def get_fn_backwards(data):
    a = 1
    b = 0
    for line in data[::-1]:
        if line[0] == "cut":
            m = int(line[-1])
            b += m
        elif line[1] == "with":
            m = int(line[-1])
            m = pow(m,-1,N)
            a *= m
            b *= m
        elif line[1] == "into":
            a *= -1
            b *= -1
            b += N-1
    return a%N,b%N

N = 119315717514047
m = 101741582076661
loc = 2020

#one shuffle f(x) = a*x+b
a, b = get_fn_backwards(data)

# m shuffles f**m(x) = a**m * x + b(a**n-1)/(a-1)
b = b*(pow(a,m,N)-1)*(pow(a-1,-1,N))
a = pow(a,m,N)
ans2 = (a*loc + b)%N
print(ans2)



