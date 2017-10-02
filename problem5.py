n = 2
while True:	
	print (n)
	for n2 in range(1, number):
		if n % n2 != 0:
			break
	else:
		return n
	n += 1
