def fib(number1: int) -> int:
	a, b = 0, 1
	while b < number1:
		print(b, end = " ")
		a, b = b, a + b
	print()


def fib1(number2: int) -> int:
	result = []
	a, b = 0, 1
	while b < number2:
		result.append(b)
		a, b = b, a + b
	return result
