
a = 591
b = 393
afactor = 16807
bfactor = 48271

def step(n,factor):
    return n*factor%2147483647


def step2(n,factor, check):
    x = n*factor%2147483647
    if x%check == 0:
        return x
    else:
        return step2(x,factor,check)

#Part 1
count1 = 0
for i in range(40000000):
    a = step(a,afactor)
    b = step(b,bfactor)
    if a%65536 == b%65536:
        count1+=1
print(f'Part 1: {count1}')

#Part 2
count2 = 0
for i in range(5000000):
    a = step2(a,afactor,4)
    b = step2(b,bfactor,8)
    if a%65536 == b%65536:
        count2+=1
print(f'Part 2: {count2}')