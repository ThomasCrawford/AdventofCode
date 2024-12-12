


data = []
with open("07.txt") as file:
    for line in file:
        a,bs = line.strip().split(':')
        data.append([int(a),[int(x) for x in bs.split()]])



def is_valid(target, nums):
    partials = set([nums[0]])

    for num in nums[1:]:
        new_partials = set()
        for x in partials:
            new_partials.add(x+num)
            new_partials.add(x*num)
        partials = set([x for x in new_partials if x <= target])
    return target in partials

def is_valid2(target, nums):
    partials = set([nums[0]])

    for num in nums[1:]:
        new_partials = set()
        for x in partials:
            new_partials.add(x+num)
            new_partials.add(x*num)
            new_partials.add(int(str(x)+str(num)))
        partials = set([x for x in new_partials if x <= target])
    return target in partials

ans1 = 0
ans2 = 0
for target, nums in data:
    if is_valid(target,nums):
        ans1 += target
    if is_valid2(target,nums):
        ans2 += target

print(ans1)
print(ans2)
