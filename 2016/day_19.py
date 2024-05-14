from collections import deque


seed = 3004953

lis = [i for i in range(1,seed+1)]

parity = 0
while len(lis)>1:
    nex_parity = (len(lis)%2+parity)%2
    lis = lis[parity::2]
    parity = nex_parity
print(f'Part 1: {lis[0]}')


lis = [i for i in range(1,seed+1)]

while len(lis)>2:
    n = len(lis)
    a = n//2 + 2 if n%2 == 0 else n//2+1
    lis = lis[n//3:n//2] + lis[a:n-1:3] + [lis[-1]] + lis[:n//3]

print(f'Part 2: {lis[0]}')