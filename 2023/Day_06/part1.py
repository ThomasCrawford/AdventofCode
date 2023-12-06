


def how_many_options(race_time, race_distance):
	return len([i for i in range(race_time) if i*(race_time-i)>race_distance])


answer = 1
with open("input.txt") as file:
	time, distance = file
	time = [int(x) for x in time[8:].split()]
	distance = [int(x) for x in distance[9:].split()]
	number_of_races = len(time)
	for index in range(number_of_races):
		answer = answer* how_many_options(time[index],distance[index])

print(answer)