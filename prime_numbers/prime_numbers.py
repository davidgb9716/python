#!/usr/bin/env python3

def prime_numbers_generator(n):
	for num in range(1, n + 1):
		yield num

def is_it_prime(n):
	prime = True
	my_gen_obj = prime_numbers_generator(n)
	
	if n == 1:
		prime = False
		return False
	for num in my_gen_obj:
		if n % num == 0 and n != num and num != 1:
			prime = False
		if n == num:
			if prime == True:
				return True
			else:
				return False

is_this_number_prime = 737373731

result = is_it_prime(is_this_number_prime)

if result == True:
	print(f'The number {is_this_number_prime} is prime.')
else:
	print(f'The number {is_this_number_prime} is composite.')