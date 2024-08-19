import re



class Moon:
    def __init__(self, x, y, z):
        self.position = [int(x),int(y),int(z)]
        self.velocity = [0,0,0]

    def move(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def attract(self, other):
        for i in range(3):
            diff = other.position[i] - self.position[i]
            if diff == 0:
                d = 0
            else:
                d = diff//abs(diff)
            self.velocity[i] += d

    def energy(self):
        pot = sum([abs(x) for x in self.position])
        kin = sum([abs(x) for x in self.velocity])
        return pot*kin


moons = []
with open("input12.txt") as file:
    for line in file:
        a,b,c = re.findall(r'-?\d+',line)
        moons.append(Moon(a,b,c))


for _ in range(1000000):
    for moon in moons:
        for other in moons:
            if moon != other:
                moon.attract(other)
    for moon in moons:
        moon.move()
    print(sum([moon.energy() for moon in moons]))
ans1 = sum([moon.energy() for moon in moons])
print(ans1)