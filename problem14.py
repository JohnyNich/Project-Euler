# Largest Collatz sequence
current = [] # This list is where all the numbers for each calculation, and will be cleared after each calculation
totals = {} # This dictionary will hold each starting number and length as length : starting number
stn = 2 # This is the starting number
while stn < 1000000: # While n is under one million
	n = stn # n will be the variable which will hold the current number
	while n != 1:
		current.append(n)
		if n % 2 == 0: # If n is even
			n = n/2
		else: # Else, n must be odd
			n = (n * 3) + 1
	print (stn, len(current) + 1)
	totals[len(current) + 1] = stn # I add 1 here as the number 1 is included. Also, I have the length
	current.clear()
	stn += 1
largest = totals[max(totals.keys())] # This will give us the largest key (the largest length) and then find out what the starting number for the length was
print (largest)
