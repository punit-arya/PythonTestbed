"""adder: return the sumTotal or concatenation of two arguments."""

# def adder(var1, var2):
# 	return var1 + var2
#
#
# def adder(*operands):
# 	if type(operands[0]) is list:
# 		sumTotal = []
# 	elif type(operands[0]) is str:
# 		sumTotal = ""
# 	else:
# 		sumTotal = 0
# 	for operand in operands:
# 		sumTotal += operand
# 	return sumTotal

# def adder(*operands):
# 	sumTotal = operands[: 0]
# 	if type(operands[0]) is list:
# 		sumTotal = []
# 	elif type(operands[0]) is str:
# 		sumTotal = ""
# 	else:
# 		sumTotal = 0
# 	for operand in operands:
# 		sumTotal += operand
# 	return sumTotal

# def adder(*operands):
# 	sumTotal = operands[0]
# 	for operand in operands[1 :]:
# 		sumTotal += operand
# 	return sumTotal

# adder(1, 2)
# adder("A", "B")
# adder([0, 1], [2, 3])
# adder(0.1, 0.01)

# print("adder(1, 2):", adder(1, 2))
# print("adder('A', 'B'):", adder("A", "B"))
# print("adder([0, 1], [2, 3]):", adder([0, 1], [2, 3]))
# print("adder(0.1, 0.01):", adder(0.1, 0.01))
# try:
# 	print("adder({'a': 1, 'b': 2}, {'c': 2, 'd': 3}):", adder({"a": 1, "b": 2}, {"c": 2, "d": 3}))
# except TypeError as ex:
# 	print("ex:", ex)
# try:
# 	print("adder({'a','b'}, {'c', 'd'}):", adder({"a", "b"}, {"c", "d"}))
# except TypeError as ex:
# 	print("ex:", ex)
# try:
# 	print("adder({'a','b'}, {'c': 0, 'd': 1}):", adder({"a", "b"}, {"c": 0, "d": 1}))
# except TypeError as ex:
# 	print("ex:", ex)
# try:
# 	print("adder(0, 1, 2, [3, 4]):", adder(0, 1, 2, [3, 4]))
# except TypeError as ex:
# 	print("ex:", ex)
# try:
# 	print("adder(0, 1, 2, '3'):", adder(0, 1, 2, "3"))
# except TypeError as ex:
# 	print("ex:", ex)

# def adder(good = 0, bad = 1, ugly = 2):
# 	return good + bad + ugly
#
#
# print("adder(1, 2, 3):", adder(1, 2, 3))
# print("adder(1, 2):", adder(1, 2))
# print("adder(1, 2, 3):", adder(1, 2, 4))
# print("adder(1, 2):", adder(bad = 1, good = 2))

# def adder(**cast):
# 	sumTotal = 0
# 	for v in cast.values():
# 		sumTotal += int(v)
# 	return sumTotal
#
#
# print("adder(1, 2):", adder(good = 1, bad = 2))
# print("adder(1, 2, 3):", adder(good = 1, bad = 2, ugly = 3))
# print("adder(1, 2, 3):", adder(good = 1, bad = 2, ugly = 3, terrible = 4))
