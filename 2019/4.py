start = 359282
end = 820401

def double(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return True
    return False

def increasing(n):
    n = str(n)
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return False
    return True

ans1 = len([x for x in range(start, end) if double(x) and increasing(x)])
print(ans1)

def double2(n):
    n = str(n)
    p = 0
    d = 0
    while p < 5:
        while d < 6 and n[p] == n[d] :
            d += 1
        if d-p == 2:
            return True
        else:
            p = int(d)
    return False
        

ans2 = len([x for x in range(start, end) if double2(x) and increasing(x)])
print(ans2)
