import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(106500,123501)[::17]:
    if not is_prime(i):
        count +=1
print(count)
