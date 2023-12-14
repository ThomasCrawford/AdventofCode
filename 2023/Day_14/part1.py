import re

def score_chunk(start_index, num_stones):
	return int((width - start_index)*num_stones - (num_stones+1)*num_stones/2)

def score(string):
	i_list = [-1]+[m.start() for m in re.finditer("#",string)]
	n_list = [chunk.count("O") for chunk in string.split("#")]
	string_answer = 0
	for start, num_stones in zip(i_list,n_list):
		string_answer += score_chunk(start,num_stones)
	return string_answer

with open("input.txt") as file:
	data = [line for line in file]
t_data = ["".join(word[i] for word in data) for i in range(len(data))]
width = len(t_data[0])


answer = 0
for x in t_data:
	answer += score(x)
print(answer)