import re

regex = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).'


def modulo_inverse(m,n):
    for i in range(n):
        if (i*m)%n ==1:
            return i

data = []
N = 1
with open("input_15.txt") as file:
    for line in file:
        i, n, a = re.match(regex, line.strip()).groups()
        data.append([int(i),int(n),int(a)])
        N *= int(n)

answer = 0

for line in data:
    i, n, a = line
    b = (n-a -i)%n
    m = N//n
    y = modulo_inverse(m,n)
    answer += y*b*m

answer = answer % N
print(answer)

