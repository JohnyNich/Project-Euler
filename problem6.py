square1 = range(1,101)
square2 = range(1,101)
sum1 = 0
sum2 = 0
for number in square1:
	sum1 += number**2
for number in square2:
	sum2 += number
sum2 = sum2**2
final = sum2 - sum1
print (final)
