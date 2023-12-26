import hashlib

secret_key = 'ckczppom'

def md5(integer):
	string = secret_key + str(integer)
	encoded_string = string.encode()
	md5_hash = hashlib.md5()
	md5_hash.update(encoded_string)
	return md5_hash.hexdigest()

for i in range(10**9):
	if md5(i)[:5]=="00000":
		print(f'Part 1: {i}')
	if md5(i)[:6]=="000000":
		print(f'Part 2: {i}')
		exit()
