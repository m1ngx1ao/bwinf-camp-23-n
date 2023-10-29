def facu(number: int):
	if number == 0:
		return 1
	return number * facu(number - 1)

#print(facu(12))
print(facu(1))

d = {}

a = [None] * 5

def fibo(number: int):
	if number == 0:
		return 0
	if number == 1:
		return 1
	if number in d:
		return d[number]
	result = fibo(number - 1) + fibo(number - 2)
	d[number] = result
	return result

print(fibo(50))
	