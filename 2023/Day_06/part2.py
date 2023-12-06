

def how_many_options(race_time, race_distance):
	return len([i for i in range(race_time) if i*(race_time-i)>race_distance])


answer = 1
with open("input.txt") as file:
	time, distance = file
	time = int(time[8:].replace(" ",""))
	distance = int(distance[9:].replace(" ",""))

print(how_many_options(time,distance))