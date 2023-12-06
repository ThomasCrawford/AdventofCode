import re
from numpy import prod

size = 140

regex = r'(\d+)'



num_location = {}

def get_surrounding(y,x):
	surrounding = []
	for a in range(max(0,x-1),min(size,x+2)):
		for b in range(max(0,y-1),min(size,y+2)):
			if (b,a) != (y,x):
				surrounding.append((b,a))
	return surrounding

def find_numbers():
	for y in range(size):
		line = lines[y]
		nums = re.finditer(regex,line)
		for num in nums:
			for x in range(num.start(),num.end()):
				num_location[(y,x)]=num




def main():
	answer = 0
	with open("input.txt") as file:
		lines = file.readlines()

		# find numbers and add to num_location dictionary
		for y in range(size):
			line = lines[y]
			nums = re.finditer(regex,line)
			for num in nums:
				for x in range(num.start(),num.end()):
					num_location[(y,x)]=num
		print(num_location.keys())

		# find *
		for y in range(size):
			line = lines[y]	
			gears = re.finditer(r"\*",line)
			for gear in gears:
				numbers_next_to_gear = []
				for (b,a) in get_surrounding(y,gear.start()):
					if (b,a) in num_location.keys():
						numbers_next_to_gear.append(num_location[(b,a)])
				numbers_next_to_gear =  set(numbers_next_to_gear)
				if len(numbers_next_to_gear)>1:
					to_be_summed = 1
					for part in numbers_next_to_gear:
						to_be_summed = to_be_summed*int(part.group())
						# print(part.group())
					# print(to_be_summed)
					answer = answer + to_be_summed
					# print(answer)
	print(answer)


if __name__ == '__main__':
	main()