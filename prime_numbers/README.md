# Prime Number Identifier with Generators

This Python project is a Prime Number Generator that allows users to determine whether a given number is prime. The program efficiently checks for primality by leveraging a Python generator to produce the series of the first (n) natural numbers, where (n) represents the number to be checked. This method ensures both optimal performance and elegant code execution.

The given number is divided by each individual number in the generated series to test for primality. If the number is divisible by any of these values (excluding 1 and the number itself), it is not a prime number. Otherwise, the number is confirmed to be prime.