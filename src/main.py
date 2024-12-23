import inspect
import math
# import doctestimport unittest

# myList = [0, 1, "a"]
# myList.append(myList)
# print(myList)
# for i in range(len(myList)):
# 	print(i, ":", myList[i], sep = "")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# s = "abc"
# b = s
# s += "d"
# print(s)
# print(b)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# f = open("../var/in5.txt")
# open = 10
# f = open("../var/in5.txt")
# print(open)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# def encloseClosure():  # Could've been called implementAFactoryMethod too.
#     var = 10
#
#     def closure():
#         print("closure: var:", var)
#
#     var += 1
#     var += 1
#
#     return closure
#
## myClosure = encloseClosure()
# myClosure()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# def argumentsExample(positional1, positional2, default1=0, default2="a", *tuple1, **dictionary1):
#     print("positional1:", positional1)
#     print("positional2:", positional2)
#     print("default1:", default1)
#     print("default2:", default2)
#     print("tuple1:", tuple1)
#     print("dictionary1:", dictionary1)
#     print()
#
## tuple2 = 1, 2
# dictionary2 = {"default1": 4, "default2": "b"}
# argumentsExample(5, 6)
# argumentsExample(5, 6, default1=7)
# argumentsExample(*tuple2)
# argumentsExample(1, 2, **dictionary2)
# argumentsExample(2, "b", default2="c", key1="value1", key2=2)
# argumentsExample(*tuple2, **dictionary2)
# argumentsExample(1, 2, 3, "4", 5, 6)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
# def isPrime(n):
#     """
#     Determine if a number is prime.
#     :param n:
#     :return:#
#     >>> isPrime(13)
#     True
#     >>> isPrime(14)
#     False
#     """
#     if not n % 2 or not n % 3:
#         return False
#     root = int(math.sqrt(n))
#     i = 5
#     dx = 4
#     while i <= root:
#         if not n % i:
#             return False
#         dx = -(dx - 6)
#         i += dx
#     return True
#
## print(isPrime(13))
# print(isPrime(133013))
# print(isPrime(133001))
# doctest.testmod()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# def isInteger(n):
#     return int(n) == n
#
## class UnitTestDemo(unittest.TestCase):
#     def testIsInteger(self):
#         self.assertTrue(isInteger(20))
#         self.assertIsNot(isInteger(20.1), True)
#         self.assertEqual(isInteger(3.1), False)
#
## unittest.main(argv=["0"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
#
# list46 = [1, [2], [3, 4], 5, 6, [7, 8], [9]]
# list46Sum = 0
# for e in list46:
#     if type(e) == list:
#         list46Sum += sum(e)
#     else:
#         list46Sum += e
# print("list46Sum:", list46Sum)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep="")
