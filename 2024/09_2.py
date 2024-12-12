with open("09.txt") as file:
    for line in file:
        data = line.strip()

def checksum(start_position, length, file_id):
    sum_of_positions = start_position*length+length*(length-1)/2
    return int(file_id*sum_of_positions)


def find_gap(gaps, length):
    for i, gap in enumerate(gaps):
        if gap[1] >= length:
            return i
    return -1

gaps = []

files = []

p = 0
for i,x in enumerate(data):
    if i%2==0:
        files.append([p, int(x) , i//2]) # start position, file length, file id
    else:
        gaps.append([p,int(x)]) # start position, length
    p += int(x)

ans2 = 0
while files:
    file = files.pop()
    if file[2]%1000 == 0:
        print(file[2])
    i = find_gap(gaps, file[1])

    if i == -1 or gaps[i][0]>file[0]:
        ans2 += checksum(*file)
    else:
        ans2 += checksum(gaps[i][0] , file[1],file[2])
        gaps[i][0] += file[1]
        gaps[i][1] -= file[1]


print(ans2)
