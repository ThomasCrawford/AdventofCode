import re
import numpy as np

regex = r'[XY][+=](\d+)'

data = []
with open("13.txt") as file:
    for line in file:
        data += [int(x) for x in re.findall(regex,line)]
prizes = [data[i:i+6] for i in range(0,len(data),6)]


def solve_system(a,c,b,d,m,n):
    det = a*d-b*c
    if det == 0: #handle this case if it comes up
        print("ERROR: det 0")
        return 0
    M = np.array([[d,-b],[-c,a]])
    v = np.array([m,n])
    result = list(np.matmul(M,v))
    if all([x%det==0 for x in result]):
        return result[0]//det*3 + result[1]//det*1
    else:
        return 0

ans1 = 0
ans2 = 0
for prize in prizes:
    ans1 += solve_system(*prize)
    prize[4] += 10000000000000
    prize[5] += 10000000000000
    ans2 +=solve_system(*prize)
print(ans1)
print(ans2)


