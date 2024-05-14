import itertools

seed = 'abcdefgh'
word = list(seed)
target = 'fbgdceah'
target = list(target)

def swap_p(word, i,j):
    x = word[i]
    word[i] = word[j]
    word[j] = x
    return word

def swap_l(word,a,b):
    return [a if l==b else b if l==a else l for l in word]

def rotate(word, n):
    l = len(word)
    n = n%l
    return word[l-n:] + word[:l-n]

def rotate_b(word,a):
    i = word.index(a)
    n = i + 2 if i >=4 else i+1
    return rotate(word,n)

def reverse(word,i,j):
    return word[:i]+ word[i:j+1][::-1] + word[j+1:]

def move(word,i,j):
    l = word.pop(i)
    word.insert(j,l)
    return word

data = []
with open("input_21.txt") as file:
    for line in file:
        data.append(line.strip().split())

def scramble(word,data):
    for line in data:
        match line[0]:
            case 'move':
                word = move(word,int(line[2]),int(line[5]))
            case 'reverse':
                word = reverse(word,int(line[2]),int(line[4]))
            case 'rotate':
                match line[1]:
                    case 'based':
                        word = rotate_b(word,line[6])
                    case 'right':
                        word = rotate(word,int(line[2]))
                    case 'left':
                        word = rotate(word,-1*int(line[2]))
            case 'swap':
                match line[1]:
                    case 'position':
                        word = swap_p(word,int(line[2]),int(line[5]))
                    case 'letter':
                        word = swap_l(word, line[2], line[5])
    return word

poss_inputs = list(itertools.permutations(word))

for i in poss_inputs:
    if scramble(i,data) == target:
        print("".join(i))



# print("".join(scramble(word,data)))

