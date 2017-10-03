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
	
# The following are some variable type functions

def rtype(variable): # rtype stands for return type. It will return the type as a string
	output = type(variable)
	return str(output)[8:-2]
	
def isType(typ, variable): # isType will check if the variable is of type typ
	if rtype(variable) == typ:
		return True
	else:
		return False

print (isType("bool", True))

# End of variable type functions
