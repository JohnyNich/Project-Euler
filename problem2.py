# Fiboncacci numbers
fibonacci_numbers = [1, 2]
even_fibonacci_numbers = []
number = 1
while number < 4000000:
	number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
	fibonacci_numbers.append(number)
for number in fibonacci_numbers:
	if number % 2 == 0:
		even_fibonacci_numbers.append(number)
total = 0
for number in even_fibonacci_numbers:
	total += number
print (fibonacci_numbers)
print (even_fibonacci_numbers)
print (number)
print (total)
print("done")
