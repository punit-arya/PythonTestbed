"""PythonTestBed: Python test bed."""

from __future__ import annotations

import contextlib
import curses
import datetime
import doctest
import inspect
import logging
import math
import os.path
import pathlib
import socket
import dis
import compileall
import subprocess
import sys
import timeit
import typing
import unittest
import unittest.mock

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
# with contextlib.suppress(socket.herror):
# 	print('socket.gethostbyaddr("199.232.20.223"):', socket.gethostbyaddr("199.232.20.223"))
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

# MINE.


def function44(number43: int) -> None:
	string43 = "spam"
	print("string43:", string43)
	return string43 * number43


for l in function44.__code__.co_lines():
	print("l:", l)

for l in inspect.getsourcelines(function44):
	print("l:", l)

print("function44.__code__.co_code:")
for i, l in enumerate(function44.__code__.co_code):
	print("i:", i, "l:", l)

compileall.compile_file("/home/punit/src/_not_mine/PythonTestBed/src/main.py")

print("dis.dis(function44):")
print(dis.dis(function44))

# MINE.


def function45():
	pass


[print(e) for e in dir(function45) if e.startswith("__")]

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

print(print(print()))
