import hashlib
import re

salt = 'zpqevtbw'
regex5 = r'(.)\1\1\1\1'

# for i in range(100000000):
#     tohash = door + str(i)
#     result = hashlib.md5(tohash.encode()).hexdigest()
#     if result[:5] =="00000":
#         loc = int(result[5],16)
#         if loc < 8 and ans[loc] == 'x':
#             ans[loc] = result[6]
#             if 'x' not in ans:
#                 print('Part 2:'+ "".join(ans))
#                 quit()


def get_ith_hash(i):
    tohash = salt + str(i)
    return hashlib.md5(tohash.encode()).hexdigest()

def get_ith_hash_2016(i):
    tohash = salt + str(i)
    for _ in range(2017):
        tohash = hashlib.md5(tohash.encode()).hexdigest()
    return tohash


# def search_for_trio(data, letter, end_index):
#     start_index = max(0,end_index - 1000)
#     for i in range(start_index,end_index):
#         if re.search(r'(.)\1\1',data[i]): 
#             print (re.search(r'(.)\1\1',data[i]).groups(2))
#     return [i for i in range(start_index,end_index) if re.search(r'(.)\1\1',data[i]) and re.search(r'(.)\1\1',data[i]).groups(1) == letter]


data = {}
keys_found = set()

for i in range(24000):
    new_candidate = get_ith_hash(i)
    letter = re.search(r'(.)\1\1',new_candidate)
    if letter:
        data[i] = letter.group(1)
    five_letter = re.search(r'(.)\1\1\1\1',new_candidate)
    if five_letter:
        # print(five_letter.group(1))
        keys_found.update([j for j in range(max(0,i-1000),i) if j in data and data[j] == five_letter.group(1) ])
        for j in range(max(0,i-1000),i):
            if j in data and data[j] == five_letter.group(1):
                keys_found.add(j)

print(f'Part 1: {sorted(keys_found)[63]}')


data = {}
keys_found = set()
for i in range(24000):
    new_candidate = get_ith_hash_2016(i)
    letter = re.search(r'(.)\1\1',new_candidate)
    if letter:
        data[i] = letter.group(1)
    five_letter = re.search(r'(.)\1\1\1\1',new_candidate)
    if five_letter:
        # print(i, five_letter.group(1))
        keys_found.update([j for j in range(max(0,i-1000),i) if j in data and data[j] == five_letter.group(1) ])
        for j in range(max(0,i-1000),i):
            if j in data and data[j] == five_letter.group(1):
                keys_found.add(j)
print(f'Part 2: {sorted(keys_found)[63]}')