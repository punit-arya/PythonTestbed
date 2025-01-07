#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""PythonTestBed: Python test bed."""

from __future__ import annotations
import __future__

import array
import ast
import bisect
import builtins
import cmath
import collections
import contextlib
import copy
import csv
import datetime
import dbm
import decimal
import doctest
import email.mime.text
import fractions
import functools
import gc
import glob
import heapq
import importlib
import inspect
import io
import json
import locale
import logging
import math
import os
import pathlib
import pickle
import platform
import pprint
import py_compile
import queue
import random
import re
import readline
import reprlib
import shutil
import site
import statistics
import string
import struct
import sys
import textwrap
import threading
import time
import timeit
import typing
import unittest
import urllib.request
import weakref
import zipfile
import zlib

import circularImport
import config
import docstrings
import fibo
import module1
import module2
import module3
import module4
import module5

# TUTORIAL.

the_world_is_flat = True
if the_world_is_flat:
	print("Be careful not to fall off!")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(17 / 3)
print(17 // 3)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(-(3 ** 2))
print((-3) ** 2)
print(5 ** 2)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

s = "First line.\nSecond line."
print(s)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print("C:\some\name")
print(r"C:\some\name")  # Note the ~r~ before the quote

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print("""\
Usage: thingy [OPTIONS]
		-h				Display this usage message
		-H	hostname	Hostname to connect to
""")  # If we don't escape the newline there, it become embedded in the string.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(3 * "un" + "ium")

print("Py"
"thon")  # Concatenation.Works with literals only, no variables or expressions.Works across literal newline characters if enclosed within parentheses.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

prefix = "Py"
# print(prefix "thon")
# print(("un" * 3) "ium")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(prefix + "thon")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

text = "Put several strings within parentheses " "to have them joined together."
print(text)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

word = "Python"
print(word[0])
print(word[-1])
print(word[0:2])
print(word[:2] + word[2:])
print(word[4:42])
print(word[42:])
# word[0] = "J"
print("J" + word[1:])

word1 = [[0, 1], [2, 3], [4, 5]]
print(word1[1])
word1[1] = [10, 11]
print(word1[1])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

s = "supercalifragilisticexpialidocious"
print(len(s))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
squares = squares + [36, 49, 64, 81, 100]
print(squares)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
print(cubes.append(216))
cubes.append(7 ** 3)  # Add the cube of 7.
print(cubes)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
letters[2:5] = ["C", "D", "E"]
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ["a", "b", "c", "d"]
print(len(letters))
a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a + b

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a, b = 0, 1
while b < 1000:
	print(b, end = ",")  # Don't append a newline to output, instead replace it with ",".  "end" is a keyword.
	a, b = b, a + b
print()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

x = int(input("Integer ? "))
if x < 0:
	x = 0
	print("Negative changed to zero.")
elif x == 0:
	print("Zero.")
elif x == 1:
	print("Single.")
else:
	print("More")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

words = ["cat", "window", "defenestrate"]
for w in words:  # "for" iterates over the items of any sequence (a list or a string).This form can not modify the items.
	print(w, len(w))

for w in words[:]:  # Makes a copy of "words" to enable modification.
	if len(w) > 6:
		words.insert(0, w)
print(words)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for i in range(5):
	print(i)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):  # Use "enumerate()" function instead.
	print(i, a[i])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(range(10))  # "range(0, 10)" Doesn't work because range doesn't return a list.  Instead, it returns an iterator object to save space.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(list(range(5)))  # Creates list from iterables.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, "equals", x, "*", n // x)
			break
		else:
			print(n, "is a prime number")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

# while True:
# 	pass

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class MyEmptyClass:
	pass


print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def initlog(*args: None) -> None:
	pass


print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def fib(number1: int) -> None:
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < number1:
		print(a, end = " ")
		a, b = b, a + b
	print()


fib(2000)
print(fib)
f = fib
print(f(100))
fib(0)
print(fib(0))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def fib2(number2: int) -> int:
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < number2:
		result.append(a)
		a, b = b, a + b
	return result


f100 = fib2(100)
print(f100)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def ask_ok(prompt: str, retries: int = 4, reminder: str = "Please try again!") -> bool:
	while True:
		ok = input(prompt)
		if ok in ("y", "ye", "yes"):  # "in" is a keyword.  Tests whether a value is in a sequence.
			return True
		if ok in ("n", "no", "nop", "nope"):
			return False
		retries = retries - 1
		if retries < 0:
			errorMessage = "invalid user response"
			raise ValueError(errorMessage)
		print(reminder)


print(ask_ok("Do you really wanna quit ? "))
print(ask_ok("OK to overwrite the file ? ", 2))
print(ask_ok("OK to overwrite the file ? ", 2, "Come on, only yes or no!"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

i = 5


def f(arg = i):
	print(arg)


i = 6
f()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def f(number1, list30 = []):
	list30.append(number1)
	return list30


print(f(1))
print(f(2))
print(f(3, [4, 5]))
print(f(6, [7, 8]))
print(f(3, [4, 5]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def f(number2, list31 = None):
	if list31 is None:
		list31 = []
	# def f(number2, list31=[]):
	list31.append(number2)
	return list31


print(f(1))
print(f(2))
print(f(3))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


# "parrot" accepts one positional argument (the value of this argument is taken from the module1 argument in the function call) and three keyword (or optional) arguments.
def parrot(voltage, state = "a stiff", action = "voom", type = "Norwegian Blue"):
	print("-- This parrot wouldn't", action, end = " ")
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")


parrot(1000)  # 1 positional argument.
parrot(voltage = 1000)  # 1 keyword argument.
parrot(voltage = 1000000, action = "VOOOOOM")  # 2 keyword arguments.
parrot(action = "VOOOOOM", voltage = 1000000)  # 2 keyword arguments.
parrot("a million", "bereft of life", "jump")  # 3 positional arguments.
parrot("a thousand", state = "pushing up the daisies")  # 1 positional, 1 keyword.
# parrot()
# parrot(voltage = 5.0, "dead")	# Invalid call because "dead" is a non-keyword argument so should be at the module1 position.  i.e., keyword arguments must follow positional arguments.
# parrot(110, voltage = 220)	# Invalid, because duplicate values for same argument.
# parrot(actor = "John Cleese")	# Keyword argument name is misspelt.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def cheeseshop(kind: str, *arguments: tuple, **keywords: dict) -> None:
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper = "Michael Palin", client = "John Cleese", sketch = "Cheese Shop Sketch")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def concat(*args, sep = "/"):
	return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep = "."))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def parrot(voltage: str, state: str = "a stiff", action: str = "voom") -> None:
	print("-- This parrot wouldn't", action, end = " ")
	print("if you put", voltage, "volts through it.", end = " ")
	print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def make_incrementor(number1: int) -> None:
	return lambda x: x + number1


f = make_incrementor(42)  # "make_incrementor" makes and returns the adder and assigns to "f" which is a reference to a function.
print(f(0))  # Calling "f" with "0", calls the lambda function and assigns the "0" argument to "x".  0 = x, 42 = n.
print(f(1))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]  # Two-dimensional array: four rows, two columns.
pairs.sort(key = lambda pair: pair[1])  # "sort" takes no arguments, or one argument which should be a lambda function.  This lambda function should return the key.  The elements of the "pairs" array is passed as an argument to the lambda function that is known as "pair" inside the lambda function.  In other words, the key argument can take a lambda function which returns a key.  Key can be a subscript if each element is an array or dot-notation attribute access if each element is an object (this will mean that the list is a collection of objects).
print(pairs)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def function88() -> None:
	"""Do nothing, but document it.

    No, really, it doesn't do anything."""


print(function88.__doc__)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def f(ham: str, eggs: str = "eggs") -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + " and " + eggs


print(f("spam"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

list24 = [10, 11, 12, 13, 14, 10]
print("list24:", list24)
print("list24.count(10):", list24.count(10), "list24.count(14):", list24.count(14), "list24.count(\"x\"):", list24.count("x"))
print("list24.insert(2, 11.5):", list24.insert(2, 11.5))  # 11.5 will be inserted at the index 2.  ~list24.insert(len(list24), element)~ is same as ~list24.append(element)~.
print("list24:", list24)
print("list24.append(15):", list24.append(15))  # Equivalent to: "list24[len(list24):] = [element]"
print("list24:", list24)
print("list24.index(15):", list24.index(15))  # Return the index of the item 15.
print("list24.remove(15):", list24.remove(15))  # Removes the module1 occurrence of 15.  Returns an error if the element is not found.
print("list24:", list24)
print("list24.reverse():", list24.reverse())  # Reverse the elements of the list in place.
print("list24:", list24)
print("list24.sort():", list24.sort())
print("list24:", list24)
print("list24.pop():", list24.pop())  # If argument to ~pop~ is not given, it removes and returns the last item in the list.
print("list24:", list24)
print("list24.extend(list24):", list24.extend(list24))  # Equivalent to: list[len(list24):] = list25
print("list24:", list24)
print("list24.count(10):", list24.count(10))  # Return the number of times 10 appears in the list.
print("list24:", list24)
print("list24.sort(key=None, reverse=False):", list24.sort(key = None, reverse = False))  # Sort the items of the list in place.  See ~sorted()~ for explanation of the optional arguments.
print("list24.pop(2):", list24.pop(2))  # List passed instead of integer.
print("list24:", list24)
print("list24.clear():", list24.clear())  # Equivalent to ~del list24[:]~.
print("list24:", list24)
copyOfA = list24.copy()  # Return a shallow copy of the list.  Equivalent to ~list24[:]~.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

myQueue = collections.deque(["Eric", "John", "Michael"])
myQueue.append("Terry")
myQueue.append("Graham")
print(myQueue.popleft())
print(myQueue.popleft())
print(myQueue)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

squares = []
for x in range(10):
	squares.append(x ** 2)
print(squares)
print(x)

for i in range(3):
	for j in range(4):
		for k in range(5):
			print("i, j, k:", i, j, k)
print(i, j, k)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

squares = list(map(lambda x: x ** 2, range(10)))  # Equivalent.  List comprehension.
print(squares)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

squares = [x ** 2 for x in range(10)]
print(squares)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])  # Equivalent to:

combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))
print(combs)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ["	 banana", "  loganberry ", "passion fruit  "]
print([weapon.strip() for weapon in freshfruit])
print([(x, x ** 2) for x in range(6)])  # To create a list of tuples.
print([x, x ** 2] for x in range(6))
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])  # Flatten a list of tuples using listcomp.
print([str(round(math.pi, i)) for i in range(1, 6)])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print(transposed)
transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
print(transposed)
print(list(zip(*matrix)))  # Better than listcomp.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a  # Deletes entire variable.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

t = 12345, 54321, "hello!"
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
print(t[0])
v = ([1, 2, 3], [3, 2, 1])
print(v)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

empty = ()
singleton = ("hello",)
print(len(empty))
print(len(singleton))
print(singleton)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

t = 12345, 54321, "hello!"  # Packing a tuple.
print(t)
x, y, z = t  # Unpacking a tuple.  This can work for any sequence.
print(x, y, z)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)
print("orange" in basket)
print("crabgrass" in basket)
a = set("abracadabra")
b = set("alacazam")
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
a = {x for x in "abracadabra" if x not in "abc"}
print(a)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)
print(tel["jack"])
del tel["sape"]
tel["irv"] = 4127
print(tel)
print(list(tel.keys()))  # List of all keys in arbitrary order.
print(sorted(tel.keys()))  # Sorted keys.
print("guido" in tel)
print("jack" not in tel)
print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
print({x: x ** 2 for x in (2, 4, 6)})  # Dict comprehensions.
print(dict(sape = 4139, guido = 4127, jack = 4098))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
	print(k, v)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for i, v in enumerate(["tic", "tac", "toe"]):
	print(i, v)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
	print("What is your {}?  It is {}.".format(q, a))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for i in reversed(range(1, 10, 2)):
	print(i)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for f in sorted(set(basket)):  # "sorted" takes any sequence and returns a new list.
	print(f)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filtered_data = []
for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)
print(filtered_data)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

