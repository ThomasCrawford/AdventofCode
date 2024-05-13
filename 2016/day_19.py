
seed = 3004953
# seed = 12

lis = [i for i in range(1,seed+1)]

parity = 0
while len(lis)>1:
    nex_parity = (len(lis)%2+parity)%2
    lis = lis[parity::2]
    parity = nex_parity

print(lis[0])