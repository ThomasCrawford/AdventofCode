from collections import defaultdict, deque

score = defaultdict(int)

players = 429  
marbles = 70901*100

circle = deque([0])
count = 0

for n in range(marbles + 1):
    if n % 23 != 0:
        circle.rotate(-2)
        circle.appendleft(n)
    elif n != 0 :
        circle.rotate(7)
        score[n%players] += n + circle[0]
        circle.popleft()

print(max(score.values()))


