


data = []
with open("input02.txt") as file:
    for line in file:
        a,b,c = line.strip().split()
        n1,n2 = [int(x) for x in a.split("-")]
        data.append([int(n1),int(n2),b[:-1],c])

ans1 = 0
for line in data:
    c = line[3].count(line[2])
    if line[0]<= c <= line[1]:
        ans1 += 1
print(ans1)


ans2 = 0
for line in data:
    n1, n2, i, s = line
    n1 -=1
    n2 -=1
    if (n1 < len(s) and s[n1] == i) ^ (n2 < len(s) and s[n2] == i):
        ans2 += 1

print(ans2)



