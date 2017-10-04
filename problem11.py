# Largest product in grid
sequence = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
sequence = sequence.split(" ")
n = 1 # This is the number used for the array name
num_lists = int(len(sequence)) / 20 # This tells us how many lists there are going to be.
while n <= 20:
	exec("numbers" + str(n) + " = sequence[:20]")
	sequence = sequence[20:]
	n += 1
print (numbers20)
print (len(sequence))
n = 1
while n <= 20: # This section handles putting all the numbers lists (numbers1, numbers2, etc.) into one giant list
	exec("sequence.append(numbers" + str(n) + ")")
	n += 1
products = [] # This list will hold all the products
sequence = [list(map(int, lst)) for lst in sequence] # This code here will convert all the list elements into integers
print (sequence)
#~ # Start by finding all the products horizontally
#~ for numbers in sequence: # For each list inside the giant sequence list
	#~ print (numbers)
	#~ n2 = 0
	#~ while n2 <= 19 : # Will iterate through each item in the list from item 0-19, not 20 as the list only goes fomr 0-19.
		#~ # We start by looking at products from left to right
		#~ if n2 <= 16: # Any index beyond 16 would have less then 4 products. Eg. 17 would have only 3 numbers to multiply: 17, 18 and 19.
			#~ products.append(numbers[n2] * numbers[n2 + 1] * numbers[n2 + 2] * numbers[n2 +3])
		#~ # Now we look at it from right to left
		#~ if n2 >= 3: # We use 3 as for 2, the product would be of index 0, 1 and 2, which is only 3 numbers.
			#~ products.append(numbers[n2] * numbers[n2 - 1] * numbers[n2 - 2] * numbers[n2 - 3])
		#~ n2 += 1
#~ # Now finding all the products vertically
#~ for x in range(0, 20): # We use numbers instead of iterating through the giant list (the list being sequence) as we have to manipulate multiple lists inside of just iterating through items inside one list
	#~ # Note: x is the row that we're currently working on
	#~ # Sequence = [list][item]. Sequence = [row][column]. Sequence = [x][n2]
	#~ print (x)
	#~ n2 = 0 # n2 is refering to the column that we're working with
	#~ while n2 <= 19: # The following setup is familiar to the previous setup, except it checks the value of x
		#~ # We start looking at products from top to bottom
		#~ if x <= 16: # As n2 is constant, this time we have to check the value of x.
			#~ products.append(sequence[x][n2] * sequence[x + 1][n2] * sequence[x + 2][n2] * sequence[x + 3][n2]) # Throughout this whole process here, n2 (the column) stays constant, it only finds the product the item at the same column but in a different row.
		#~ # Now we look from bottom to top
		#~ if x >= 3:
			#~ products.append(sequence[x][n2] * sequence[x - 1][n2] * sequence[x - 2][n2] * sequence[x - 3][n2])
		#~ n2 += 1
#~ # Now finding all the products diagonally
#~ for x1 in range(0, 20): # The range is going from 0 to 19 (it doesn't include 20 as, with range(), it will only go up to and not including to 20.
	#~ for x2 in range(0, 20): # x1 is the row, x2 is the column
		#~ print (x1, x2)
		#~ # This algorithm will go through each item in each row, then use that item in that row to find the diagonal
		#~ # We start looking at products of diagonal from top left to bottom right
		#~ if x1 <= 16 and x2 <= 16: # Here, both x1 and x2 are changing
			#~ products.append(sequence[x1][x2] * sequence[x1 + 1][x2 + 1] * sequence[x1 + 2][x2 + 2] * sequence[x1 + 3][x2 + 3])
		#~ # Now we look from top right to bottom left
		#~ if x1 >= 3 and x2 >= 3:
			#~ products.append(sequence[x1][x2] * sequence[x1 - 1][x2 - 1] * sequence[x1 - 2][x2 - 2] * sequence[x1 - 3][x2 - 3])
			
c = 0
for x1 in range(0, 20): # x1 is the row
	for x2 in range(0,20): # x2 is the column, or the index
		print (x1, x2)
		# We start with horizontal equations
		# Left to right
		if x2 <= 16: # If the number's index is more than 16, then there won't be enough numbers proceding it to do a 4-number product. Eg. Something at index 17 could only do the product of 17, 18 and 19
			print ("Left to right")
			c += 1
			products.append(sequence[x1][x2] * sequence[x1][x2 + 1] * sequence[x1][x2 + 2] * sequence[x1][x2 + 3]) # Here, the row stays constant, but the column changes
		# Now vertical
		# Top to bottom
		if x1 <= 16: # If the row is 17 or over, it will not work, as there will only be 3 numbers to calculate
			print ("Top to bottom")
			c += 1
			products.append(sequence[x1][x2] * sequence[x1 + 1][x2] * sequence[x1 + 2][x2] * sequence[x1 + 3][x2])
		# Lastly diagonal
		# Down to the right
		if x1 <= 16 and x2 <= 16: # Here, both x1 and x2 are changing
			print ("Top left to bottom right")
			c += 1
			products.append(sequence[x1][x2] * sequence[x1 + 1][x2 + 1] * sequence[x1 + 2][x2 + 2] * sequence[x1 + 3][x2 + 3])
		# Down to the left
		if x1 <= 16 and x2 >= 3:
			print ("Top right to bottom right")
			c += 1
			products.append(sequence[x1][x2] * sequence[x1 + 1][x2 - 1] * sequence[x1 + 2][x2 - 2] * sequence[x1 + 3][x2 - 3])
print (products)
print (max(products))
print (len(products))
print (c)
# Answer: 70600674
