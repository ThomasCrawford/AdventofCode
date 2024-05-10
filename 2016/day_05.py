import hashlib
 
door = "ojvtpuvg"

index = 0

ans = ["x"]*8


for i in range(100000000):
    tohash = door + str(i)
    result = hashlib.md5(tohash.encode()).hexdigest()
    if result[:5] =="00000":
        loc = int(result[5],16)
        if loc < 8 and ans[loc] == 'x':
            ans[loc] = result[6]
            if 'x' not in ans:
                print('Part 2:'+ "".join(ans))
                quit()

