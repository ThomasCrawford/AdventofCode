import re

regex1 = r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))'

ans1 = 0
ans2 = 0
flag = True
with open("03.txt") as file:
    for line in file:
        for hit in re.findall(regex1,line):
            if hit[2]:
                flag = True
            elif hit[3]:
                flag = False
            else:
                v = int(hit[0])*int(hit[1])
                ans1 += v
                if flag:
                    ans2 += v
print(ans1)
print(ans2) 


