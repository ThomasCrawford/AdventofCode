import itertools
import heapq
import math

connection_count = 1000


class Dset:
    def __init__(self,objects):
        self.dsets = []
        self.which_set = {}
        for box in objects:
            its_set = set([box])
            self.dsets.append(its_set)
            self.which_set[box] = its_set

    def merge(self,a,b):
        if self.which_set[a] != self.which_set[b]:
            new_set = self.which_set[a].union(self.which_set[b])
            self.dsets.append(new_set)
            self.dsets = [x for x in self.dsets if x not in [self.which_set[a],self.which_set[b]]]
            for x in new_set:
                self.which_set[x] = new_set



def dist(box1, box2):
    return sum(abs(a-b)**2 for a,b in zip(box1,box2))


boxes = []
with open("8.txt") as file:
    for line in file:
        boxes.append(tuple(int(x) for x in line.strip().split(",")))


distances = []
for a,b in itertools.combinations(boxes,2):
    distances.append([dist(a,b),(a,b)])
distances.sort()
    

#Part 1
sets = Dset(boxes)
for pair in distances[:connection_count]:
    sets.merge(pair[1][0],pair[1][1])

lengths = [len(x) for x in sets.dsets]
lengths.sort()
ans1 = math.prod(lengths[-3:])
print(ans1)



#Part 2
sets = Dset(boxes)
while len(sets.dsets)>1:
    d = distances.pop(0)
    sets.merge(d[1][0],d[1][1])
ans2 = d[1][0][0]*d[1][1][0]
print(ans2)

