# Largest palindrome product
import time
palindrome = []
for n in range(100, 999):
	for n2 in range(100, 999):
		product = n * n2
		if len(str(product)) == 5:
			print (product)
			print (str(product)[:2])
			print (str(product)[:2:-1])
			if str(product)[:2] == str(product)[:2:-1]:
				print ("match 5 length")
				palindrome.append(product)
		else: # The only other possibility is if the length is 6, as the length of 999*999 is 6.
			print (n)
			print (n2)
			print (product)
			if str(product) == str(product)[::-1]:
				print ("match 6 length")
				palindrome.append(product)
print (max(palindrome))
