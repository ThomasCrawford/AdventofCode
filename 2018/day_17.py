import re
import sys

sys.setrecursionlimit(20000)


def look_down(x, y, horr,vert):
    for line in horr:
        if line[0] > y and line[1]<= x <=line[2]:
            return x, line[0]-1, line[1], line[2] #newx, newy, left end of support, y end
    return False

def look_right(x, y, horr,vert):
    for line in vert:
        if line[0] > x and line[1]<= y <=line[2]:
            return line[0]
    return False

def look_left(x, y, horr,vert):
    for line in vert[::-1]:
        if line[0] < x and line[1]<= y <=line[2]:
            return line[0]
    return False

# def fill(x,y,horr,vert, fill_so_far):
#     left = look_left(x,y,horr,vert)[0]
#     right = look_right(x,y,horr,vert)[0]
#     if not left or not right:
#         return x,y,horr, fill_so_far
#     else:
#         for h in crit_heights[::-1]:
#             if h < y:
#                 look_l = look_left(x, h, horr,vert)[0]
#                 look_r = look_right(x, h, horr,vert)[0]
#                 #if container being filled has something in it
#                 if look_l > left or look_r < right:
#                     horr.append([h-1,left,right])
#                     horr.sort()
#                     fill_count = (right-left)*(y-h-1) + fill_so_far
#                     return x, h, horr, fill_count
#                 # if container overflows:
#                 if not look_l or not look_r or look_l < left or look_r > right:
#                     horr.append([h,left,right])
#                     horr.sort()
#                     fill_count = (right-left)*(y-h)
#                     return x, h, horr, fill_count


def condense(h, horr):
    for h2 in horr:
        if h[0] == h2[0]:
            if h[2] == h2[1]:
                horr.remove(h2)
                horr.append([h2[0], h[1], h2[2]])
                return horr
            if h[1] == h2[2]:
                horr.remove(h2)
                horr.append([h2[0], h2[1], h[2]])
                return horr
    horr.append(h)
    return horr


def display(horr, vert):

    xmin = min([line[0] for line in vert])
    xmax = max([line[0] for line in vert])

    data = set()
    for line in vert:
        for y in range(line[1],line[2]+1):
            data.add((line[0],y))
    for line in horr:
        for x in range(line[1],line[2]+1):
            data.add((x, line[0]))


    for y in range(crit_heights[-1]+1):
    # for y in range(80):
        out = ""
        for x in range(xmin-1, xmax+2):
            if x == 500 and y == 0:
                out += "+"
            elif (x,y) in data:
                out += "#"
            else:
                out += "."
        out += str(y)
        print(out)



def fill(x,y,horr,vert):
    # print(f'filling {x}, {y}')
    left = look_left(x,y,horr,vert)
    right = look_right(x,y,horr,vert)
    for h in crit_heights[::-1]:
        if h < y:
            look_l = look_left(x, h, horr,vert)
            look_r = look_right(x, h, horr,vert)
            # print(f'h {h}, left {left}, right {right}, look_l {look_l}, look_r {look_r}')
            #if container being filled has something in it
            if look_l > left or look_r < right:
                horr = condense([h,left,right],horr)
                horr.sort()
                fill_count = (right-left)*(y-h-1) 
                return horr, fill_count
            # if container overflows:
            if not look_l or not look_r or look_l < left or look_r > right:
                horr = condense([h + 1,left,right], horr)
                horr.sort()
                fill_count = (right-left)*(y-h)
                return horr, fill_count
                
def flow(x,y,horr, vert, count):
    
    if not look_down(x,y,horr,vert):
        return
    x, new_y, ls, rs = look_down(x,y,horr,vert)
    left = look_left(x,new_y,horr,vert)
    right = look_right(x,new_y,horr,vert)
    if left and right and left >= ls and right <= rs:
        # print(f'Filling at {x},{y}')
        new_horr, new_count = fill(x, new_y, horr, vert)
        main(new_horr, vert, new_count + count)
    #flow left
    if not left or left < ls:
        new_x = ls - 1
        a = flow(new_x, new_y, horr, vert, count)
    if not right or right > rs:
        new_x = rs + 1
        b = flow(new_x, new_y, horr, vert, count)


def pools(x,y,horr, vert):
    if not look_down(x,y,horr,vert):
        return False
    x, new_y, ls, rs = look_down(x,y,horr,vert)
    left = look_left(x,new_y,horr,vert)
    right = look_right(x,new_y,horr,vert)
    if left and right and left >= ls and right <= rs:
        return x, new_y

    a = False
    b = False
    if not left or left < ls:
        new_x = ls - 1
        a = pools(new_x, new_y, horr, vert)
    if not right or right > rs:
        new_x = rs + 1
        b = pools(new_x, new_y, horr, vert)
    return a or b

def fill_all(horr, vert):
    x = 500
    y = 0
    fill_count = 0
    while pools(x,y,horr,vert):
        x_to_fill, y_to_fill = pools(x,y,horr,vert)
        horr, count = fill(x_to_fill, y_to_fill, horr, vert)
        fill_count += count
        display(horr,vert)
    return horr, fill_count


vert = []
horr = []
with open("input_17.txt") as file:
    for line in file:
        nums = [int(x) for x in re.findall(r'(\d+)', line)]
        if line[0] == "x":
            vert.append(nums)
        else:
            horr.append(nums)
vert.sort()
for line in vert:
    if not any([line[1] == h[0] and h[1] <= line[0] <= h[2]  for h in horr]):
        horr.append([line[1],line[0],line[0]])
horr.sort()

c_heights= []
for x in [line[1] for line in vert] + [line[2] for line in vert]:
    c_heights.append(x)
    c_heights.append(x-1)
crit_heights = list(set(sorted(c_heights)))
  


horr, count = fill_all(horr, vert)

display(vert, horr)

