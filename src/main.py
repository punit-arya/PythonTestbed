"""Test bed."""

# import curses
# import curses.wrapper
import datetime
import inspect
import math
<<<<<<< HEAD
# import doctestimport unittest
=======
import os.path
import pathlib
import socket
import subprocess
import sys
import timeit

# import doctest
import unittest
>>>>>>> 3b88eaa7c9d995f8fb0be47ccde29d2198e4bafa

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


# def diff_method():
#     rpm_file = r"D:\Users\punit.arya\src\PythonTestBed\var\rpm.out"
#     demo_rpms_file = r"D:\Users\punit.arya\src\PythonTestBed\var\demo.txt"
#     try:
#         ps = subprocess.Popen(
#             "diff " + rpm_file,
#             " " + demo_rpms_file,
#             text=True,
#             shell=True,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#         )
#         out, err = ps.communicate()
#         rc = ps.returncode
#     except Exception as e:
#         out, err = "", str(e)
#         rc = -1
#     return {"out": out.decode().strip(), "err": err.decode().strip(), "returncode": rc}
#
#
# def set_method():
#     with open(r"D:\Users\punit.arya\src\PythonTestBed\var\rpm.out") as f:
#         standard_rpms = f.readlines()
#
#     with open(r"D:\Users\punit.arya\src\PythonTestBed\var\demo.txt") as f:
#         demo_rpms = f.readlines()
#
#     standard_rpms_set = set()
#     for rpm in sorted(standard_rpms):	# Use a set comprehension instead.
#         standard_rpms_set.add(rpm.strip())
#
#     demo_rpms_set = set()
#     for rpm in sorted(demo_rpms):
#         demo_rpms_set.add(rpm.strip())
#
#     nonstandard_rpms_set = standard_rpms_set - demo_rpms_set

    # for pkg in nonstandard_rpms_set:
    #     print(pkg)


# print(timeit.timeit("set_method()", setup="from __main__ import set_method", number=1))
# print(
#     timeit.timeit("diff_method()", setup="from __main__ import diff_method", number=1)
# )


# print("123456"[:-3])
#
# print(os.path.basename("/home/punit/doc/test"))
# print(os.path.basename("/home/punit/doc/test/"))
# print(os.path.dirname("/home/punit/doc/test"))
# print(os.path.dirname("/home/punit/doc/test/"))
#
# # yearStart = "1 Jan 2024"
# # dateFormat = "%b %m %Y"
# print(datetime.datetime.now())
#
# mySet = set()
# for i in range(1, 10):
# 	mySet.add(i)
# print(mySet)
#
# mySet = {i for i in range(1, 10)}
# print(mySet)

# print("argv:", os.path.join(os.path.dirname(sys.argv[0]), "..", "var", "all_rpms.txt"))

# def conv(s, numRows):
# 	pass

# stdscr = curses.initscr()
#
# def main(stdscr):
# 	stdscr.clear()
#
# 	for i in range(11):
# 		v = i - 10
# 		stdscr.addstr(i, 0, "10 divided by {} is {}".format(v, 10/v))
#
# 	stdscr.refresh()
# 	stdscr.getkey()
#
# curses.wrapper(main)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("www.python.org", 80))
# print("s:", s)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((socket.gethostname(), 61000))
# # print("socket.hostname():", socket.gethostname())
# server_socket.listen(5)
# print("socket.gethostbyname('python.org'):", socket.gethostbyname("python.org"))
# print("socket.gethostbyaddr('199.232.20.223'):", socket.gethostbyaddr("199.232.20.223"))
# print("socket.gethostbyaddr('223.233.66.174'):", socket.gethostbyaddr("223.233.66.174"))
# print("socket.gethostbyaddr('223.233.66.174'):", socket.gethostbyaddr("223.233.66.174")[0])


print(sys.__doc__)


def myPager(content: str, numberLines: int) -> None:
	"""myPager: page me."""
	lines = content.split(sep = "\n")
	while lines:
		page = lines[:numberLines]
		for line in page:
			print(line)
		lines = lines[numberLines:]
		if lines and input("More ? ") not in ["Y", "y"]:
			return

if __name__ == "__main__":
	with pathlib.Path.open(r"C:/Users/T0311408/src/PythonTestBed/var/demo.txt") as f:
		myPager(f.read(), 100)
