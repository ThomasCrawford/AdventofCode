from functools import lru_cache

buckets = []
with open("input_17.txt") as file:
    for line in file:
        buckets.append(int(line.strip()))

bit_count = len(buckets)
start = 150



successes = set()

#how many ways
@lru_cache(maxsize = 200000)
def f(buckets_used, eggnog):
    if eggnog == 0:
        successes.add(buckets_used)
        print(len(successes), bin(buckets_used))
    for bucket_index in range(bit_count):
        if not buckets_used & 1 << bucket_index:
            if buckets[bucket_index] <= eggnog:
                f(buckets_used | (1 << bucket_index), eggnog - buckets[bucket_index])


print(f(0,start))

print(len(successes))

print(f.cache_info())



