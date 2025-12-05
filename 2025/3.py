
def mostj(line,n):
    lis = [int(x) for x in line]
    out = ""
    while n:
        m = len(lis)-n
        newi = lis.index(max(lis[:m+1]))
        out += str(lis[newi])
        n -= 1
        if n:
            lis = lis[newi+1:]
    return int(out)

data = []
with open("3.txt") as file:
    for line in file:
        data.append(line.strip())


ans1 = sum([mostj(line,2) for line in data])
ans2 = sum([mostj(line,12) for line in data])
print(ans1)
print(ans2)









