import random

while True:
	try:
		password_length = int(input('How many characters does your password need to include? '))
	except ValueError:
		print('Please input an integer.')
		continue
	if password_length <= 0:
		print('Please input a positive integer above zero.')
	else:
		break

class Password:
	def __init__(self, password_length):
		self.password_length = password_length
	
	def generate(self):
		characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '&', '%', '.']
		
		password_list = []
		
		for char in range(0, password_length):
			rand_num = random.randint(0, len(characterList) - 1)
			password_list.append(characterList[rand_num])
			
		password = ''.join(password_list)
		
		print('Your password is:', password)

new_password = Password(password_length)
new_password.generate()