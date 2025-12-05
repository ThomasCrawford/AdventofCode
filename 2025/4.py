import cmath

neighbors = [1,1j,-1,-1j, 1+1j, 1-1j, -1+1j, -1-1j]

def get_count(data,point):
    return len([d for d in neighbors if point+d in data])


data = set()
with open("4.txt") as file:
    for i,line in enumerate(file):
        for k,v in enumerate(line.strip()):
            if v == "@":
                data.add(k+1j*i)


ans1 = len([x for x in data if get_count(data,x)<4])
print(ans1)

ans2 = 0
while min([get_count(data,x) for x in data])<4:
    
    new = [x for x in data if get_count(data,x)>=4]
    ans2 += len(data)-len(new)
    data = set(new)
    print(len(data))

print(ans2)