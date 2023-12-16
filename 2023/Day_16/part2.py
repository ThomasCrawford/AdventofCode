# Right is the positive real direction, DOWN is the positive imag direction
import cmath

def shine(start):
  todo = [start]
  lit = []
  while todo:
    loc, d = todo.pop()
    #d is direction light is moving LEAVING loc
    while (loc, d) not in lit:
      lit.append((loc,d))
      loc += d
      match data.get(loc):
        case None: break
        case "\\": 
          d = (d*-1j).conjugate()
        case "/": 
          d = (d*1j).conjugate()
        case "-":
          if int(d.imag):
            d = 1
            todo.append((loc,-1))
        case "|":
          if int(d.real):
            d = 1j
            todo.append((loc,-1j))
  return len(set([x for x,_ in lit]))-1

data = {}
with open("input.txt") as file:
   lines = [line.strip() for line in file]
w = len(lines)
for i in range(w):
   for k in range(w):
       data[k+i*1j] = lines[i][k]


# print(shine((-1,1)))

num_illuminated = []

for i in range(w):
  num_illuminated.append(shine((-1+i*1j,1)))
  num_illuminated.append(shine((i-1j,1j)))
  num_illuminated.append(shine((w+i*1j,-1)))
  num_illuminated.append(shine((i+w*1j,-1j)))
  # print(i, max(num_illuminated))


print(max(num_illuminated))