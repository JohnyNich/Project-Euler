# Summation of primes
from assets import *
total = 0
numbers = range(3, 2000000, 2)
for n in numbers:
	print (n)
	if isPrime(n) == True:
		total += n
total += 2
print (total)
# Answer: 142913828922
