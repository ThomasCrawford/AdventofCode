import re
from collections import defaultdict


def next_date(date):
    if date[0] in [1,3,5,7,8,10,12] and date[1] == 31:
        return tuple([(date[0]+1)%12, 1])
    elif date[0] in [4,6,9,11] and date[1] == 30:
        return tuple([(date[0]+1)%12, 1])
    elif date[0] == 2 and date[1] in [28]:
        return tuple([(date[0]+1)%12, 1])
    else:
        return tuple([date[0],date[1]+1])

def min_asleep(times):
    asleep_mins = 0
    for i in range(len(times)//2):
        asleep_mins += times[2*i +2] - times[2*i +1]
    return asleep_mins

def sleepiest_minute(guard, data):
    clock = [0]*60
    for date in data:
        if register[date] == guard:
            for i in range(len(data[date])//2):
                for t in range(data[date][2*i+1], data[date][2*i+2]):
                    clock[t] += 1
    return clock

def is_asleep(times, minute):
    for i in range(len(times)//2):
        if times[2*i+1] <= minute < times[2*i + 2]:
            return True
    return False

def how_freq_asleep(guard, minute, data):
    count = 0
    for date in data:
        if register[date] == guard and is_asleep(data[date],minute):
            count += 1
    return count

register = {}
data = defaultdict(list)
with open("input_04.txt") as file:
    for line in file:
        nums = [int(x) for x in re.findall(r'\d+', line.strip())]
        date = tuple(nums[1:3])
        if nums[3] == 23:
            date = next_date(date)
        time = nums[4] - 60 if nums[3] == 23 else nums[4]
        data[date].append(time)
        if len(nums) > 5:
            register[date] = nums[5]
for guard in data:
    data[guard].sort()
    data[guard][0] = max(0,data[guard][0])

sleep_count = {}
for guard in set(register.values()):
    sleep_count[guard] = 0 

for date in data:
    sleep_count[register[date]] += min_asleep(data[date])

sleepiest = max(sleep_count, key = sleep_count.get)
clock = sleepiest_minute(sleepiest, data)
key_minute = clock.index(max(clock))

print(key_minute * sleepiest)


#Part 2

record = 0
for guard in sleep_count:
    clock = sleepiest_minute(guard, data)
    m = max(clock)
    if m > record:
        ans2 = guard*clock.index(m)
        record = m

print(ans2)
