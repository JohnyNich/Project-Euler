# 10001st prime number
from assets import *
counter = 0
n = 2
prime_numbers = []
while counter != 10001:
	if isPrime(n) == True:
		prime_numbers.append(n)
		counter +=1
	n += 1
print (prime_numbers)
		