string1, string2, string3 = "", "Trondheim", "Hammer Dance"
non_null = string1 or string2 or string3
print(non_null)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print("ABC" < "C" < "Pascal" < "Python")
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ("aa", "ab")) < (1, 2, ("abc", "a"), 4))
# print((1, 2, 3) < [1, 2, 4])
print(1 / 3 <= 100 / 300)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib
print(fib(500))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

if __name__ == "__main__":
	print(fib(int(sys.argv[1])))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

# print(sys.ps1)
# print(sys.ps2)
# sys.ps1 = "C> "
# print(sys.ps1)
sys.path.append("/home/punit/lib/python")
print(sys.path)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print("dir(fibo):", dir(fibo))
print("dir(sys):", dir(sys))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a = [1, 2, 3, 4, 5]
fib = fibo.fib
print("dir():", dir())
print("dir(builtins):", dir(builtins))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(str(1))
print(str(1.0))
print(str(1.1))
print(str("ab"))
print(str((1, 2, 3)))
print(str([1, 2, 3]))
print(str({1, 2, 3, 1}))
print(str({"a": 1, "b": 2}))
print(repr(1))
print(repr(1.0))
print(repr(1.1))
print(repr("ab"))
print(repr((1, 2, 3)))
print(repr([1, 2, 3]))
print(repr({1, 2, 3, 1}))
print(repr({"a": 1, "b": 2}))
s = "Hello, world!"
print(repr(s))
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = "Value of x is " + repr(x) + " and y is " + repr(y) + "..."
print(s)
hello = "Hello, world!\n"
hellos = repr(hello)
print(hellos)
print(repr((x, y, ("spam", "eggs"))))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for x in range(1, 11):
	print(repr(x).rjust(2), repr(x * x).rjust(3), end = " ")
	print(repr(x * x * x).rjust(4))

for x in range(1, 11):
	print(f"{x:2d} {x * x:3d} {x * x * x:4d}")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print("12".zfill(5))
print("-3.14".zfill(7))
print("3.14159265359".zfill(5))
print("We are the {} who say \"{}!\"".format("knights", "Ni"))
print("{} and {}".format("spam", "eggs"))
print("{} and {}".format("spam", "eggs"))
print("This {food} is {adjective}.".format(food = "spam", adjective = "absolutely horrible"))
print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other = "George"))
contents = "eels"
print(f"My hovercraft is full of {contents}.")
print(f"My hovercraft is full of {contents:!r}.")
print(f"My hovercraft is full of {contents:!s}.")
print(f"My hovercraft is full of {contents:!a}.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(f"Value of PI is approximately {math.pi:.3f}.")

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
	print(f"{name:10} ==> {phone:10d}")

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637378}
print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}: Dcab: {0[Dcab]:d}".format(table))

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(f"The value of PI is approximately {math.pi:5.3f}.")

with pathlib.Path.open("../../var/in.txt") as f:
	print("1:", f.read())
	print("2:", f.read())
	print("3:", f.readline())

with pathlib.Path.open("../../var/in.txt") as f:
	for line in f:
		print(line, end = "")

f = pathlib.Path.open("../../var/out.txt", "w")
f.write("This is a test\n")
value = ("the answer", 42)
s = str(value)
print("s:", s)
f.write(s)
f.close()

with pathlib.Path.open("../../var/out.txt", "rb+") as f:
	print(f.write(b"0123456789abcdef"))
	print(f.seek(5))
	print(f.read(1))
	print("seek:", f.seek(-3, 2))
	print("read:", f.read(1))
	f.close()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

with pathlib.Path.open("../../var/in.txt") as f:
	read_data = f.read()
print(f.closed)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(json.dumps([1, "simple", "list"]))
with pathlib.Path.open("../../var/out1.txt", "w") as f:
	x = [1, "simple", "list"]
	json.dump(x, f)
	f.close()
with pathlib.Path.open("../../var/out1.txt") as g:
	y = json.load(g)
	print(y)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops! Invalid number.")
	except (RuntimeError, TypeError, NameError):
		pass

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class BError(Exception):
	pass


class CError(BError):
	pass


class DError(CError):
	pass


try:
	for MyClass in [BError, CError, DError]:
		raise MyClass()
except DError:
	print("DError")
except CError:
	print("CError")
except BError:
	print("BError")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

while True:
	try:
		with pathlib.Path.open("../../var/in1.txt") as f:
			s = f.readline()
			i = int(s.strip())
	except OSError as e:
		print(f"OS error: {e}.")
	except ValueError:
		print("Could not convert data to an integer.")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise
	break

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

try:
	for arg in sys.argv[2:]:
		with pathlib.Path.open(arg) as f:
			pass
except OSError:
	print("can not open", arg)
else:
	print(arg, "has", len(f.readlines()), "lines")
	f.close()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

try:
	errorMessage = "spam", "eggs", "thisIsATuple"
	raise Exception(errorMessage)  # When we raised this exception, these arguments got packed into a tuple.
except Exception as exceptionInstance:
	print(type(exceptionInstance))
	print(exceptionInstance.args)
	print("0:", exceptionInstance.args[0])
	print("1:", exceptionInstance.args[1])
	print("2:", exceptionInstance.args[2])
	print(exceptionInstance)  # Note that ~__str__~ may be overridden in exception subclasses.
	print("str(exceptionInstance):", str(exceptionInstance))
	print(exceptionInstance.__str__())
	x, y, z = exceptionInstance.args
	print("x = ", x)
	print("y = ", y)
	print("z = ", z)


def tupleReversor(myTuple: tuple) -> None:
	reversedTuple = ()
	for i in myTuple[-1::-1]:
		reversedTuple += (i,)
	reversedTuple += (5,)
	reversedTuple += (6,)

	return reversedTuple


print(tupleReversor((1, 2, 3, 4)))

for i in reversed(("d", "c", "b", "a")):
	print(i)


class AnotherTuple:

	def __init__(self, tup: tuple | None = None, dic: dict | None = None) -> None:
		self.tup = tup
		self.dic = dic

	# def __init__(self, tup):
	# 	self.tup = tup

	def printMe(self) -> None:
		print("Printing (tup):", self.tup)
		if self.dic is not None:
			print("Printing (dic):", self.dic)


AnotherTuple(tup = (1, 2, 3), dic = {"a": 1, "b": 2}).printMe()
AnotherTuple(tup = (1, 2, 3, 4)).printMe()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def this_fails() -> None:
	x = 1 / 0


try:
	this_fails()
except ZeroDivisionError as error:
	print("Handling run-time error:", error)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def raiseError(errorMessage: str) -> None:
	raise NameError(errorMessage)


try:
	errorMessage = "Hi There"
	# raise NameError(errorMessage)
	raiseError(errorMessage)
except NameError:
	print("An exception flew by!")  # raise

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

try:
	# raise KeyboardInterrupt
	pass
finally:
	print("Goodbye, World!")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def divide(x: int, y: int) -> None:
	try:
		result = x / y
	except ZeroDivisionError:
		print("Division by zero!")
	else:
		print("Result is:", result)
	finally:
		print("Executing finally clause.")


divide(2, 1)
divide(2, 0)
# divide("2", "1")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def scope_test() -> None:

	def do_local() -> None:
		spam = "local spam"

	def do_nonlocal() -> None:
		nonlocal spam
		spam = "nonlocal spam"

	def do_global() -> None:
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam)


scope_test()
# print("In global scope:", spam)

sys.exit()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class Complex:

	def __init__(self, realpart: float, imagpart: float) -> None:
		self.r = realpart
		self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class MyClass:
	"""A simple example class."""

	i = 12345

	def f(self) -> str:
		return "hello world"


x = MyClass()
x.counter = 1
while x.counter < 10:
	x.counter = x.counter * 2
print(x.counter)
del x.counter

xf = x.f
# while True:
print(xf())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class Dog:
	kind = "canine"

	def __init__(self, name: str) -> None:
		self.name = name


d = Dog("Fido")
e = Dog("Buddy")
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class Dog:
	tricks: typing.ClassVar = []

	def __init__(self, name: str) -> None:
		self.name = name

	def add_trick(self, trick: str) -> None:
		self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print("d.tricks:", d.tricks)
print("e.tricks:", e.tricks)
print("Dog.tricks:", Dog.tricks)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class Dog:

	def __init__(self, name: str) -> None:
		self.name = name
		self.tricks = []

	def add_trick(self, trick: str) -> None:
		self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print(d.tricks)
print(e.tricks)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

for element in [1, 2, 3]:
	print(element)
for element in (1, 2, 3):
	print(element)
for key in {"one": 1, "two": 2}:
	print(key)
for char in "ABC":
	print(char)
with pathlib.Path.open("../../var/in.txt") as file132:
	for line in file132.readlines():
		print(line, end = "")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

s = "abc"
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class Reverse:
	"""Iterating for looping over a sequence backwards."""

	def __init__(self, data: str) -> None:
		self.data = data
		self.index = len(data)

	def __iter__(self) -> Reverse:
		return self

	def __next__(self) -> str:
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]


rev = Reverse("spam")
print(iter(rev))
for char in rev:
	print(char)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def reverse(data: str) -> str:
	for index in range(len(data) - 1, -1, -1):
		yield data[index]


