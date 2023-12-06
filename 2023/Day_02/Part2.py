import re


def max_red(line):
    red_instance = re.findall(r"\d{1,2} red",line)
    reds = [int(x.split(' ')[0]) for x in red_instance]
    return(max(reds))

def max_green(line):
    green_instance = re.findall(r"\d{1,2} green",line)
    greens = [int(x.split(' ')[0]) for x in green_instance]
    return(max(greens))

def max_blue(line):
    blue_instance = re.findall(r"\d{1,2} blue",line)
    blues = [int(x.split(' ')[0]) for x in blue_instance]
    return(max(blues))

    # for x in red_instance:
    #     if int(x.split(' ')[0]) > 12: 
    #         return True
    # blue_instance = re.findall(r"\d{2} blue",line)
    # for x in blue_instance:
    #     if int(x.split(' ')[0]) > 14: 
    #         return True    
    # green_instance = re.findall(r"\d{2} green",line)
    # for x in green_instance:
    #     if int(x.split(' ')[0]) > 13: 
    #         return True                

answer = 0
with open("input.txt") as file:
    for line in file:
        answer = answer + max_red(line)*max_blue(line)*max_green(line)
print(answer)