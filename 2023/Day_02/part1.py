import re


def is_over(line):
    red_instance = re.findall(r"\d{2} red",line)
    for x in red_instance:
        if int(x.split(' ')[0]) > 12: 
            return True
    blue_instance = re.findall(r"\d{2} blue",line)
    for x in blue_instance:
        if int(x.split(' ')[0]) > 14: 
            return True    
    green_instance = re.findall(r"\d{2} green",line)
    for x in green_instance:
        if int(x.split(' ')[0]) > 13: 
            return True                

answer = 0
with open("input.txt") as file:
    for line in file:
        colon_index = line.find(':')
        game = int(line[5:colon_index])
        if not is_over(line): answer = answer + game
print(answer)