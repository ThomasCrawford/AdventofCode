

def endpoints(steps):
    start = (0,0)
    segments = []
    for step in steps:
        if step[0] == "R":
            end = (start[0] + int(step[1:]), start[1])
        elif step[0] == "L":
            end = (start[0] - int(step[1:]), start[1])
        elif step[0] == "U":
            end = (start[0] , start[1] + int(step[1:]))
        elif step[0] == "D":
            end = (start[0] , start[1] - int(step[1:]))
        segments.append([start, end])
        start = end
    return segments

def pt_on_seg(pt, seg):
    xs = sorted([seg[0][0], seg[1][0]])
    ys = sorted([seg[0][1], seg[1][1]])
    if xs[0] <= pt[0] <= xs[1] and ys[0] <= pt[1] <= ys[1]:
        return True
    return False

def intersect(seg1, seg2):
    if seg1[0][0] == seg1[1][0] and seg2[0][1] == seg2[1][1]:
        cand = (seg1[0][0], seg2[0][1])
    elif seg2[0][0] == seg2[1][0] and seg1[0][1] == seg1[1][1]:
        cand = (seg2[0][0], seg1[0][1])
    else:
        return False
    if pt_on_seg(cand, seg1) and pt_on_seg(cand, seg2):
        return cand
    else:
        return False

def find_intersections(wire1, wire2):
    out = [intersect(seg1, seg2) for seg1 in wire1 for seg2 in wire2 if intersect(seg1, seg2)]
    out = [x for x in out if x != (0,0)]
    return out


def wire_dist_to_pt(wire, pt):
    count = 0
    for seg in wire:
        if not pt_on_seg(pt, seg):
            count += abs(seg[0][0] - seg[1][0]) + abs(seg[0][1] - seg[1][1])
        else:
            count += abs(seg[0][0] - pt[0]) + abs(seg[0][1] - pt[1])
            return count



data = []
with open("input3.txt") as file:
    for line in file:
        data.append(line.strip().split(","))

wire1, wire2 = [endpoints(steps) for steps in data]
intersections = find_intersections(wire1, wire2)
ans1 = min([abs(x[0]) + abs(x[1]) for x in intersections])
print(ans1)


ans2 = min([wire_dist_to_pt(wire1, pt) + wire_dist_to_pt(wire2, pt) for pt in intersections])
print(ans2)
