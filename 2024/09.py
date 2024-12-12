


with open("09.txt") as file:
    for line in file:
        data = line.strip()

def checksum(start_position, length, file_id):
    sum_of_positions = start_position*length+length*(length-1)/2
    return int(file_id*sum_of_positions)

front = 0
back = [len(data)-1,0]
pos = 0
last_id = (len(data)-1)//2
print(last_id)


ans1 = 0
while front < back[0]:
    if front % 2 == 0:
        ans1 += checksum(pos, int(data[front]),front//2)
        pos += int(data[front])
    else: # odd indexed entries are gaps
        gap = int(data[front])
        while gap >= int(data[back[0]])-back[1]: #if a gap is big enough to hold an entire file
            remaining = int(data[back[0]])-back[1]
            gap -= remaining
            ans1 += checksum(pos, remaining, back[0]//2)
            pos += remaining
            back = [back[0]-2,0]
        ans1 += checksum(pos, gap, back[0]//2)
        back[1] += gap
        pos += gap
    front += 1
assert front == back[0]
remaining = int(data[back[0]])-back[1]
ans1 += checksum(pos, remaining,front//2)

print(ans1)

