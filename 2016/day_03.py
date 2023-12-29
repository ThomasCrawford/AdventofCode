data = []
with open("input_03.txt") as file:
    for line in file:
        data.append([int(x) for x in line.strip().split()])

def test (triple):
    out = sorted(triple)
    return out[0] + out[1] > out[2]

answer1 = sum([test(x) for x in data])
print(answer1)


new_data = []
for i in range(0,len(data),3):
    x = []
    x.append(data[i])
    x.append(data[i+1])
    x.append(data[i+2])
    transposed_matrix = [list(row) for row in zip(*x)]
    new_data += transposed_matrix

answer2 = sum([test(x) for x in new_data])
print(answer2)
