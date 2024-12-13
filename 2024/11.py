from collections import defaultdict


with open("11.txt") as file:
    for line in file:
        nums = [int(x) for x in line.strip().split()]
        stones = defaultdict(int)
        for num in nums:
            stones[num] += 1

def one_stone_blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone))%2 ==0:
        l = len(str(stone))//2
        return [int(str(stone)[:l]), int(str(stone)[l:])]
    else:
        return [stone*2024]

def blink(stones):
    new_stones = defaultdict(int)
    for stone in stones:
        labels = one_stone_blink(stone)
        for label in labels:
            new_stones[label] += stones[stone]
    return new_stones


for i in range(25):
    stones = blink(stones)

ans1 = sum(stones.values())
print(ans1)

for i in range(50):  # 75 total
    stones = blink(stones)

ans2 = sum(stones.values())
print(ans2)
