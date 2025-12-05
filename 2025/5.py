
def check(num):
    for a,b in ranges:
        if int(a) <= num <= int(b):
            return True
    return False


ranges = []
ingredients =[]
with open("5.txt") as file:
    skip = False
    for line in file:
        if line == "\n":
            skip = True
        elif skip:
            ingredients.append(int(line.strip()))
        else:
            ranges.append(line.strip().split("-"))


ans1 = len([x for x in ingredients if check(x)])
print(ans1)

ranges = [[int(a),int(b)] for [a,b] in ranges]
ranges.sort()


ans2 = 0
latter = ranges.pop()
while ranges:
    former = ranges.pop()
    print(former,latter)
    if former[1] >= latter[0]:
        print("absorbed")
        latter = [min(former[0],latter[0]),max(former[1],latter[1])]
    else:
        print("not")
        ans2 += latter[1]-latter[0]+1
        latter = former
ans2 += latter[1]-latter[0]+1
print(ans2)

