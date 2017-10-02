# Largest prime factors
from assets import *

def prime_factors(number):
	prime_factors = []
	print ("start")
	for n in getFactors(number):
		if isPrime(n) == True:
			prime_factors.append(n)
	print (prime_factors)
	print ("done")
	
prime_factors(600851475143)
