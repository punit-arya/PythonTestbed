"""PythonTestBed: Python test bed."""

from __future__ import annotations

import compileall
import curses
import datetime
import decimal
import dis
import doctest
import functools
import inspect
import logging
import math
import operator
import os.path
import pathlib
import pprint
import socket
import subprocess
import sys
import time
import timeit
import typing
import unittest
import unittest.mock

import matplotlib.pyplot as mp

# list1 = [0, 1, "a"]
# list1.append(list1)
# print("list1:", list1)
# for i in range(len(list1)):
# 	print(i, ":", list1[i], sep = "")
# 	number1 = 3
# 	if i == number1:
# 		for j in range(len(list1[3])):
# 			print(j, ":", list1[3][j], sep = "")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# string1 = "abc"
# string2 = string1
# string2 += "d"
# print(string2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# file1 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# open = 10
# try:
# 	file2 = open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# except TypeError as ex:
# 	print("TypeError: ", ex, file = sys.stderr)
# file3 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# print(open)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def encloseClosure() -> callable:  # Implements a factory method.
# 	"""Demonstrate closure."""
# 	var1 = 10
#
# 	def closure() -> None:
# 		print("encloseClosure: closure: var1:", var1)
#
# 	var1 += 1
#
# 	return closure
#
#
# closure1 = encloseClosure()
# print("closure1():", closure1())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def argumentsExample(positional1: any, positional2: any, default1: any = 0, default2: any = "a", *tuple1: tuple, **dict1: dict) -> None:
# 	"""Demonstrate the different types of arguments."""
#
# 	print("positional1:", positional1)
# 	print("positional2:", positional2)
# 	print("default1:", default1)
# 	print("default2:", default2)
# 	print("tuple1:", tuple1)
# 	print("dict1:", dict1)
# 	print()
#
#
# tuple2 = 1, 2
# dict2 = {"default1": 4, "default2": "b"}
# argumentsExample(5, 6)
# argumentsExample(5, 6, default1 = 7)
# argumentsExample(*tuple2)
# argumentsExample(1, 2, **dict2)
# argumentsExample(2, "b", default2 = "c", key1 = "value1", key2 = 2)
# argumentsExample(*tuple2, **dict2)
# argumentsExample(1, 2, 3, "4", 5, 6)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def isPrime(dividend: int) -> bool:
# 	"""Determine if a number is prime.
#
#     :param dividend:
#     :return:
#     >>> isPrime(13)
#     False
#     >>> isPrime(14)
#     False"""
#
# 	if not dividend % 2 or not dividend % 3:
# 		return False
# 	root = int(math.sqrt(dividend))
# 	divisor = 5
# 	dx = 4
# 	while divisor <= root:
# 		if not dividend % divisor:
# 			return False
# 		dx = -(dx - 6)
# 		divisor += dx
# 	return True
#
#
# doctest.testmod()
# print(isPrime(13))
# print(isPrime(133013))
# print(isPrime(133001))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def isInteger(number2: float) -> bool:
# 	"""isInteger: return whether a given number is integer."""
#
# 	return int(number2) == number2
#
#
# class UnitTestDemo(unittest.TestCase):
# 	"""UnitTestDemo: my own demo of a unit test."""
#
# 	def testIsInteger(self) -> None:
# 		"""testIsInteger: Just for the sake of it."""
#
# 		# self.assertTrue(isInteger(20))
# 		assert isInteger(20) is True
# 		# self.assertIsNot(isInteger(20.1), True)
# 		assert isInteger(20.1) is not True
# 		# self.assertEqual(isInteger(3.1), False)
# 		assert isInteger(3.1) is not False
#
#
# unittest.main(exit = False)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# list2 = [1, [2], [3, 4], 5, 6, [7, 8], [9]]
# sumOfList2 = 0
# for e in list2:
# 	if type(e) is list:
# 		sumOfList2 += sum(e)
# 	else:
# 		sumOfList2 += e
# print("sumOfList2:", sumOfList2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def diff_method() -> dict:
# 	"""diff_method: return the diff of two files."""
#
# 	# standard_rpms_file = r"D:\Users\punit.arya\src\PythonTestBed\var\standard_rpms.out"
# 	standard_rpms_file = "/home/punit/src/_not_mine/PythonTestBed/var/standard_rpms.out"
# 	# demo_rpms_file = r"D:\Users\punit.arya\src\PythonTestBed\var\demo.txt"
# 	demo_rpms_file = "/home/punit/src/_not_mine/PythonTestBed/var/demo.txt"
# 	try:
# 		process = subprocess.Popen(["/usr/bin/diff", standard_rpms_file, demo_rpms_file], text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# 		out, err = process.communicate()
# 		rc = process.returncode
# 	except (ValueError, OSError) as ex:
# 		out, err = "", str(ex)
# 		rc = -1
# 	return {"out": out.strip(), "err": err.strip(), "returncode": rc}
#
#
# dict3 = diff_method()
# print("diff_method:", dict3["out"], dict3["err"])
#
#
# def set_method() -> None:
# 	"""set_method: evaluate the set method to find diff of two files."""
#
# 	# with open(r"D:\Users\punit.arya\src\PythonTestBed\var\standard_rpms.out") as file4:
# 	with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/standard_rpms.out") as file4:
# 		standard_rpms = file4.readlines()
#
# 	# with open(r"D:\Users\punit.arya\src\PythonTestBed\var\demo.txt") as file5:
# 	with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/demo.txt") as file5:
# 		demo_rpms = file5.readlines()
#
# 	standard_rpms_set = {standard_rpms.strip() for standard_rpms in standard_rpms}
# 	demo_rpms_set = {standard_rpms.strip() for standard_rpms in demo_rpms}
# 	return standard_rpms_set - demo_rpms_set
#
#
# print("set_method:", set_method())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # print(timeit.timeit("diff_method()", setup = "from __main__ import diff_method", number = 1))
# # print(timeit.timeit("set_method()", setup = "from __main__ import set_method", number = 1))
# print(timeit.timeit("diff_method()", setup = "from __main__ import diff_method", number = 1))
# print(timeit.timeit("set_method()", setup = "from __main__ import set_method", number = 1))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # print(os.path.basename("/home/punit/doc/test"))
# # print(os.path.basename("/home/punit/doc/test/"))
# # print(os.path.dirname("/home/punit/doc/test"))
# # print(os.path.dirname("/home/punit/doc/test/"))
# print(pathlib.Path("/home/punit/doc/test").name)
# print(pathlib.Path("/home/punit/doc/test/").name)
# print(pathlib.Path("/home/punit/doc/test").parent)
# print(pathlib.Path("/home/punit/doc/test/").parent)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# yearStart = "1 Jan 2024 5:30 pm +0530"
# dateFormat = "%d %b %Y %H:%M %p %z"
# print(datetime.datetime.now(tz = datetime.timezone(datetime.timedelta(hours = 5.5))))
# print(datetime.datetime.strptime(yearStart, dateFormat).astimezone(datetime.timezone(datetime.timedelta(hours = -1))).strftime("%Y %H %M %z"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# set1 = set(range(1, 10))
# print(set1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # print("argv:", os.path.join(os.path.dirname(sys.argv[0]), "..", "var", "all_rpms.txt"))
# print("argv:", pathlib.Path(pathlib.Path(sys.argv[0]).parent).joinpath("..", "var", "all_rpms.txt"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("socket1:", socket1)
# socket1.connect(("www.python.org", 80))
# print("socket1:", socket1)
# print("socket1.getpeername():", socket1.getpeername())
#
# socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket2.bind((socket.gethostname(), 61000))
# print("socket.gethostname():", socket.gethostname())
# socket2.listen(5)
# print('socket.gethostbyname("python.org"):', socket.gethostbyname("python.org"))
# try:
# 	print('socket.gethostbyaddr("199.232.20.223"):', socket.gethostbyaddr("199.232.20.223"))
# except socket.herror as ex:
# 	print(sys.exc_info()[0].__name__ + ":", ex, "\n")
# print('socket.gethostbyaddr("223.233.66.174"):', socket.gethostbyaddr("223.233.66.174"))
# print('socket.gethostbyaddr("223.233.66.174"):', socket.gethostbyaddr("223.233.66.174")[0])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def myPager(content: str, numberLines: int) -> None:
# 	"""myPager: page me."""
#
# 	lines = content.split(sep = "\n")
# 	while lines:
# 		page = lines[:numberLines]
# 		for l in page:
# 			print(l)
# 		lines = lines[numberLines:]
# 		if lines and input("More ? ") not in ["Y", "y"]:
# 			return
#
#
# if __name__ == "__main__":
# 	# with pathlib.Path.open(r"C:/Users/T0311408/src/PythonTestBed/var/demo.txt") as file6:
# 	with pathlib.Path.open(r"/home/punit/src/_not_mine/PythonTestBed/var/demo.txt") as file6:
# 		myPager(file6.read(), 60)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
#
# def function1(a: int | str) -> None:
# 	"""function1: testing union types in function annotations."""
# 	print(a)
#
#
# function1(1)
# function1("a")
# function1(2.3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# print([1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # #MIRAGE-CLIENT@MATRIX.ORG:
# print(hex(ord(b"\xef\x8f\x8f".decode("utf-8"))))
# print(chr(ord(b"\xef\x8f\x8f".decode("utf-8"))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# print(sys.platform)
# print(os.getuid())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# LOG_FILE_HANDLER = logging.FileHandler("/tmp/install_compass1.log")
# LOG = logging.getLogger()
# LOG.addHandler(LOG_FILE_HANDLER)
# LOG.setLevel("INFO")
# LOG.info("infomessage")
# LOG.debug("debugmessage")
# LOG.setLevel("DEBUG")
# LOG.debug("debugmessage1")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # _MINE.
#
# print(inspect.getfile(os))
# print(inspect.getfile(os.path))
# print(inspect.getfile(os.path.samestat))
# print(inspect.getfile(os.path.genericpath.samestat))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# #
#
# w, h = 2, 3
# list23 = [[None] * w for _ in range(h)]
# list99 = [*[[None] * w] * h]
# print(list23)
# print(list99)
# if list23 == list99:
# 	print("It's a match.")
# else:
# 	print("Oh, no!")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # MINE.
#
#
# def function44(number43: int) -> None:
# 	string43 = "spam"
# 	print("string43:", string43)
# 	return string43 * number43
#
#
# for l in function44.__code__.co_lines():
# 	print("l:", l)
#
# for l in inspect.getsourcelines(function44):
# 	print("l:", l)
#
# print("function44.__code__.co_code:")
# for i, l in enumerate(function44.__code__.co_code):
# 	print("i:", i, "l:", l)
#
# compileall.compile_file("/home/punit/src/_not_mine/PythonTestBed/src/main.py")
#
# print("dis.dis(function44):")
# print(dis.dis(function44))
#
# # MINE.
#
#
# def function45():
# 	pass
#
#
# [print(e) for e in dir(function45) if e.startswith("__")]
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# MINE
# print(print(print()))
#
# print(*list(map(lambda n: n ** 2, filter(lambda n: operator.imod(n, 2) == 0, range(0, 10)))))
#
# print({chr(i + 65): i + 65 for i in range(10) if i % 2 == 0 for i in range(26) if i % 2 == 1})
# print({chr(i + 65): i + 65 for i in range(26) if i % 2 == 0 for i in range(10) if i % 2 == 1})
# print([i for i in range(10) if i % 2 == 0 for i in range(26) if i % 2 == 1])  # Value of i that is printed is from the inner loop.  65 elements.  Outer loop only tells the number of iterations to run.  Odd numbers only.
# print([i for i in range(26) if i % 2 == 0 for i in range(10) if i % 2 == 1])  # 65 elements.  Odd numbers only.
# print([i for i in range(26) if i % 2 == 1 for i in range(10) if i % 2 == 0])  # Even numbers only.  65 elements.
#
# list120 = []
# for i in range(26):
# 	if i % 2 == 1:
# 		for i in range(10):
# 			if i % 2 == 0:
# 				list120.append(i)
# print(list120)

# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# list96 = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
# list97 = [[2, 2, 2], [3, 3, 3, 3], [4, 4, 4]]
# list98 = [list96[i][j] ** list97[i][j] for i in range(len(list96)) for j in range(len(list96[i]))]
# print("list98:", list98)
#
#
# def generatorFunction3():
# 	for i in range(10):
# 		j = yield i
# 		print(j)
#
#
# generator3 = generatorFunction3()
# print(next(generator3))
# print(generator3.send(77))
# print(generator3.send(88))
# print(next(generator3))
# print(next(generator3))
# print(next(generator3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# string1 = "abc"
# string2 = "xzy123"
# string3 = "jkl12345"
# print(list(zip(string1, string2, string3)))  # Truncates the shorter two strings.
#
# print(map(abs, [-2, -1]))
# a = map(abs, [-1, -2])
# print(a)
# b = (c.upper() for c in "spam")
# print(b)
# print(type(a) is type(b))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# mapObject = map(pow, [1, 2, 3], [1, 2, 3])
# for i in mapObject:
# 	print("i:", i)
# try:
# 	print(next(mapObject))
# except StopIteration as ex:
# 	print(inspect.getframeinfo(inspect.currentframe()).lineno, ": ex:", ex)
# for i in mapObject:
# 	print("i:", i)
# try:
# 	print(next(mapObject))
# except StopIteration as ex:
# 	print(inspect.getframeinfo(inspect.currentframe()).lineno, ": ex:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# MINE
# generatorObject1 = (a for a in [1, 2, 3])
# print("generatorObject1:", generatorObject1)
# set1 = set(generatorObject1)  # Works because set initalizer expects any iterable.
# print("set1:", set1)
#
# generatorObject2 = ((k, k ** 2) for k in [1, 2, 3])  # Dictionary initializer expects iterable of tuples.
# print("generatorObject2:", generatorObject2)
# dict1 = dict(generatorObject2)
# print("dict1:", dict1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP, MINE
#
#
# def timer(func, *args):
# 	# start = time.clock()
# 	start = time.time()
# 	for i in range(1000):
# 		func(*args)
# 	# return time.clock() - start
# 	return time.time() - start
#
#
# print(timer(lambda i: i ** i, 20000))
#
# timer = time.clock if sys.platform[: 3] == "win" else time.time
#
#
# def total(reps, function, *positionals, **keywords):
# 	repslist = list(range(reps))
# 	start = timer()
# 	for i in repslist:
# 		retval = function(*positionals, **keywords)
# 	elapsed = timer() - start
#
# 	return (elapsed, retval)
#
#
# def bestof(reps, function, *positionals, **keywords):
# 	best = 2 ** 32
# 	for i in range(reps):
# 		start = timer()
# 		retval = function(*positionals, **keywords)
# 		elapsed = timer() - start
# 		if elapsed < best:
# 			best = elapsed
#
# 	return (best, retval)
#
#
# def bestoftotal(reps1, reps2, function, *positionals, **keywords):
# 	return bestof(reps1, total, reps2, function, *positionals, **keywords)
#
#
# val1 = total(1000, pow, 2, 1000)[0]
# print("total(1000, pow, 2, 1000)[0]:", val1)
# val2 = total(1000, str.upper, "spam")[0]
# print("total(1000, str.upper, 'spam')[0]:", val2)
# print(decimal.Decimal(val1).normalize())
# print(decimal.Decimal(val2).normalize())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# UNKNOWN
# def foo():
# 	for i in range(5):
# 		print("a")
# 	one = 10
# 	two = 20
# 	return one
#
#
# def function100():
# 	pass
#
#
# def function101():
# 	var = 2
# 	return var
#
#
# function100 = 0
# print(function100)
# var10 = 1
# function100 = var10
# print(function100)
# function100 = function101()
# print(function100)

