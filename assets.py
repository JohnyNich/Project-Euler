def getFactors(number):
	print ("start")
	factors = []
	for n in range(2, number):
		print (n)
		for n2 in range(2, number):
			print (n2)
			if n * n2 == number:
				factors.append(n)
				print (n)
	return factors

def isPrime(number):
	n = 2
	while n != number:
		if number % n == 0:
			return False
			break
		n += 1
	else:
		return True
	