for char in reverse("golf"):
	print(char)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(sum(i * i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x * y for x, y in zip(xvec, yvec)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

sine_table = {x: math.sin(x * math.pi / 180) for x in range(91)}
print(sine_table)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

data = "golf"
print(list(data[i] for i in range(len(data) - 1, -1, -1)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

# print(os.getcwd())
print(pathlib.Path.getcwd())
os.chdir("../../var/log/")
# os.system("mkdir pythontestbed")
print("chdir:", os.chdir("/home/punit/src/_not_mine/PythonTestBed/src/_not_mine"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print("dir(os):", dir(os))  # Returns a list of all module functions.
print("help(os):", help(os))  # Returns an extensive manual page created from the module's docstrings.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(pathlib.Path.getcwd())
shutil.copyfile("../../var/in.txt", "../../var/copy_of_in.txt")
shutil.move("../../var/copy_of_in.txt", "../../var/copy_of_in_moved.txt")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

# print(glob.glob("*.py"))
print(pathlib.Path.glob("*.py"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(sys.argv)
sys.stderr.write("Warning, log file not found starting a new one\n")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat"))

print("tea for too".replace("too", "two"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(math.cos(math.pi / 4))
print(math.log(1024 / 2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(random.choice(["apple", "pear", "banana"]))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

# with urlopen("https://www.usno.navy.mil/USNO/time/display-clocks/simpletime") as response:
with urllib.request.urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
	for line in response:
		line = line.decode("utf-8")
		if "EST" in line or "EDT" in line:
			print(line)
		else:
			print("line:", line)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

now = datetime.datetime.now(tz = datetime.timezone(datetime.timedelta(hours = 5.5))).date()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = datetime.date(1964, 7, 31)
age = now - birthday
print(age.days)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

s = b"which witch has which witch's wrist watch"
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print("crc32:", zlib.crc32(s))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(timeit.Timer("t = a; a = b; b = t", "a = 1; b = 2").timeit())
print(timeit.Timer("a, b = b, a", "a = 1; b = 2").timeit())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


def average(values: list) -> float:
	"""Compute the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """

	return sum(values) / len(values)


doctest.testmod(verbose = False)  # Automatically validate the embedded tests.


class TestMyAverageFunction(unittest.TestCase):

	def test_average(self) -> None:
		# self.assertEqual(average([20, 30, 70]), 40.0)
		assert average([20, 30, 70]) == 40.0
		# self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
		assert round(average([1, 5, 7]), 1) == 4.3
		# with self.assertRaises(ZeroDivisionError):
		with self.pytest.Raises(ZeroDivisionError):
			average([])  # with self.assertRaises(TypeError):  # 	average([20, 30, 70])


# unittest.main(argv = ["0"])  # Calling from the command line invokes all tests.
unittest.main(exit = False)  # Calling from the command line invokes all tests.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(reprlib.repr(set("supercalifragilisticexpialidocious")))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

t = [[[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]]

print("len(t):", len(t))
print("len(t[0]:", len(t[0]))
print("len(t[0][0]):", len(t[0][0]))  # Count the commas, 1 comma means 2 elements.
print("len(t[0][0][0]):", len(t[0][0][0]))
print("t:", t)
print("t[0]:", t[0])
print("t[0][0]:", t[0][0])
print("t[0][0][0]:", t[0][0][0])

pprint.pprint(t, width = 30)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width = 40))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

locale.setlocale(locale.LC_ALL, "en_US.utf-8")
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping = True))
print(locale.format_string("%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x), grouping = True))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

t = string.Template("${village} folk send $$10 to $cause.")
print(t.substitute(village = "Nottingham", cause = "the ditch fund"))

t = string.Template("Return the $item to $owner.")
d = dict(item = "unladen swallow")
# print(t.substitute(d))
print(t.safe_substitute(d))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

photoFiles = ["img_1074.jpg", "img_1076.jpg", "img_1077.jpg"]


class BatchRename(string.Template):
	delimiter = "%"


fmt = input("Enter rename style (%d-date %n-seqnum %f-format): ")
t = BatchRename(fmt)
date = time.strftime("%d%b%y")
for i, filename in enumerate(photoFiles):
	# base, ext = os.path.splitext(filename)
	base, ext = pathlib.Path.splitext(filename)
	newname = t.substitute(d = date, n = i, f = ext)
	print(f"{filename} --> {newname}")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.zip", "rb") as f:
	data = f.read()

start = 0
for i in range(3):
	start += 14
	fields = struct.unpack("<IIIHH", data[start:start + 16])
	crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

	start += 16
	filename = data[start:start + filenamesize]
	start += filenamesize
	extra = data[start:start + extra_size]
	print("Header ", i + 1, ":", sep = "", end = "")
	print(filename, hex(crc32), comp_size, uncomp_size)

	start += extra_size + comp_size

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class AsyncZip(threading.Thread):  # Like Java, we need to create a class that will create a thread object.

	def __init__(self, infile: text, outfile: text) -> None:
		threading.Thread.__init__(self)  # This line should be there for every thread class in its ~init~.  Doesn't work.
		self.infile = infile  # Initialise other fields of your thread class.
		self.outfile = outfile

	def run(self) -> None:  # Define the operations to be done by the thread.
		f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)  # Operation step number one.
		f.write(self.infile)
		f.close()
		print("Finished background zip of:", self.infile)  # This thread is run in background (~background thread~).


background = AsyncZip("../../var/in.txt", "../../var/in1.zip")  # Create your thread.
background.start()  # Start the execution of your thread.
print("The main program continues to run in foreground.")  # This is main thread, running simultaneously.

background.join()  # Wait for the background task to finish.
print("Main program waited until background was done.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

logging.debug("Debugging information")
logging.info("Informational message")
logging.warning("Warning:config file %s not found", "server.conf")
logging.error("Error occurred")
logging.critical("Critical error -- shutting down")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.


class A:

	def __init__(self, value: any) -> None:
		self.value = value

	def __repr__(self) -> None:
		return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d["primary"] = a
print("d[\"primary\"]:", d["primary"])
del a
gc.collect()
# print("d[\"primary\"]:", d["primary"])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

a = array.array("H", [4000, 10, 700, 22222])  # "H" is typecode for 2-byte unsigned binary number, thus 2 bytes per entry.
print("sum:", sum(a))
print("a[1:3]:", a[1:3])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

d = collections.deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
bisect.insort(scores, (300, "ruby"))
print(scores)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(data)
heapq.heappush(data, -5)
print([heapq.heappop(data) for i in range(3)])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(round(decimal.Decimal("0.70") * decimal.Decimal("1.05"), 2))
print(round(0.70 * 1.05, 2))

print(decimal.Decimal("1.00") % decimal.Decimal(".10"))
print(1.00 % 0.10)
print(sum([decimal.Decimal("0.1")] * 10) == decimal.Decimal("1.0"))
print(sum([0.1] * 10) == 1.0)

decimal.getcontext().prec = 36
print(decimal.Decimal(1) / decimal.Decimal(7))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(format(math.pi, ".12g"))
print(format(math.pi, ".2f"))
print(repr(math.pi))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(0.1 + 0.1 + 0.1 == 0.3)

print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))

print(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

x = 3.14159
print(x.as_integer_ratio())  # Much more exact than smaller numbers for lossless recreation of original numbers.
print(x == 3537115888337719 / 1125899906842624)
print(x.hex())
print(x == float.fromhex("0x1.921f9f01b866ep+1"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(sum([0.1] * 10) == 1.0)

print(math.fsum([0.1] * 10) == 1.0)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

print(2 ** 52 <= 2 ** 56 // 10 < 2 ** 53)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL.

q, r = divmod(2 ** 56, 10)
print(r)
print(q + 1)

print(0.1 * 2 ** 55)
print(3602879701896397 * 10 ** 55 // 2 ** 55)
print(format(0.1, ".17f"))

print(fractions.Fraction.from_float(0.1))
print((0.1).as_integer_ratio())
print(decimal.Decimal.from_float(0.1))
print(format(decimal.Decimal.from_float(0.1), ".17"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL

# if os.path.isfile(".pythonrc.py"):
if pathlib.Path.is_file(".pythonrc.py"):
	with open(".pythonrc.py").read() as file_content:
		exec(file_content)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# TUTORIAL

filename = os.environ.get("PYTHONSTARTUP")
if filename and pathlib.Path.is_file(filename):
	with pathlib.Path.open(filename) as fobj:
		startup_file = fobj.read()
	exec(startup_file)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# GLOSSARY

print(site.getusersitepackages())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# GLOSSARY

print(__future__.division)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# GLOSSARY.

result = [f"{x:#04x}" for x in range(256) if x % 2 == 0]
print(result)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# GLOSSARY.


class C:

	class D:

		def meth(self) -> None:
			pass


print(C.__qualname__)
print(C.D.__qualname__)
print(C.D.meth.__qualname__)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# GLOSSARY.

print(email.mime.text.__name__)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

L = []
print([d for d in dir(L) if "__" not in d])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

x = 10


def bar() -> None:
	print(x)


bar()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

x = 10


def bar() -> None:
	print(x)


# x = 10

bar()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

x = 10


def bar() -> None:
	global x
	print(x)
	x = 20


bar()
print(x)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def foo() -> None:
	x = 10

	def bar() -> None:
		nonlocal x

		print(x)
		x += 1

	bar()
	print(x)


foo()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

squares = []
for x in range(5):
	squares.append(lambda: x ** 2)

print(squares)
print(squares[0](), squares[1](), squares[2]())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

squares = []

for x in range(5):
	squares.append(lambda n = x: n ** 2)

print(squares)
print(squares[0](), squares[1](), squares[2]())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print(config.x)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def foo(myDict: dict = {}):  # Reference is shared with subsequent invocations.
	myDict["key2"] = 1
	print("myDict: 4:", myDict)

	return myDict


myDict = {}
# myDict = {"key1": 0, "key2": 1}
myDict["key1"] = 0
print("myDict: 1:", foo(myDict))  # r.t.l. evaluation and printing.
print("myDict: 5:", myDict)
print("myDict: 1:", foo(myDict))  # r.t.l. evaluation and printing.
print("myDict: 5:", myDict)
print("myDict: 2:", foo())
print("myDict: 5:", myDict)
print("myDict: 3:", foo())
print("myDict: 5:", myDict)


def add_element(element, myList = []):
	myList.append(element)

	return myList


myList = [0, 1, 2]
print(add_element(3, myList))
print(add_element(4, myList))
print(add_element(0))
print(add_element(1))  # Default argument's value is used and persisted across all invocations that don't specify that argument's value.
print(add_element(5, myList))
print(add_element(2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = []
myList += [1, 2, 3]  # Is same as:
myList.extend([1, 2, 3])
print(myList)
myTuple = ()
myTuple += (1, 2, 3)  # Creates a new object, like:
print(myTuple)
myNumber = 1
myNumber += 1
print(myNumber)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def f(a: int, b: int) -> tuple(int, int):
	print("a:", a, "b:", b)
	a += 1
	b = b + 2
	print("a:", a, "b:", b)
	return a, b


x, y = 0, 1
print("x:", x, "y:", y)
x, y = f(x, y)
print("x:", x, "y:", y)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def f(a: list) -> None:
	a[0] = 1
	a[1] += 1


args = [0, 1]
f(args)
print(args[0], args[1])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def f(args: dict) -> None:
	args["a"] = "1"
	args["b"] += "1"


a = {"a": "0", "b": "1"}
f(a)
print(a["a"], a["b"])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class CallByReference:

	def __init__(self, **args: dict) -> None:
		for key, value in args.items():
			setattr(self, key, value)


def f(args: dict):
	args.a = "1"
	args.b += 1


args = CallByReference(a = "0", b = 1)
f(args)
print(args.a, args.b)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def Linear(a: float, b: float) -> None:

	def result(x: float) -> float:
		return a * x + b

	return result


taxes = Linear(0.3, 2)
print(taxes(10e6))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class Linear:

	def __init__(self, a: float, b: float) -> None :
		self.a, self.b = a, b

	def __call__(self, x: float) -> float:
		return self.a * x + self.b


taxes = Linear(0.3, 2)
print(taxes(10e6))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class Counter:
	value = 0

	def up(self) -> None:
		self.value = self.value + 1

	def down(self) -> None:
		self.value = self.value - 1

	def set(self, x: int) -> None:
		self.value = x


count = Counter()
increment, decrement, reset = count.up, count.down, count.set

print(increment, decrement, reset)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class A:
	pass


B = A
b = B()
a = b
print(b)
print(a)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print("a" in "b", "a")
print(("a" in "b"), "a")
print("a" in ("b", "a"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print(list(filter(None, map(lambda y: y * functools.reduce(lambda x, y: x * y != 0, map(lambda x, y = y: y % x, range(2, int(pow(y, 0.5) + 1))), 1), range(2, 1000)))))
print(list(map(lambda x, f = lambda x, f: (f(x - 1, f) + f(x - 2, f)) if x > 1 else 1: f(x, f), range(10))))
print((lambda Ru, Ro, Iu, Io, IM, Sx, Sy: functools.reduce(lambda x, y: x + y, map(lambda y, Iu = Iu, Io = Io, Ru = Ru, Ro = Ro, Sy = Sy, L = lambda yc, Iu = Iu, Io = Io, Ru = Ru, Ro = Ro, i = IM, Sx = Sx, Sy = Sy: functools.reduce(lambda x, y: x + y, map(lambda x, xc = Ru, yc = yc, Ru = Ru, Ro = Ro, i = i, Sx = Sx, F = lambda xc, yc, x, y, k, f = lambda xc, yc, x, y, k, f: (k <= 0) or (x * x + y * y >= 4.0) or 1 + f(xc, yc, x * x - y * y + xc, 2.0 * x * y + yc, k - 1, f): f(xc, yc, x, y, k, f): chr(64 + F(Ru + x * (Ro - Ru) / Sx, yc, 0, 0, i)), range(Sx))): L(Iu + y * (Io - Iu) / Sy), range(Sy))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 5))  # Mandelbrot set.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

__import__("os").system("ls $HOME")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print(f"{'144':04d}")
print("{:04x}".format(16))
# print("{:.3f}".format(1.0 / 3.0))
print(f"{1.0/3.0:.3f}")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

s = "Hello, world!"
sio = io.StringIO(s)
print(sio.getvalue())
sio.seek(7)
sio.write("there!")
print(sio.getvalue())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

s = "Hello, world!"
a = array.array("u", s)
print(a)
a[0] = "y"
print(a)
print(a.tounicode())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def a() -> None:
	print("A")


def b() -> None:
	print("B")


dispatch = {"callA": a, "callB": b}
dispatch["callB"]()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class Char:

	def __init__(self, c: str) -> None:
		self.c = c

	def do_lower(self) -> str:
		return self.c.lower()

	def do_upper(self) -> str:
		return self.c.upper()


opToDo = input("What do you want to do today ? ")
if opToDo == "lower":
	char = Char("A")
elif opToDo == "upper":
	char = Char("a")
else:
	print("Invalid Choice.")

function = getattr(char, "do_" + opToDo)
print(function())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def myFunction() -> None:
	print("Hello")


f = "myFunction"
f1 = locals()[f]
f1()

# f2 = eval(f)
f2 = ast.literal_eval(f)
f2()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myString = "test\r\n"
print(myString.rstrip("\r\n"))

lines = "line\r\n" "\r\n" "\r\n"
print(lines.rstrip("\n\r"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]
# myList = ["a", "a", "b", "c", "d", "d", "e", "e", "f"]
if myList:
	myList.sort()

	for i in range(len(myList) - 2, -1, -1):
		if myList[i] == myList[i + 1]:
			del myList[i + 1]

print(myList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]
# myList = ["a", "a", "b", "c", "d", "d", "e", "e", "f"]

if myList:
	myList.sort()
	last = myList[-1]

	for i in range(len(myList) - 2, -1, -1):
		if last == myList[i]:
			del myList[i]
		else:
			last = myList[i]

print(myList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]

myList = list(set(myList))
print(myList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

oneDimList = [1] * 2
print("oneDimList1:", oneDimList)
oneDimList1 = [None] * 2
print("oneDimList1:", oneDimList1)
multiDimList = [[None] * 2] * 3
print("multiDimList:", multiDimList)
print("multiDimList[0][0]:", multiDimList[0][0])
multiDimList[0][0] = 0
print("multiDimList:", multiDimList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

aList = [None] * 3
for i in range(3):
	aList[i] = [None] * 2
print(aList)
aList[0][0] = 1
print(aList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

w, h = 2, 3
aList = [[None] * w for i in range(h)]
print(aList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myTuple = (["1"], "2")
# myTuple[0] += ["one"]
print(myTuple)
print(myTuple[0])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = []
myList += [1]
print(myList)
myList.extend([2])
print(myList)
myList = myList.__add__([3])
print(myList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myList = ["4", "8", "3", "2", "9", "1", "6", "0"]
print(sorted(myList))
myList1 = ["c", "a", "g", "e", "b", "d"]
print(sorted(myList1))
myList2 = ["186", "185", "199", "131", "198", "121", "195", "105", "193", "183"]
myList2.sort(key = lambda s: int(s[1]))
print(myList2)
myList3 = [186, 185, 199, 131, 198, 121, 195, 105, 193, 183]
myList3.sort(key = lambda s: str(s)[1])
print(myList3)
myList4 = ["186", "185", "199", "131", "198", "121", "195", "105", "193", "183"]
myList4.sort(key = lambda s: s[1])
print(myList4)
myList5 = ["18606", "18335", "19569", "13421", "11918", "12281", "19255", "10575", "14923", "12813"]
myList5.sort(key = lambda s: s[1:3])
print(myList5)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

husbands = ["zero", "one", "two", "three", "four", "five", "six", "seven"]
wives = ["eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
children = ["sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty"]
families = zip(husbands, wives, children)
print("Families:", families)
familiesSortedByHusbands = sorted(families)
print("sortedFamilies:", familiesSortedByHusbands)
sortedHusbands = [i[0] for i in familiesSortedByHusbands]
print(sortedHusbands)
sortedWives = [i[1] for i in familiesSortedByHusbands]
print(sortedWives)
sortedChildren = [i[2] for i in familiesSortedByHusbands]
print(sortedChildren)
wivesAnotherWay = []
for wife in familiesSortedByHusbands:
	wivesAnotherWay.append(wife[1])
print("wivesAnotherWay:", wivesAnotherWay)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class MyClass:
	classVariableObjectsCount = 0

	def __init__(self) -> None:
		MyClass.classVariableObjectsCount += 1

	def printCount(self) -> None:
		print("MyClass.classVariable:", MyClass.classVariableObjectsCount)
		print("self.classVariable:", self.classVariableObjectsCount)


print("MyClass.classVariableObjectsCount:", MyClass.classVariableObjectsCount)
myObject1 = MyClass()
print("printCount:")
myObject1.printCount()
print("MyClass.classVariableObjectsCount:", MyClass.classVariableObjectsCount)
print("Creating object 2:")
myObject2 = MyClass()
print("MyClass.classVariableObjectsCount:", MyClass.classVariableObjectsCount)
print("printCount:")
myObject2.printCount()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print("0:", id(0))
print("0:", id(0))
print("0:", id(0))
print("1:", id(1))
print("0:", id(0))
print("1:", id(1))
print("2:", id(2))
print("0:", id(0))
print("1:", id(1))
a = 0
b = 1
c = 2
d = 3
print("a:", id(a))
print("b:", id(b))
print("c:", id(c))
print("d:", id(d))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

py_compile.compile("/home/punit/src/_not_mine/PythonTestBed/src/_not_mine/main.py")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print("module4.module4Var:", module4.module4Var)
# print("module5Var:", module5.module5Var)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# _MINE.

print(inspect.getfile(os))
print(inspect.getfile(os.path))
print(inspect.getfile(os.path.samestat))
print(inspect.getfile(os.path.genericpath.samestat))

print("os:")
for key, value in inspect.getmembers(os):
	print("KEY:", key)
	print("VALUE:", value, end = "\n\n")

print("os.path:")
for key, value in inspect.getmembers(os.path):
	print("KEY:", key)
	print("VALUE:", value, end = "\n\n")

print("os.path.samestat:")
for key, value in inspect.getmembers(os.path.samestat):
	print("KEY:", key)
	print("VALUE:", value, end = "\n\n")

print("os.path.genericpath.samestat:")
for key, value in inspect.getmembers(os.path.genericpath.samestat):
	print("KEY:", key)
	print("VALUE:", value, end = "\n\n")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

importlib.reload(module4)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

myClassObject = module2.MyClass(1)
print(module2.MyClass.getX(myClassObject))
myClassObject1 = module2.MyClass(2)
print(module2.MyClass.getX(myClassObject1))
print(isinstance(myClassObject, module2.MyClass))
print(hex(id(myClassObject.__class__)))
print(hex(id(module2.MyClass)))
importlib.reload(module2)
print(isinstance(myClassObject, module2.MyClass))
print(hex(id(myClassObject.__class__)))
print(hex(id(module2.MyClass)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def caseA() -> int:
	return hex(ord("A"))


def caseB() -> int:
	return hex(ord("B"))


def caseC() -> int:
	return hex(ord("C"))


switch = {"A": caseA, "B": caseB, "C": caseC}
executeSwitch = switch["A"]
print(executeSwitch())
executeSwitch = switch["B"]
print(executeSwitch())
executeSwitch = switch["C"]
print(executeSwitch())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

print(os.listdir("."))  # Returns all files in the current directory.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


class GoToLabelError(Exception):
	print("GoToLabelError.")


def raiseGoToLabel() -> None:
	raise GoToLabelError


try:
	if True:
		raiseGoToLabel()
except GoToLabelError:
	print("Except.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.


def threadTask(threadName, threadNum):
	time.sleep(1)
	print("Entering thread:", threadNum)
	# print("Entering sleep:", threadNum)
	# print("Exiting sleep:", threadNum)
	for i in range(threadNum):
		print(threadName, threadNum)
	print("Exiting thread:", threadNum)


for i in range(10):
	print("Starting thread:", i)
	myThread = threading.Thread(target = threadTask(str(i), i))
	myThread.start()
	print("Ending thread:", i)

# time.sleep(12)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

"""
	The job of the worker is to take an element from the queue and print it.
"""


def worker():
	print("Running Worker:", threading.current_thread().name)
	time.sleep(0.1)
	while True:
		try:
			arg = tasksQueue.get(block = False)
		except queue.Empty:
			print("Worker:", threading.current_thread().name, "Empty.")
			break
		else:
			print("Worker:", threading.current_thread().name, "\b: Argument:", arg)
			time.sleep(0.5)


tasksQueue = queue.Queue()

for i in range(5):
	t = threading.Thread(target = worker, name = chr(i + ord("A")))
	t.start()

print("Enqueueing...")
for tasksQueueArg in range(50):
	tasksQueue.put(tasksQueueArg)
print("Finished.")

print("Main Thread Sleeping...")
time.sleep(5)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# FAQ.

with open("/home/punit/src/_not_mine/PythonTestBed/var/randEight.txt", "w+b") as f:
	randomEight = random.randbytes(8)
	print("randomEight:", randomEight)
	f.write(randomEight)
	s1, s2, l = struct.unpack("<hhl", randomEight)
	print("s1:", s1, "s2:", s2, "l:", l)
	l1 = -2147483648
	l2 = -1
	l3 = 1
	l4 = 2147483647
	fourLongs = struct.pack("<llll", l1, l2, l3, l4)
	f.write(fourLongs)
	f.seek(-16, os.SEEK_CUR)
	readLongs = f.read(16)
	print("readLongs:", readLongs)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

circularImportExample = 10
x = 1

y = 2
print("main: x:", x)
print("main: y:", y)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(sys.get_int_max_str_digits())
sys.set_int_max_str_digits(100000)
print(sys.get_int_max_str_digits())
print(len(str(2 ** 100000)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

S = "shrubbery"
L = list(S)
L[1] = "c"
L = "".join(L)
print(L)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

B = bytearray(b"spam")
B.extend(b"eggs")
print(B)
print(B.decode())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

S = "spam"
print(S.find("pa"))
print(S.replace("pa", "XYZ"))
print(S)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

line = "aaa,bbb,ccccc,dd"
print(line.split(","))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

S = "spam"
print(S + "NI!")
print(S.__add__("NI!"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(help(S.replace))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("sp\xc4\u00c4\U000000c4m")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

match = re.match("Hello[ \t]*(.*)world", "Hello		Python world")
print(match.group(1))

match = re.match("[/:](.*)[/:](.*)[/:](.*)", "/usr/home:lumberjack")
match = re.match("(.*)[/:](.*)[/:](.*)[/:](.*)", "lumberjack:/home/user")

print(match.groups())

print(re.split("[/:]", "/usr/home/lumberjack"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

myList = [1, 2]
print(myList + [3])
print(myList * 2)
myList.append("WOMAN")
print(myList)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
secondColumn = [row[1] + 1 for row in matrix if row[1] % 2 == 0]
print(secondColumn)
diagonal = [matrix[row][row] for row in [0, 1, 2]]
print(diagonal)
doubledLetters = [character * 2 for character in "WOMAN"]
print(doubledLetters)
myList = list(range(30))
print(myList)
myList = list(range(-6, 7, 2))
print(myList)
myList = [[x ** 2, x ** 3] for x in list(range(4)) if x % 2 == 0]
print(myList)
myGenerator = ([x ** 2, x ** 3] for x in list(range(4)) if x % 2 == 0)
print(next(myGenerator))
print(next(myGenerator))
print("list map sum:" + str(list(map(sum, matrix))))
print(list(map(sum, matrix)))
print(matrix)
print({sum(row) for row in matrix})
print({row: sum(matrix[row]) for row in range(3)})
print([ord(character) for character in "DAMSELINDISTRESS"])
print({ord(character) for character in "DAMSEL"})

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

myDictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(myDictionary["key1"] + str(1))
myDictionary["key3"] = "value3"

print(myDictionary["key3"])
myDictionary1 = dict(key4 = "value4")
print(myDictionary1["key4"])
myDictionary2 = dict(zip(["name", "age", "salary"], ["Woman", 27, 1000000]))
print(myDictionary2)
print(myDictionary2.get("name2", "Punit"))
print(myDictionary2["name"] if "name2" in myDictionary2 else "Punit")
keys = list(myDictionary2.keys())
print(keys)
for key in sorted(myDictionary2):
	print(myDictionary2[key])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

D = {"a": 1, "b": 2, "c": 3}
value = D.get("x", 0)
print(value)
value = D["x"] if "x" in D else 0
print(value)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(list(map(ord, "spam")))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print([1, 2] + list("34"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(list(map(abs, [-1, -2, 0, 1, 2])))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list9 = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("list9:", list9)
list9[2:5] = list9[3:6]  # Overlapping works fine because module1 fetching is done, then deletion.
print("list9:", list9)
list9[1:1] = ["x", "y"]
print("list9:", list9)
list10 = [1]
list10[:0] = [2, 3, 4]
print("list10:", list10)
list10[len(list10):] = [5, 6, 7]
print("list10:", list10)

list11 = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("list11:", list11)
list11[len(list11):] = ["i"]  # Is same as:
print("list11:", list11)
list11.append("i")  # And:
print("list11:", list11)
list11.insert(len(list11), "i")
print("list11:", list11)

list11[:0] = ["0"]  # Prepending.  Same as:
print("list11:", list11)
list11.insert(0, "0")
print("list11:", list11)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list12 = ["abc", "ABD", "aBe"]
list12.sort(key = str.lower)
print("list12:", list12)

list12 = ["abc", "ABD", "aBe"]
list12.sort(key = str.lower, reverse = True)
print("list12:", list12)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list13 = ["spam", "eggs", "ham", "toast"]
del list13[1:]  # Delete entire section.  Same as:
print("list13:", list13)
list13 = ["spam", "eggs", "ham", "toast"]
list13[1:] = []
print("list13:", list13)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list14 = ["Already", "got", "one"]
list14[0] = []  # Does not delete.  Instead, puts a reference to an empty list at that index.
print("list14:", list14)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

dict1 = dict([("name", "Bob"), ("age", 40)])
dict2 = dict.fromkeys(["name", "age"])
print("dict1.items():", dict1.items())  # All key, value tuples.
print("\"Name\" in dict1:", "Name" in dict1)
print("dict1.update(dict2):", dict1.update(dict2))  # Merge by keys.
print("dict1.get(\"name\", \"Punit\"):", dict1.get("name", "Punit"))  # Fetch by key, if absent default (or "None").
print("dict1.pop(\"age\", \"29\"):", dict1.pop("age", "29"))  # Remove by key, same as above.
print("dict1.setdefault(\"name\", \"Punit\"):", dict1.setdefault("name", "Punit"))  # Fetch by key, if absent: set default, or "None".
print("dict1.popitem():", dict1.popitem())
print("dict1:", dict1)
print("dict2:", dict2)
dict1 = dict([("name", "Bob"), ("age", 40)])
del dict1["name"]  # Delete entries by key.
print("list(dict1.keys():", list(dict1.keys()))  # Dictionary views.
print("dict1.keys() & dict2.keys():", dict1.keys() & dict2.keys())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

table = {"Holy Grail": "1975", "Life of Brian": "1979", "The Meaning of Life": "1983"}
print(list(table.items()))
print([title for (title, year) in table.items() if year == "1975"])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

Matrix = {(2, 3, 4): 88, (7, 8, 9): 99}
x = 2
y = 3
z = 4
print("Matrix[(x, y, z)]:", Matrix[(x, y, z)])
origin = (7, 8, 9)
print("Matrix[origin]:", Matrix[origin])
print("Matrix:", Matrix)

try:
	print(Matrix[(2, 3, 6)])
except KeyError:
	print(0)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("list(zip([\"a\", \"b\", \"c\"], [1, 2, 3])):", list(zip(["a", "b", "c"], [1, 2, 3])))
dict11 = {k: v for (k, v) in zip(["a", "b", "c"], [1, 2, 3])}
print("dict11:", dict11)
k = dict11.keys()
print("k | {\"x\" : 4}:", k | {"x": 4})
v = dict11.values()
try:
	print("v | {\"x\" : 4}:", v | {"x": 4})
except TypeError:
	print("Value error.")
try:
	print("v | {\"x\" : 4}.values():", v | {"x": 4}.values())
except TypeError:
	print("Value error.")
print("k & {\"c\": 3}:", k & {"c": 3})
print("dict11.items() | dict11.keys():", dict11.items() | dict11.keys())
print("dict(dict11.items() | {(\"d\", 4), (\"e\", 5)}):", dict(dict11.items() | {("d", 4), ("e", 5)}))
print("dict({(\"a\", 1), (\"b\", 2)}):", dict({("a", 1), ("b", 2)}))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

dict12 = {"a": 1, "b": 2}
dict13 = {"a": 1, "c": 3}
print("sorted(dict12.items()) < sorted(dict13.items()):", sorted(dict12.items()) < sorted(dict13.items()))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

file39 = dbm.open("../../var/in.dbm", "c")
file39["key"] = "Any Random String"
data = file39["key"]
print("data:", data)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

import shelve

file40 = shelve.open("../../var/in.shelve", "c")
file40["key"] = {"a": 1, "b": 2, "c": 3}
data = file40["key"]
print("data:", data)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(dict.fromkeys("ab", 0))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

x = 1
y = 2
assert x > y, "x is smaller than y"

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

[a, b, c] = (1, 2, 3)
print("a:", a)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

a, b, c = range(3)
print(a, b, c)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list15 = [3, 1, 4, 1, 5, 9]
while list15:
	head, list15 = list15[0], list15[1:]
	print("head:", head)
	print("list15:", list15)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

a, *b, c = "spam"
print("a:", a, "b:", b, "c:", c)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list16 = [3, 1, 4, 1, 5, 9]

while list16:
	head, *list16 = list16
	print("head:", head)
	print("list16:", list16)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list17 = ["a", "b", "c", "d"]
a, b, c, *d = list17
print("a:", a, "b:", b, "c:", c, "d:", d)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list17 = ["a", "b", "c", "d"]
a, b, c, d, *e = list17
print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list17 = ["a", "b", "c", "d"]
a, b, *c, d, e = list17
print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list17 = []
list17 += "spam"  # Works.
print("list17:", list17)
list17.append("spam")  # Works.
print("list17:", list17)
list17.extend("spam")  # Works.
print("list17:", list17)
try:
	list17 = list17 + "spam"  # Doesn't.
except:
	print("Got TypeError.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("a", file = sys.stderr)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("A", file = open("../../var/out2.txt", "w"))
print("out2.txt:", open("../../var/out2.txt").read())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

number10 = 0x16_FF_9A
string20 = "\u1f9e"
tuple12 = number10, string20
list32 = [number10, string20]
set20 = {number10, string20}
dict14 = {number10: string20}
print(number10, string20, tuple12, list32, set20, dict14, sep = "")  # Is same as:
sys.stdout.write(str(number10) + str(string20) + str(tuple12) + str(list32) + str(set20) + str(dict14))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

sys.stdout = open("../../var/out3.txt", "a")
print("B")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

std = sys.stdout
print("A")
sys.stdout = open("../../var/out4.txt", "a")
print("B")
sys.stdout = std
print("C")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

s = """
A
B	# Comment not ignored.
C
"""
print("s:", s, "len(s):", len(s))
s = "A" "B" "C"
print("s:", s)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(1 and 1)
print("a" and 0)
print("a" and "0")
print("a" or "0")
print(("a", "1") and ("", 0))
print(("a", "1") and ("b", 1))
print(("a", "1") or ("b", 1))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

for x in (False, True):
	for y in (False, True):
		for z in (False, True):
			print("x:", x, "y:", y, "z:", z)
			a = (x and y) or z
			print("a:", a)
			a = y if x else z  # Always same as:
			print("a:", a)
			a = [z, y][bool(x)]  # This.
			print("a:", a)
			a = x or y or z or None
			print("a:", a)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list19 = ["a", 0, "b", [], "c", {}]
print(list(filter(bool, list19)))
print(any(list19), all(list19))
print(list(filter(str, list19)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

table = [("Bob", 120129, "DB Admin", "Calicut"), ("Alice", 108420, "Python Expert", "Kozhikode"), ("Carl", 109481, "AI Engineer", "Trivandrum")]
for name, iD, designation, location in table:
	print("ID:", iD)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

for (a, b), c in [([1, 2], 3), ["XY", 4]]:
	print("a:", a, "b:", b, "c:", c)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
	for item in items:
		if item == key:
			print(key, "was found")
			break
	else:
		print(key, "not found!")

# This is better because Python is doing all the work.

for key in tests:
	if key in items:
		print(key, "was found")
	else:
		print(key, "not found!")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

output = os.popen("ls")
print("readline:", output.readline())
output = os.popen("ls")
print("read(5):", output.read(5))
output = os.popen("ls")
print("readlines()[0]:", output.readlines()[0])
print("read()[:5]:", os.popen("ls").read()[:5])

print("Line iteration in for loop:")
for line in os.popen("ls"):
	print(line.rstrip())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

file19 = open("../../var/in4.txt")
print(file19 is iter(file19) and iter(file19) is file19.__iter__())
print(file19.__next__())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list20 = ["A", "B", "C", "D"]
list20.extend(open("../../var/in5.txt"))
print("list20:", list20)
list20.append(open("../../var/in5.txt"))
print("list20:", list20)
list20.append(list(open("../../var/in5.txt")))
print("list20:", list20)
print("list20[8]:", list20[8])
print("list(list20[8]):", list(list20[8]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

x = (1, 2)
y = (3, 4)
print("list(zip(x, y)):", list(zip(x, y)))
a, b = zip(*zip(x, y))
print("a:", a, "b:", b)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

map1 = map(abs, [-1, 0, 1])
print("map1:", map1)
iterator1 = iter(map1)
print("type(map1):", type(map1))
print("type(iterator1):", type(iterator1))

print("next(map1):", next(map1))
print("next(iterator1):", next(iterator1))

for i in map1:
	print("i:", i)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(len(dir(sys)))
print(len([d for d in dir(sys) if not d.startswith("_")]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.Employee.__doc__)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

help("sys")  # If not imported.
help("email.message")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("help(docstrings.square):")
help(docstrings.square)
print("help(docstrings.Employee):")
help(docstrings.Employee)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

x = "old"


def changer():
	global x
	x = "new"


def outer():
	x = "old"

	def changer():
		nonlocal x
		x = "new"


print("x:", x)
changer()
print("x:", x)


def squares(x):
	for i in range(x):
		yield i ** 2


print(list(squares(5)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

tuple1 = 1, 2
tuple2 = 2, 3, 4
print(tuple1 + tuple2)
print(tuple1 * 3)
tuple3 = "spam"
# print([c ** 2 for c in tuple3])	# Can't apply the exponentiation operator on a string.
tuple4 = "item1", 2, 3.0, ["four1", "four2"], "item1"
print("tuple4[1]:", tuple4[1])
print("tuple4.index(2):", tuple4.index(2))
print("tuple4.index(3, 1):", tuple4.index(3, 1))
print("tuple4.count(\"item1\"):", tuple4.count("item1"))
print("tuple4[3]:", tuple4[3])
myNamedTuple = collections.namedtuple("Employee", ["name", "designation"])
print(myNamedTuple)
print(myNamedTuple["Employee"])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

tuple1 = (1, [2, 3], 4)
# tuple1[1] = [2]
tuple1[1][0] = 20
print(tuple1)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

RecordClass = collections.namedtuple("RecordClass", ["name", "age", "jobs"])  # Create the class.
bob = RecordClass("Bob", age = 30, jobs = ["dev", "mgr"])
print(bob)
print(bob[0], bob[2])
print(bob.name, bob.jobs)
RecordDict = bob._asdict()
print(RecordDict)
print(RecordDict["name"])
print(RecordDict["age"])
name1, age1, jobs1 = bob
print("jobs1:", jobs1)

for i in bob:  # Iteration context.
	print(i)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

binaryData = open("../../var/in.bin", "rb").read()
print(binaryData)
print("binaryData[4:7]:", binaryData[4:7].decode())
print("str(binaryData):", str(binaryData, "utf-8"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

packed = struct.pack(">i9sh", 7, b"MANNA DEY", 8)  # Create packed binary data.
print(packed)
myFile = open("/home/punit/src/_not_mine/PythonTestBed/var/bytestring.bin", "wb")  # Open binary output file.
myFile.write(packed)
myFile.close()

readString = open("/home/punit/src/_not_mine/PythonTestBed/var/bytestring.bin", "rb").read()
print(readString)
print(readString[4:8])
print(len(readString))
print(list(readString))
print("Read:" + readString.decode())
print(struct.unpack(">i10sh", readString))  # Unpack in to objects again.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

S = "sp\xc4m"
print(S)

with open("../../var/unicode_data.txt", "w", encoding = "utf-8") as file60:
	file60.write(S)

text = open("../../var/unicode_data.txt", encoding = "utf-8").read()
print(text)
print(len(text))

raw = open("../../var/unicode_data.txt", "rb").read()
print(raw)
print(len(raw))

print(text.encode("utf-8"))
print(raw.decode("utf-8"))
print(text.encode("utf-16"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

X = set("spam")
Y = {"h", "a", "m"}
print(X, Y)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

mySet = set(str("woman"))
mySet1 = set("man")
print(mySet)
print(mySet & mySet1)
print(mySet - mySet1)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

{n ** 2 for n in [1, 2, 3, 4]}  # Set comprehension.
print(list(set("woman")))

print(set("spam") == set("asmp"))  # Order-neutral equality test.
print("p" in set("spam"), "p" in "spam", "ham" in ["eggs", "spam", "ham"])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

d = decimal.Decimal("3.141")
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

myFraction = fractions.Fraction(1, 4)
print(myFraction + 1)
print(myFraction + fractions.Fraction(1, 2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(bool("spam"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

variable = None
print(variable)
L = [None] * 100
print(L)
print(type(L))
print(type(type(L)))
if type(L) == type([]):  # Type testing.
	print("yes")
print(type("a"))
print(type(type("a")))
myList = []
if type(myList) == list:
	print("type function output matches type name (as keyword)")
if isinstance(myList, list):  # OO test.
	print("isInstance working")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


class Lovers:

	def __init__(self, name, salary):  # Initialize when created.
		self.name = name
		self.salary = salary

	def giveHike(self, percent):
		self.salary += self.salary * percent / 100

	def getLastName(self):
		return self.name.split()[-1]


woman = Lovers("Woman", 1000)
man = Lovers("Man", 1000)
print(man.getLastName())
print(woman.giveHike(20))
print(woman.salary)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(int(3.1415))
print(float(3))  # Converts to float.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(repr("spam"))
print(str("spam"))
print(str(b"xy", "utf8"))  # Alternative to ~bytes.decode~ method.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

X = 2
Y = 4
Z = 6

print(X < Y < Z)  # Range test.
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y and Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print(1 == 2 < 3)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(1j * 1j)
print(2 + 1j * 3)
print((2 + 1j) * 3)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(oct(64), hex(64), bin(64))
print(64, 0o100, 0x40, 0b1000000)
print(int("64"), int("100", 8), int("40", 16), int("1000000", 2))
print(int("0x40", 16), int("0b10000000", 2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("{0:0}, {1:x}, {2:b}".format(64, 64, 64))  # Returns digits not strings.
print("%o, %x, %x, %X" % (64, 64, 255, 255))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
print(abs(-42.0), sum((1, 2, 3, 4)))  # Summation.
print(min(3, 1, 2, 4), max(3, 1, 2, 4))
print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(round(2.567), round(2.467), round(2.567, 2))
print("%.1f" % 2.567, "{0:.2f}".format(2.567))
print((1 / 3.0), round(1 / 3.0, 2), ("%.2f" % (1 / 3.0)))
print(math.sqrt(144))
print(144 ** 0.5)
print(pow(144, 0.5))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(hex(15))
print(bin(15))
print(int("0b1111", 2))
myComplex = complex(2, 3)
print(myComplex)
myFloat = 25.0
print(myFloat.as_integer_ratio())
if myFloat.is_integer():
	print("yes integer")
myInteger = 5
print(myInteger.bit_length())
print("OK" if False else True)
print("OK" if False else "NOK")
print("not in" if "s" not in "spam" else "in")
myList2 = myList = [1]
print("yes" if myList is not myList2 else "not")
print("abcdefghi"[1:-1:2])
myString = "abcdefghi"
myString2 = myString[slice(1, 2, -1)]
print(myString2)
myDictionary = {"key3": "value1", "key2": "value2", "key1": "value3"}
print(sorted(myDictionary.items()))
print(int(3.14), int(3.54), int(3.84))
print(float(3))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

myCode = "print(oct(8))"
eval(myCode)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("{0:o}, {1:x}, {2:b}".format(16, 16, 16))
print("%o, %x, %X" % (15, 15, 15))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(random.randint(1, 10))
print(random.randint(1, 10))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

suits = ["hearts", "clubs", "diamonds", "spades"]
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(suits)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(0.1 + 0.1 + 0.1 - 0.3)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(decimal.Decimal.from_float(1.25))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(decimal.Decimal("0.1") + decimal.Decimal("0.1") + decimal.Decimal("0.1") - decimal.Decimal("0.3"))
print(decimal.Decimal("0.1") + decimal.Decimal("0.10") + decimal.Decimal("0.10") - decimal.Decimal("0.30"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(decimal.Decimal(1) / decimal.Decimal(7))  # Default: 28 digits.
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

with decimal.localcontext() as ctx:
	ctx.prec = 2
	print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))
print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

x = fractions.Fraction(1, 3)
y = fractions.Fraction(4, 6)

print(x + y)
print(x - y)
print(x * y)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(fractions.Fraction(".25"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(fractions.Fraction("0.25"))
myDecimal = 0.25
print(fractions.Fraction(*myDecimal.as_integer_ratio()))
print(fractions.Fraction(*(0.25).as_integer_ratio()))
myFraction = fractions.Fraction(4 / 3)
print(myFraction.limit_denominator(3))

print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))

print((2.5).as_integer_ratio())

f = 2.5
z = fractions.Fraction(*f.as_integer_ratio())  # "*" converts a tuple in to individual arguments.
print(z)
print(float(z))
print(fractions.Fraction.from_float(1.75))
print(fractions.Fraction(*(1.75).as_integer_ratio()))
print(x + 2)  # "fractions.Fraction" + "int" -> "fractions.Fraction"
print(x + 2.0)  # "fractions.Fraction" + "float" -> "float"
print(x + fractions.Fraction(4, 3))  # "fractions.Fraction" + "fractions.Fraction" -> "fractions.Fraction"
a = x + fractions.Fraction(*(4.0 / 3).as_integer_ratio())
print(a)
print(a.limit_denominator(10))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

x = set("abcde")
y = set("bdxyz")
z = x.intersection(y)  # Same as "x & y".
print(z)
print(z.add("SPAM"))
print(z.update(set(["X", "Y"])))  # Merge, i.e., in-place union.
print(z.remove("b"))

for item in set("abc"):
	print(item * 3)

S = {1, 2, 3}
print(S | {3, 4})
print(S | [3, 4])

print(S.union([3, 4]))
print(S.issubset(range(-5, 5)))

S1 = {1, 2, 3, 4}
print(S1 - {1, 2, 3, 4})
print(type({}))
S = set()  # Initialize an empty set.
print(S.add(1.23))
print({1, 2, 3}.union([3, 4]))

print(set(dir(bytes)) - set(dir(bytearray)))
print(set(dir(bytearray)) - set(dir(bytes)))

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)  # Order matters in sequence.
print(set(L1) == set(L2))  # It doesn't in sets.
print(sorted(L1) == sorted(L2))

engineers = {"bob", "sue", "ann", "vic"}
managers = {"tom", "sue"}

print(engineers > managers)
print((managers | engineers) - (managers ^ engineers))  # Intersection.

print(type(True))
print(isinstance(True, int))
print(True == 1)
print(True is 1)
print(True + 4)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

mySet = {1, 2, 3, 3}
print(mySet)

copyOfMySet = mySet.copy()
print(copyOfMySet)

copyOfCopyOfMySet = set(copyOfMySet)
print(copyOfCopyOfMySet)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

mySet = [1, 2, (1, 2, [1, 2, (1, 2, [1, 2])])]

print(mySet)
copyOfMySet = copy.copy(mySet)

print(copyOfMySet)
copyOfCopyOfMySet = copy.deepcopy(mySet)

print(copyOfCopyOfMySet)
copyOfCopyOfCopyOfMySet = mySet.copy()

print(copyOfCopyOfCopyOfMySet)
print(len(mySet))

copyOfMySet = copy.copy(mySet)
print(len(copyOfMySet))

copyOfCopyOfMySet = copy.deepcopy(mySet)
print(len(copyOfCopyOfMySet))

copyOfCopyOfCopyOfMySet = mySet.copy()
print(len(copyOfCopyOfCopyOfMySet))

print(type(mySet[2]))
print(type(mySet[2][2]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("knight\'s", 'knight"s')

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

path = r"C:\new\text.dat"
print(path)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(hex(255))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

D = {"spam": 2, "ham": 1, "eggs": 3}
print(list(D.values()))
print(list(D.items()))
print(D.get("spam"))
print(D.get("toast"))
print(D.get("toast", 88))

# LP.

allTheFile = open("../../var/in.txt", encoding = "utf-8")
print(len(allTheFile.read()))

for line in open("../../var/in.txt"):
	print(line.rstrip())

	words = line.split()
	print(words)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

f = open("../../var/in3.txt")
line = f.readline()
print("line:", line)
listOfLines = line.split("$")
print("listOfLines:", listOfLines)
object1 = eval(listOfLines[0])
print("object1:", object1)
object2 = eval(listOfLines[1])
print("object2:", object2)
objectsRead = [eval(line) for line in listOfLines]
print("objectsRead:", objectsRead)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

myDict = {"a": 1, "0x29cc": "⧌", "0x29c9": "⧉", "0x29c6": "⧆", "0x29c1": "⧁"}
myPickleFile = open("../../var/out.pkl", "wb")
pickle.dump(myDict, myPickleFile)
myPickleFile.close()

myPickleFile = open("../../var/out.pkl", "rb")
unpickledObjects = pickle.load(myPickleFile)
print("unpickledObjects:", unpickledObjects)
myPickleFile.close()

print("Pickled Objects:", open("../../var/out.pkl", "rb").read())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

cSVFile = csv.reader(open("../../var/in.csv"))
for row in cSVFile:
	print(row)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

binFile = open("../../var/out.bin", "wb")
binData = struct.pack(">i4sh", -2147483647, b"pyth", -32768)
print("binData:", binData)
print("binFile.write:", binFile.write(binData))
binFile.close()

binFile = open("../../var/out.bin", "rb")
binData = binFile.read()
print("binData:", binData)
unpackedData = struct.unpack(">i4sh", binData)
print("unpackedData:", unpackedData)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list1 = [0, 1]
list2OfList1 = [-1, list1, 2]
dict1OfList2OfList1 = {"a": 1, "reference": list2OfList1, "b": 2}
print("list1:", list1)
print("list2OfList1:", list2OfList1)
print("dict1OfList2OfList1:", dict1OfList2OfList1)
list1.append(0.5)
print("list1:", list1)
print("list2OfList1:", list2OfList1)
print("dict1OfList2OfList1:", dict1OfList2OfList1)

tuple1 = 0, 1
list1OfTuple1 = [0, tuple1, 1]
dict1OfList1OfTuple1 = {"a": 1, "reference": list1OfTuple1, "b": 2}
print("tuple1:", tuple1)
print("list1OfTuple1:", list1OfTuple1)
print("dict1OfList1OfTuple1:", dict1OfList1OfTuple1)
tuple1 = 0, 0.5, 1
print("tuple1:", tuple1)
print("list1OfTuple1:", list1OfTuple1)
print("dict1OfList1OfTuple1:", dict1OfList1OfTuple1)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(bool(0.0))
print(bool({}))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(type([1]) == type([]))
print(list == type([]))
print(isinstance([1], list))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(type(lambda arg1: arg1 * 2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list1 = [0, 1, 2]
list2 = list1 * 4
print("list2:", list2)
list3 = [list1] * 4
print("list3:", list3)
list1[1] = 0.5
print("list2:", list2)
print("list3:", list3)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list4 = [0, 1, 2]
list5 = [list4] * 4
list6 = [list(list4)] * 4
print("list4:", list4)
print("list5:", list5)
print("list6:", list6)
list4[1] = 0.5
print("list4:", list4)
print("list5:", list5)
print("list6:", list6)
list6[2][1] = 0.25
print("list6:", list6)
list7 = [list(list4) for i in range(4)]
print("list7:", list7)
list4[1] = 0.0625
list7[2][1] = 0.125
print("list7:", list7)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

cyclicalList = ["grail"]
cyclicalList.append(cyclicalList)
print(cyclicalList)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

l = [0, 0xA, 0b10, "d"]
print("l:", l)
print("l[3:1]:", l[3:1])
l[3:1] = "?"
print("l:", l)
print("l[10:-10]:", l[10:-10])
l[10:] = "V"
print("l:", l)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

dict1 = {}
dict1[1] = "a"
print("dict1:", dict1)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

s = "spam"
print("s[0][0][0][0][0]:", s[0][0][0][0][0])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

s = ["s", "p", "a", "m"]
print("s[0][0][0][0][0]:", s[0][0][0][0][0])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

s = "spam"
print("s:", s)
s = s[0:1] + "l" + s[2:4]
print("s:", s)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print(zip is builtins.zip)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

# print(builtins is __builtin__)
print(builtins is __builtins__)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

try:
	print("x:", x)
except NameError:
	print("NameError raised.")
	pass


def f():
	global x
	x = 10


f()
print("x:", x)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("main: module1.x:", module1.x)
module1.x = 1
print("main: module1.x:", module1.x)

import second

print("main: module1.x:", module1.x)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

var = 0


def local():
	var = 1
	print("local: var:", var)


def global1():
	global var
	print("global1: var:", var)
	var = 2
	print("global1: var:", var)


def global2():
	var = 3

	import __main__

	print("global2: __main__.var:", __main__.var)
	__main__.var = 4
	print("global2: __main__.var:", __main__.var)


def global3():
	var = 5

	import sys

	globals = sys.modules["__main__"]
	print("global3: globals.var:", globals.var)
	globals.var = 6
	print("global3: globals.var:", globals.var)


def test():
	print("test: var:", var)
	local()
	global1()
	global2()
	global3()
	print("test: var:", var)


test()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

var = 0


def f1():
	var = 1
	print("f1: var:", var)

	def f2():
		print("f2: var:", var)

	print("f1: var:", var)

	f2()
	print("f1: var:", var)


print("main: var:", var)
f1()
print("main: var:", var)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def f1():
	var = 0

	def f2():
		print("var:", var)

	return f2


action = f1()
action()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def returnClosure(b):

	def closure(e):
		return b ** e

	b = 3  # Return me powers of 3 instead.

	return closure


myClosure = returnClosure(2)  # Return me powers of 2.
print("myClosure:", myClosure)
# myClosure: <function returnClosure.<locals>.closure at 0x7fb8391e8430>

threePoweredThree = myClosure(3)  # A different power of 3 (cubed).
print("threePoweredThree:", threePoweredThree)
# threePoweredThree: 9

threePoweredFour = myClosure(4)  # Another power of 3.
print("threePoweredFour:", threePoweredFour)
# threePoweredFour: 81

threePoweredFive = myClosure(5)  # A different name and a different object.
print("threePoweredFive:", threePoweredFive)
# 243

print("returnClosure(2) is returnClosure(3):", returnClosure(2) is returnClosure(3))
print("returnClosure(2) is returnClosure(2):", returnClosure(2) is returnClosure(2))
myClosure1 = returnClosure(3)
myClosure2 = returnClosure(4)
print("myClosure1 is myClosure2:", myClosure1 is myClosure2)
print("myClosure1(2) is myClosure2(2):", myClosure1(2) is myClosure2(2))
print("myClosure1(3) is myClosure2(3):", myClosure1(3) is myClosure2(3))
print("myClosure1(4) is myClosure2(4):", myClosure1(4) is myClosure2(4))
print("myClosure1(5) is myClosure2(5):", myClosure1(5) is myClosure2(5))
print("myClosure1(4) is myClosure2(5):", myClosure1(4) is myClosure2(5))
print("myClosure1(6) is myClosure2(6):", myClosure1(6) is myClosure2(6))
print("myClosure1(7) is myClosure2(7):", myClosure1(7) is myClosure2(7))
print("myClosure1(8) is myClosure2(8):", myClosure1(8) is myClosure2(8))
print("myClosure1(9) is myClosure2(9):", myClosure1(9) is myClosure2(9))
print("myClosure1(6):", myClosure1(6))
print("myClosure2(6):", myClosure2(6))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def returnLambda(b):
	return lambda e: b ** e


myLambda = returnLambda(3)
print("myLambda:", myLambda)

threePoweredThree = myLambda(3)
print("threePoweredThree:", threePoweredThree)

threePoweredFour = myLambda(4)
print("threePoweredFour:", threePoweredFour)

threePoweredFive = myLambda(5)
print("threePoweredFive:", threePoweredFive)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def f1():
	x = 0
	y = 10

	def f2(x = x):
		x += 1
		nonlocal y
		y += 1
		print("f2: x:", x)
		print("f2: y:", y)

	f2()
	f2()


f1()
f1()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def f1():
	x = 0

	f2(x)
	f2(x)


def f2(x):
	x += 1
	print("f2: x:", x)


f1()
f1()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def f1():
	b = 2

	f2 = lambda e: b ** e

	return f2


myLambda = f1()
print("myLambda(3):", myLambda(3))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("h")
# nonlocal a

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def tester(start):
	state = start

	def nested(label):
		print(label, start)

	return nested


f = tester(0)
print(f("spam"))
print(f("ham"))
g = tester(1)
print(g("spam"))
print(f is g)
print(tester(0) is tester(0))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def tester(start):
	state = start

	def nested(label):
		nonlocal state

		print(label, state)
		state += 1

	return nested


f = tester(0)
print(f("spam"))
print(f("ham"))
print(f("eggs"))
g = tester(42)
print(g("spam"))
print(g("eggs"))
print(f("bacon"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def demoFunctionAttribute(myArgument1):

	def nestedFunction(myArgument2):
		print(myArgument2, nestedFunction.myAttribute)
		nestedFunction.myAttribute += 1

	nestedFunction.myAttribute = myArgument1  # This statement attaches the attribute to the nested function.

	return nestedFunction  # Return the function object.


myFunctionObject = demoFunctionAttribute(0)  # Assign the function object to ~f~.  This function object has the ~start~ state stored.
print(myFunctionObject("spam"))
print(myFunctionObject("ham"))
print(myFunctionObject.myAttribute)  # Access the function attribute.

g = tester(42)  # Create another copy of the nested function.
print(g.state)
print(g.state)
g("Incrementing the state:")
print(g.state)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def customizeOpen(customizationId):
	print("builtins.open:", builtins.open)
	originalOpen = builtins.open

	def customOpen(*keywordArguments, **positionalArguments):
		print("Customizing ~open~ %r:" % customizationId, keywordArguments, positionalArguments)
		print("customOpen: originalOpen:", originalOpen, " customizationId:", customizationId)
		return originalOpen(*keywordArguments, **positionalArguments)

	builtins.open = customOpen


f = open("../../var/in6.txt")
print("f:", f.read())
customizeOpen("hell2")
f = open("../../var/in7.txt")
print("f:", f.read())
customizeOpen("hell1")
f = open("../../var/in8.txt")
print("f:", f.read())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


class customizeOpen:

	def __init__(self, customizationId):
		self.id = customizationId
		self.originalOpen = builtins.open
		builtins.open = self

	def __call__(self, *keywordArguments, **positionalArguments):
		print("Customizing ~open~ using classes.  ID: %r:" % self.id, keywordArguments, positionalArguments)
		print("customOpen: originalOpen:", self.originalOpen, " customizationId:", self.id)
		return self.originalOpen(*keywordArguments, **positionalArguments)


f = open("../../var/in6.txt")
print("f:", f.read())
customizeOpen("hell2")
f = open("../../var/in7.txt")
print("f:", f.read())
customizeOpen("hell1")
f = open("../../var/in8.txt")
print("f:", f.read())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def changer(a, b):
	a = 2
	b[0] = "spam"


x = 1
l = [1, 2]
print("x:", x, "l:", l)
changer(x, l)
print("x:", x, "l:", l)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def multiple(x, y):
	x = 2
	y = [3, 4]

	return x, y


x = 1
l = [1, 2]
print("x:", x, "l:", l)
x, l = multiple(x, l)
print("x:", x, "l:", l)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def function9(argument1, argument2):
	print("function9: argument1:", argument1, "argument2:", argument2)


def function10(argument1, argument2):
	print("function10: argument1:", argument1, "argument2:", argument2)


if sys.argv[4] == "function9":
	function, arguments = function9, (1, 2)
elif sys.argv[4] == "function10":
	function, arguments = function10, (3, 4)
else:
	function, arguments = (None,) * 2
print("function:", function, "arguments:", arguments)
if function is not None:
	function(*arguments)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def keywordOnlyDemo(a, *b, c):
	print("a:", a, "b:", b, "c:", c)


keywordOnlyDemo(0, 1, 2, 3, c = "value")
keywordOnlyDemo(0, c = "value")
keywordOnlyDemo(0, 1, c = 2)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def keywordOnlyDemo(a, *, b, c):
	print("a:", a, "b:", b, "c:", c)


keywordOnlyDemo(0, b = 3, c = "value")
with contextlib.suppress(TypeError):
	keywordOnlyDemo(0, c = "value")
	keywordOnlyDemo(0)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def keywordOnlyArgumentsDemo(a: any, *, b: int = 0, c: int = 1, d: int = 2) -> None:
	print("a:", a, "b:", b, "c:", c, "d:", d)


keywordOnlyArgumentsDemo(3, b = 4)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def argumentsOrderDemo(a: any, *b: typing.Iterable, c: int = 0, **d: typing.Iterable) -> None:
	print("a:", a, "b:", b, "c:", c, "d:", d)


argumentsOrderDemo(0, 1, 2, c = 3, x = 4, y = 5)
argumentsOrderDemo(0, 1, 2, x = 4, y = 5, c = 3)
argumentsOrderDemo(0, 1, 2, x = 4, c = 3, y = 5)


def argumentsOrderDemo(a: any, b: int = 0, *c: typing.Iterable, **d: typing.Iterable) -> None:
	print("a:", a, "b:", b, "c:", c, "d:", d)


argumentsOrderDemo(0, 1, 2, c = 3, x = 4, y = 5)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def argumentsOrderDemo(a: int, *b: typing.Iterable, c: int = 0, **d: typing.Iterable) -> None:
	print("a:", a, "b:", b, "c:", c, "d:", d)


argumentsOrderDemo(0, *(2, 3), c = 1, x = 4, y = 5)
try:
	argumentsOrderDemo(0, 2, 3, c = 1, x = 4, y = 5)
except SyntaxError:
	print("SyntaxError raised.")

argumentsOrderDemo(0, *{1, 2, 2}, **dict(c = 3, x = 4, y = 5))
try:
	argumentsOrderDemo(0, *{1, 2, 2}, **dict(x = 4, y = 5), c = 3)
except SyntaxError:
	print("SyntaxError raised.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def findMinimum1(*items: any) -> any:
	firstItem = items[0]
	for item in items[1:]:
		firstItem = min(item, firstItem)
	return firstItem


print("findMinimum1: Smallest item:", findMinimum1("b", "c", "a", "d"))


def findMinimum2(module1, *rest):
	for item in rest:
		module1 = min(item, module1)
	return module1


print("findMinimum2: Smallest item:", findMinimum2(["b", "c"], ["a", "d"], ["a", "b"], ["a", "a", "b"], ["a", "a"], ["a", "a", "a"]))


def findMinimum3(*items: any):
	return sorted(items)[0]


print("findMinimum3: Smallest item:", findMinimum3(("b", "c"), ("a", "d"), ("a", "b"), ("a", "a", "b"), ("a", "a"), ("a", "a", "a")))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def findMinOrMax(minOrMax: any, firstItem: any, *RestItems: typing.Iterable) -> any:
	for item in RestItems:
		if minOrMax(item, firstItem):
			firstItem = item
	return firstItem


def findMinimum(item: any, firstItem: any) -> None:
	return item <= firstItem


def findMaximum(item: any, firstItem: any) -> None:
	return item >= firstItem


print("findMinOrMax(findMinimum, \"b\", \"a\", \"d\", \"c\"):", findMinOrMax(findMinimum, "b", "a", "d", "c"))
print("findMinOrMax(findMaximum, \"b\", \"a\", \"d\", \"c\"):", findMinOrMax(findMaximum, "b", "a", "d", "c"))

print("findMinOrMax(eval(findMinimum.__name__), \"b\", \"a\", \"d\", \"c\"):", findMinOrMax(eval(findMinimum.__name__), "b", "a", "d", "c"))
print("findMinOrMax(eval(findMaximum.__name__), \"b\", \"a\", \"d\", \"c\"):", findMinOrMax(eval(findMaximum.__name__), "b", "a", "d", "c"))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def myPrint(*positionalArguments: typing.Iterable, **keywordArguments: typing.Iterable) -> None:
	sep = keywordArguments.pop("sep", " ")
	end = keywordArguments.pop("end", "\n")
	file = keywordArguments.pop("file", sys.stdout)
	if keywordArguments:
		try:
			errorMessage = f"extra keywords: {keywordArguments}"
			raise TypeError(errorMessage)
		except TypeError as e:
			print(sys.exc_info()[0].__name__ + ":", e, "\n")
	output = ""
	for i, argument in enumerate(positionalArguments):
		output += str(argument) + (sep if i != len(positionalArguments) - 1 else end)
	file.write(output)


print("myPrint(): Start.")
myPrint()
print("myPrint(): End.")
print()
myPrint(0, "a", (1, "b"))
print()
myPrint(0, "a", (1, "b"), sep2 = "invalid")
print()
myPrint(0, "a", (1, "b"), sep = "  ")
print()
myPrint(0, "a", (1, "b"), end = "$")
print()
myPrint(0, "a", (1, "b"), sep = "|", end = "$")
print()
myPrint(0, "a", (1, "b"), sep = "|", end = "$", file = sys.stderr)
print()
with pathlib.Path.open("../../var/out5.txt", "w") as file49:
	myPrint(0, "a", (1, "b"), sep = "|", end = "$", file = file49)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def summateRecursively(list40: list) -> int:
	if not list40:
		return 0
	return list40[0] + summateRecursively(list40[1:])


print(summateRecursively([0, 1, 2, 3, 4, 5]))
print(summateRecursively([0]))
print(summateRecursively([]))
print(summateRecursively(None))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def summateRecursively(list41: list) -> int:
	return 0 if not list41 else list41[0] + summateRecursively(list41[1:])


print(summateRecursively([0, 1, 2, 3, 4, 5]))
print(summateRecursively([0]))
print(summateRecursively([]))
print(summateRecursively(None))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def summateRecursively(list42: list) -> int:
	return list42[0] if len(list42) == 1 else list42[0] + summateRecursively(list42[1:])


print(summateRecursively([0, 1, 2, 3, 4, 5]))
print(summateRecursively([0]))
print(summateRecursively(["s", "p", "a", "m"]))
print(summateRecursively(["spam"]))
print(summateRecursively(["s"]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def summateRecursively(list43: list) -> int:
	module1, *rest = list43
	return module1 if not rest else module1 + summateRecursively(rest)


print(summateRecursively([0, 1, 2, 3, 4, 5]))
print(summateRecursively([0]))
print(summateRecursively(["s", "p", "a", "m"]))
print(summateRecursively(["spam"]))
print(summateRecursively(["s"]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def indirectlySummateRecursively(list44: list) -> bool:
	if not list44:
		return 0
	return nonEmpty(list44)


def nonEmpty(list44: list) -> int:
	return list44[0] + indirectlySummateRecursively(list44[1:])


print(indirectlySummateRecursively([0, 1, 2, 3, 4]))

# LP.

list45 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sum9 = 0
while list45:
	sum9 += list45[0]
	list45 = list45[1:]
print("sum9:", sum9)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list46 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]


def sumTree(list46: list) -> int:
	sum10 = 0
	for e in list46:
		if not isinstance(e, list):
			sum10 += e
		else:
			sum10 += sumTree(e)
	return sum


print("sumTree(list46):", sumTree(list46))
list46 = [1, [2, [3, [4, [5]]]]]  # Pathological case (right-heavy).
print("sumTree(list46):", sumTree(list46))
list46 = [[[[[1], 2], 3], 4], 5]  # Pathological case (left-heavy).
print("sumTree(list46):", sumTree(list46))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list46 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
list46Sum = 0
list46Copy = list(list46)
while list46Copy:
	print("list46:", list46Copy)
	item = list46Copy.pop(0)
	if type(item) is not list:
		list46Sum += item
	else:
		list46Copy.extend(item)
print("list46:", list46)
print("list46Sum:", list46Sum)

list46 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
list46Sum = 0
while list46:
	print("list46:", list46)
	item = list46.pop(0)
	if type(item) is not list:
		list46Sum += item
	else:
		list46.extend(item)
print("list46:", list46)
print("list46Sum:", list46Sum)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

list47 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
total = 0
while list47:
	print("list47:", list47)
	print("total:", total)
	element = list47.pop(0)
	if type(element) is not list:
		total += element
	else:
		list47[:0] = element
print("total:", total)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.

print("sys.getrecursionlimit():", sys.getrecursionlimit())
sys.setrecursionlimit(1048576)
print("sys.getrecursionlimit():", sys.getrecursionlimit())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def function30(number9: int) -> None:
	string40 = "spam"
	print("string40:", string40)
	return string40 * number9


print("function30.__code__:", function30.__code__)
print("dir(function30.__code__):", dir(function30.__code__))
print("function30.__code__.co_varnames:", function30.__code__.co_varnames)
print("function30.__code__.co_argcount:", function30.__code__.co_argcount)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def decorator1(function100: callable) -> callable:
	print("decorator1:")
	return function100


@decorator1
def function100() -> None:
	print("function100:")


print("function100():", function100())


def decorator2(function100: callable):
	print("decorator2:")
	return function100


@decorator2
def function101() -> None:
	print("function101:")


print("function101():", function101())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


def decorator1(function102: callable):
	print("decorator: function102:", function102)

	def wrapper19(*args: typing.Iterable) -> None:
		print("wrapper19: args:", args)
		function102(*args)

	return wrapper19


@decorator1
def function103(arg1: any, arg2: any):
	print("function103: arg1:", arg1, "arg2:", arg2)
	args = arg1, arg2
	print("function103: args:", args)


function103(100, 101)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP.


class Decorator1:

	def __init__(self, function104: callable):  # On ~@~ decoration.
		print("__init__: function104:", function104)
		self.function104 = function104

	def __call__(self, *args: typing.Iterable):  # On wrapped function call.
		print("self.function104:", self.function104)
		print("self.function104(1000, 1001):", self.function104(1000, 1001))
		print("self.function104(*args):", self.function104(*args))


@Decorator1
def function105(arg1: any, arg2: any) -> None:
	print("function105: arg1:", arg1, "arg2:", arg2)  # Passed to ~__init__~.


function105(100, 101)  # Passed to ~__call__~.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(math.log2(1024))

print(2 ** 31)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

try:
	with pathlib.Path.open("../../var/in.txt") as f:
		for line in f:
			print(line.strip())
			print(int(line.strip()))
except OSError as e:
	print(f"I/O Error ({e.errno}): {e.strerror})")
	print(sys.exc_info()[0])
except ValueError:
	print("Could not convert data to an integer.")
except:
	print("Unexpected error:", sys.exc_info()[0])

	print(sys.exc_info())
	print(type(sys.exc_info()))

	raise

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN


def counter(myId: int, count: int) -> None:
	for i in range(count):
		print("Thread ID: %s.  i: %s." % (myId, i))
		time.sleep(2)


print("Main thread running.")

for i in range(5):
	myThread.start_new_thread(counter, (i, 5))

time.sleep(12)

print("Main thread exiting.")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN [OLD VERSION OF TUTORIAL PROBABLY]


def asyncZip(infile: str, outfile: str) -> None:
	print("Background thread started.")
	with zipfile.ZipFile(outfile, "w") as myzip:
		myzip.write(infile)
	print("Background thread ended. ", infile)  # This thread is run in background (background thread).


print("Main thread started.")

myThread.start_new_thread(asyncZip, ("/home/punit/src/_not_mine/PythonTestBed/doc/Changelog.org", "/home/punit/src/_not_mine/PythonTestBed/var/new.zip"))
time.sleep(1)

print("Main thread ended.")  # This is main thread, running simultaneously.

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

with zipfile.ZipFile("/home/punit/src/_not_mine/PythonTestBed/tmp/Changelog.zip", "w") as myzip:
	myzip.write("/home/punit/src/_not_mine/PythonTestBed/doc/Changelog.org")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(readline.get_history_length())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN


def merge_lists() -> None:
	lengthList1 = input()
	lengthList2 = input()
	count = 0
	list1 = list2 = list3 = []
	while count < int(lengthList1):
		list1.append(int(input()))
	count = 0
	while count < lengthList2:
		list2.append(int(input()))

	i = j = 0
	while i < lengthList1 and j < lengthList2:
		if int(list1[i]) < int(list2[j]):
			list3.append(list1[i])
			i += 1
		else:
			list3.append(list2[j])
			j += 1

	list3 = list3 + list1[i:] + list2[j:]


if __name__ == "__main__":
	merge_lists()

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(math.pi)

print(math.sqrt(-1))
print(str(math.sqrt(10))[0])

print(str(math.pi)[len(str(math.pi)) - 2])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(len(list(myString)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print("%s, %s, and %s, ma'am" % ("wham", "bang", "thank you"))
print("{}, {}, and {}, ma'am".format("wham", "bang", "thank you"))

print("{:,.2f} and {:+04d}".format(3000.14159, 3))
print("%+04d and %.3f" % (3, 30.300999))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(list("🌥".encode()))
print(list("🌥".encode("utf-16")))

print(list("🌥".encode("utf-32")))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(platform.version(), platform.release(), platform.python_version(),)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print("%e" % 31415.926)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print("Yes" if 1.1 + 2.3 == 3.3 else "No")
print((99999999999999999999999).bit_length() + 1)

print(complex(2 + -3j) * 3)
print(2 + -3j * 3)

print(cmath.cos(complex(2, -3)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(1 / math.e)

print(math.sqrt(math.sin(math.pi / 2)))
print(pow(2, 4))

print(abs(-2))
print(max(1, 2, 3, 4), min(1, 2, 3, 4))

print(math.floor(-2.1))
print(math.trunc(-2.1))

print(round(-2.1111, 2))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

mySet1 = set("mySet1")
mySet2 = set("mySet2")

mySet1 = mySet1.intersection(mySet2)
print(mySet1)

mySet1.add("sets")
print(mySet1)

mySet2.update(["m", "y", "S", "e", "t", "3"])
print(mySet2)

mySet2.update("mySet4")
print(mySet2)

mySet2 = mySet2.union("mySet1")
print(mySet2)

print("yes subset" if {1, 2, 3, 9}.issubset(range(10)) else "not a subset")
print(dir(mySet2))

myList = [1, 2, 3, 4, 5, 4, 3, 2]
myList = list(set(myList))

print(myList)
print(set([1, 3, 5]) - set([1, 2, 3, 4, 5]))

print(set(dir(str)) - set(dir(bytes)))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(True + 4)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

list1 = [1, 2, 3]
list2 = list1

list2[2] = 4
print(list1)

list2 = list1[:]
list2[2] = 5

print(list1, list2)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print(sys.argv[0], len(sys.argv[0]))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

a = 14

b = 21
if (a // b) * b + (a % b) == a:
	print("True")

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

num = [4, 3, 1, 2]
num.sort()
print(num)
num.shuffle()
random.shuffle(num)
print(num)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

ab = [(20, 21), (11, 10), (00, 40)]
ab.sort(key = 2)
ab.sort(key = 1)
ab.sort(key = lambda mykey: mykey[1])
print(ab)

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))
print(fruits.reverse())
print(fruits)
print(fruits.append("grape"))
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.pop())

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

row1 = ["00", "01", "02"]
row2 = ["10", "11", "12"]
matrix = [row1, row2]
print(matrix)
print(matrix[0][1])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print([1, 2] < [2, 1])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

print("Decimal is fixed-precision unlike floating-points" if decimal.Decimal("1.11") + decimal.Decimal("2.22") == decimal.Decimal("3.33") else "it's not")
print(decimal.Decimal.from_float(1.11))

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# UNKNOWN

pprint.pprint([[[["test", "ok", "4", "3"]], [["test", "1", "2", "1"]]]], width = 1)
listed = [[[["test", "ok", "4", "3"]], [["test", "1", "2", "1"]]]]
[print(a) for a in listed]
for x in listed:
	print(" ".join(map(str, x)))


def f(listed: list) -> list:
	yield from listed


for x in f(listed):
	print(*x)

print("\n".join(" ".join(map(str, list101)) for list101 in listed))
for _ in listed:
	print(*[e[0] for e in listed])

print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
