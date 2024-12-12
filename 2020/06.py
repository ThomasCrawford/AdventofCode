




data = []
with open("input06.txt") as file:
    content = file.read().strip()
    for entry in content.split("\n\n"):
        data.append(entry)

counts = [len(set(group + '\n'))-1 for group in data]
print(sum(counts))


ans2 = 0
for group in data:
    agree = 0
    ppl = group.split("\n")
    for q in ppl[0]:
        if all([q in line for line in ppl]):
            ans2 += 1
print(ans2)