# ispy3 = False
# string20 = "A $listif3 B"
# string20 = string20.replace("$listif3", "list" if ispy3 else "")
# print(string20)
#
# ispy3 = False
# string20 = "A$listif3B"
# string20 = string20.replace("$listif3", "list" if ispy3 else "")
# print(string20)
#
# ispy3 = True
# string20 = "Alistif3B"
# string20 = string20.replace("listif3", "list" if ispy3 else "")
# print(string20)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# YOUTUBE VIDEO
# total = 0
# for i in range(1, 100_000_001):
# 	total += i
#
# print(total)

# YOUTUBE VIDEO
# var100 = 50
# print(sys.getsizeof(var100), "bytes")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# def f1(a, b):
# 	print("f1:", "a:", a, "b:", b)
#
#
# def f2(a, *b):
# 	print("f2:", "a:", a, "b:", b)
#
#
# def f3(a, **b):
# 	print("f3:", "a:", a, "b:", b)
#
#
# def f4(a, *b, **c):
# 	print("f4:", "a:", a, "b:", b, "c:", c)
#
#
# def f5(a, b = 2, c = 3):
# 	print("f5:", a, b, c)
#
#
# def f6(a, b = 2, *c):
# 	print("f6:", a, b, c)
#
#
# f1(1, 2)
# f1(b = 2, a = 1)
# f2(1, 2, 3)
# f3(1, x = 2, y = 3)
# f4(1, 2, 3, x = 2, y = 3)
# f5(1)
# f6(1)
# f6(1, 3, 4)
#
# dict101 = {"a": 1, "b": 2}
# print(dict101)

# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# print(functools.reduce(lambda a, b: a * b, range(1, 7)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# A 5-by-10 ARRAY OF 3-ELEMENT LISTS.

# array = [[[[0, 0, 0]] * 10] * 5] * 3
# # pprint.pprint(array)
# for i in range(3):
# 	for j in range(5):
# 		for k in range(10):
# 			if i == 0:
# 				array[i][j][k] = [0, 0, 255]
# 			elif i == 1:
# 				array[i][j][k] = [0, 255, 0]
# 			elif i == 2:
# 				array[i][j][k] = [255, 0, 0]
# 			else:
# 				print("UNPOSSIBLE!")
# pprint.pprint(array)

# array1 = [0] * 3  # List of ten elements.
# print(array1)
# array2 = [[0] * 3]  # List with only one element.
# print(array2)
# array3 = [[0] * 3] * 5  # List with 5 elements, each element a 10-element list.
# print(array3)
# array4 = [[[0] * 3] * 5]  # Same as above, but a single-element list containing the above.
# print(array4)
# array5 = [[[0] * 3] * 5] * 10  # Same as above, but a single-element list containing the above.
# print(array5)

# pixel = [0, 0, 0]
# # image = pixel[5][10]
# # image[1][2] = [255, 0, 0]
# image = [[pixel] * 5] * 10
# # image[1][2] = [255, 255, 0]
# print(image[1][2])
# print(image[1][2][3])
# pprint.pprint(image)

# pixel = [0, 0, 0]
# image = [[pixel] * 5 for _ in range(10)]
# pprint.pprint(image)
# image[0][1] = [255, 0, 255]
# # pprint.pprint(image)
# mp.imshow([[0, 255, 255] * 5] * 10)

# print(type(sys.modules))
# print(sys.modules)

print(sys.path)
