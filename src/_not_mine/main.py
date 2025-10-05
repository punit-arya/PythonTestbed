#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations, division

import _thread
import array
import ast
import bisect
import builtins
import cmath
import collections
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
import operator
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
import shelve
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
import tkinter as tk
import typing
import unittest
import urllib.request
import weakref
import zipfile
import zlib

import __main__
import circularImport
import docstrings
import module1
import module2
import module3
import module4
import module5

# import src._not_mine.module6 as module6
import module6
import module7
import moduleFib

# 200 /home/punit/src/_not_mine/PythonTestBed/var/in.txt /home/punit/src/_not_mine/PythonTest1Bed/var/in.txt function41

"""PythonTestBed: Python test bed."""

# # TUTORIAL
#
# the_world_is_flat = True
# if the_world_is_flat:
# 	print("Be careful not to fall off!")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(17 / 3)
# print(17 // 3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(-(3 ** 2))
# print((-3) ** 2)
# print(5 ** 2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("doesn't")
# print("doesn't")
# print('"Yes," he said.')
# print('"Yes," he said.')
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string1 = "First line.\nSecond line."
# print(string1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("C:\some\name")
# print(r"C:\some\name")  # Note the "r" before the quote
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("""\
# Usage: thingy [OPTIONS]
#         -h				Display this usage message
#         -H	hostname	Hostname to connect to
# """)  # If we don't escape the newline there, it is embedded in the string.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(3 * "un" + "ium")
#
# print("Py"
# "thon")  # Concatenation.  Works with literals only, no variables or expressions.  Works across literal newline characters if enclosed within parentheses.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# prefix = "Py"
# # print(prefix "thon")
# # print(("un" * 3) "ium")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(prefix + "thon")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string2 = "Put several strings within parentheses " "to have them joined together."
# print(string2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string3 = "Python"
# print(string3[0])
# print(string3[-1])
# print(string3[-2])
# print(string3[-6])
# print(string3[: 2] + string3[2 :])
# print(string3[: 2])
# print(string3[0 : 2])
# print(string3[4 :])
# print(string3[-2 :])
# print(string3[-2 :-4])
# print(string3[-4 :-2])
# print(string3[-4 :-2 :-1])
# print(string3[-2 :-4 :-1])
# print(string3[4 : 42])
# print(string3[42 :])
#
# try:
# 	string3[0] = "J"
# 	print("J" + string3[1 :])
# except TypeError as ex:
# 	print(sys.exc_info()[0].__name__ + ":", ex, "\n")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN.
#
# list1 = [[0, 1], [2, 3], [4, 5]]
# print(list1[1])
# list1[1] = [10, 11]
# print(list1[1])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string4 = "supercalifragilisticexpialidocious"
# print(len(string4))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# squares = [1, 4, 9, 16, 25]
# print(squares)
# print(squares[0])
# print(squares[-1])
# print(squares[-3 :])
# print(squares[:])
# squares = squares + [36, 49, 64, 81, 100]
# print(squares)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# cubes = [1, 8, 27, 65, 125]
# cubes[3] = 64
# print(cubes)
# print(cubes.append(216))
# cubes.append(7 ** 3)  # Add the cube of 7.
# print(cubes)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# letters = ["a", "b", "c", "d", "e", "f", "g"]
# print(letters)
# letters[2 : 5] = ["C", "Class3", "E"]
# print(letters)
# letters[2 : 5] = []
# print(letters)
# letters[:] = []
# print(letters)
# letters = ["a", "b", "c", "d"]
# print(len(letters))
# list2 = ["a", "b", "c"]
# list3 = [1, 2, 3]
# list4 = [list2, list3]
# print(list4)
# print(list4[0])
# print(list4[0][1])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# maxNumber = 1
# number1, number2 = 0, 1
# while number2 < maxNumber:
# 	print(number2)
# 	number1, number2 = number2, number1 + number2
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# number3, number4 = 0, 1
# maxNumber = 1000
# while number4 < maxNumber:
# 	print(number4, end = ",")  # Don't append a newline to output, instead replace it with ",".  "end" is a keyword.
# 	number3, number4 = number4, number3 + number4
# print()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# number5 = int(input("Integer ? "))
# if number5 < 0:
# 	number5 = 0
# 	print("Negative changed to zero.")
# elif number5 == 0:
# 	print("Zero.")
# elif number5 == 1:
# 	print("Single.")
# else:
# 	print("More")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# words = ["cat", "window", "defenestrate"]
# for word in words:  # "for" iterates over the items of any sequence (a list or a string).  This form can not modify the items.
# 	print(word, len(word))
#
# length = 6
# for word in words[:]:  # Makes a copy of "words" to enable modification.
# 	if len(word) > length:
# 		words.insert(0, word)
# print(words)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i in range(5):
# 	print(i)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# list5 = ["Mary", "had", "a", "little", "lamb"]
# for i in range(len(list5)):  # Use "enumerate()" function instead.
# 	print(i, list5[i])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(range(10))  # "range(0, 10)" Doesn't work because "range" doesn't return a list.  Instead, it returns an iterator object to save space.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(list(range(5)))  # Creates list from iterables.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i in range(2, 10):
# 	for j in range(2, i):
# 		if i % j == 0:
# 			print(i, "equals", j, "*", i // j)
# 			break
# 		else:
# 			print(i, "is a prime number")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i in range(2, 10):
# 	if i % 2 == 0:
# 		print("Found an even number", i)
# 		continue
# 	print("Found a number", i)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# # while True:
# # 	pass
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Class1:
# 	pass
#
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def initlog(*args: None) -> None:
# 	pass
#
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def fib(number6: int) -> None:
# 	"""Print Fibonacci series up to "number6"."""
#
# 	a, b = 0, 1
# 	while a < number6:
# 		print(a, end = " ")
# 		a, b = b, a + b
# 	print()
#
#
# fib(2000)
# print(fib)
# function1 = fib
# print(function1(100))
# fib(0)
# print(fib(0))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def fib1(number7: int) -> int:
# 	"""Return a list containing the Fibonacci series up to "number7"."""
#
# 	retval = []
# 	a, b = 0, 1
# 	while a < number7:
# 		retval.append(a)
# 		a, b = b, a + b
# 	return retval
#
#
# function2 = fib1(100)
# print(function2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def ask_ok(prompt: str, retries: int = 4, reminder: str = "Please try again!") -> bool:
# 	while True:
# 		ok = input(prompt)
# 		if ok in ("y", "ye", "yes"):  # "in" is a keyword.  Tests whether a value is in a sequence.
# 			return True
# 		if ok in ("n", "no", "nop", "nope"):
# 			return False
# 		retries = retries - 1
# 		if retries < 0:
# 			message = "Invalid user response."
# 			raise ValueError(message)
# 		print(reminder)
#
#
# print(ask_ok("Do you really wanna quit ? "))
# print(ask_ok("OK to overwrite the file ? ", 2))
# print(ask_ok("OK to overwrite the file ? ", 2, "Come on, only yes or no!"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# number8 = 5
#
#
# def function3(arg: int = number8) -> None:
# 	print(arg)
#
#
# number8 = 8
# function3()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def function4(number9: int, list6: list = []) -> list:
# 	list6.append(number9)
# 	return list6
#
#
# print(function4(1))
# print(function4(2))
# print(function4(3, [4, 5]))
# print(function4(6, [7, 8]))
# print(function4(3, [4, 5]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def function5(number10: int, list7: list | None = None) -> None:
# 	if list7 is None:
# 		list7 = []
#
#
# def function50(number46, list100 = []):
# 	list100.append(number46)
# 	return list100
#
#
# print(function5(1))
# print(function5(2))
# print(function5(3))
# print(function50(1))
# print(function50(2))
# print(function50(3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# # "parrot" accepts one positional argument (the value of this argument is taken from the first argument in the function call) and three keyword (or optional) arguments.
#
#
# def parrot(voltage: int, state: str = "a stiff", action: str = "voom", type1: str = "Norwegian Blue") -> None:
# 	print("-- This parrot wouldn't", action, end = " ")
# 	print("if you put", voltage, "volts through it.")
# 	print("-- Lovely plumage, the", type1)
# 	print("-- It's", state, "!")
#
#
# parrot(1000)  # 1 positional argument.
# parrot(voltage = 1000)  # 1 keyword argument.
# parrot(voltage = 1000000, action = "VOOOOOM")  # 2 keyword arguments.
# parrot(action = "VOOOOOM", voltage = 1000000)  # 2 keyword arguments.
# parrot("a million", "bereft of life", "jump")  # 3 positional arguments.
# parrot("a thousand", state = "pushing up the daisies")  # 1 positional, 1 keyword.
# # parrot()
# # parrot(voltage = 5.0, "dead")	# Invalid call because "dead" is not a keyword argument so should be at the first position.  i.e., keyword arguments must follow positional arguments.
# # parrot(110, voltage = 220)	# Invalid, because duplicate values1 for same argument.
# # parrot(actor = "John Cleese")	# Keyword argument name is misspelt.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def cheeseshop(kind: str, *args: tuple, **keywords: dict) -> None:
# 	print("-- Do you have any", kind, "?")
# 	print("-- I'm sorry, we're all out of", kind)
# 	for a in args:
# 		print(a)
# 	print("-" * 40)
# 	keys = sorted(keywords.keys())
# 	for k in keys:
# 		print(k, ":", keywords[k])
#
#
# cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper = "Michael Palin", client = "John Cleese", sketch = "Cheese Shop Sketch")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def concat(*args: typing.Iterable, sep: str = "/") -> None:
# 	return sep.join(args)
#
#
# print(concat("earth", "mars", "venus"))
# print(concat("earth", "mars", "venus", sep = "."))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(list(range(3, 6)))
# args = [3, 6]
# print(list(range(*args)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def parrot(voltage: str, state: str = "a stiff", action: str = "voom") -> None:
# 	print("-- This parrot wouldn't", action, end = " ")
# 	print("if you put", voltage, "volts through it.", end = " ")
# 	print("E's", state, "!")
#
#
# dict21 = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# print(parrot(**dict21))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def make_incrementor(addend: int) -> None:
# 	return lambda augend: augend + addend
#
#
# lambda1 = make_incrementor(42)  # "make_incrementor" makes and returns the adder and assigns to "lambda1" which is a reference to a function.
# print(lambda1(0))  # Calling the lambda function with 0 assigns the 0 argument to "augend".  0 = "augend", 42 = "addend".
# print(lambda1(1))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]  # Two-dimensional array: four rows, two columns.
# pairs.sort(key = lambda pair: pair[1])  # "sort" takes no arguments, or one argument which should be a lambda function.  This lambda function should return the "key".  The elements of the "pairs" array is passed as an argument to the lambda function that is known as "pair" inside the lambda function.  In other words, the "key" argument can take a lambda function which returns a "key".  "key" can be a subscript if each element is an array or dot-notation attribute access if each element is an object (this will mean that the list is a collection of objects).
# print(pairs)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def function6() -> None:
# 	"""Do nothing, but document it.
#
#     No, really, it doesn't do anything."""
#
#
# print(function6.__doc__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def function7(ham: str, eggs: str = "eggs") -> str:
# 	print("Annotations:", function7.__annotations__)
# 	print("Arguments:", ham, eggs)
# 	return ham + " and " + eggs
#
#
# print(function7("spam"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# list9 = [10, 11, 12, 13, 14, 10]
# print("list9:", list9)
# print("list9.count(10):", list9.count(10), "list9.count(14):", list9.count(14), 'list9.count("x"):', list9.count("x"))
# print("list9.insert(2, 11.5):", list9.insert(2, 11.5))  # 11.5 will be inserted at the index 2.  "list9.insert(len(list9), element)" is same as "list9.append(element)".
# print("list9:", list9)
# print("list9.append(15):", list9.append(15))  # Equivalent to: "list9[len(list9):] = [element]"
# print("list9:", list9)
# print("list9.index(15):", list9.index(15))  # Return the index of the item 15.
# print("list9.remove(15):", list9.remove(15))  # Removes the occurrence of 15.  Returns an error if the element is not found.
# print("list9:", list9)
# print("list9.reverse():", list9.reverse())  # Reverse the elements of the list in place.
# print("list9:", list9)
# print("list9.sort():", list9.sort())
# print("list9:", list9)
# print("list9.pop():", list9.pop())  # If argument to "pop" is not given, it removes and returns the last item in the list.
# print("list9:", list9)
# print("list9.extend(list9):", list9.extend(list9))  # Equivalent to: "list[len(list9):] = list25".
# print("list9:", list9)
# print("list9.count(10):", list9.count(10))  # Return the number of times 10 appears in the list.
# print("list9:", list9)
# print("list9.sort(key=None, reverse=False):", list9.sort(key = None, reverse = False))  # Sort the items of the list in place.  See "sorted()" for explanation of the optional arguments.
# print("list9.pop(2):", list9.pop(2))  # List passed instead of integer.
# print("list9:", list9)
# print("list9.clear():", list9.clear())  # Equivalent to "del list9[:]".
# print("list9:", list9)
# copyOflist9 = list9.copy()  # Return a shallow copy of the list.  Equivalent to "list9[:]".
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# stack1 = [3, 4, 5]
# stack1.append(6)
# stack1.append(7)
# print(stack1)
# print(stack1.pop())
# print(stack1)
# print(stack1.pop())
# print(stack1.pop())
# print(stack1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# queue1 = collections.deque(["Eric", "John", "Michael"])
# queue1.append("Terry")
# queue1.append("Graham")
# print(queue1.popleft())
# print(queue1.popleft())
# print(queue1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# squares1 = []
# for i in range(10):
# 	squares1.append(i ** 2)
# print(squares1)
# print(i)
#
# for i in range(3):
# 	for j in range(4):
# 		for k in range(5):
# 			print("i, j, k:", i, j, k)
# print(i, j, k)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# squares2 = list(map(lambda p: p ** 2, range(10)))  # Equivalent.  List comprehension.
#
# print(squares2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# squares3 = [i ** 2 for i in range(10)]
# print(squares3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print([(i, j) for i in [1, 2, 3] for j in [3, 1, 4] if i != j])  # Equivalent to:
#
# combined = []
# for i in [1, 2, 3]:
# 	for j in [3, 1, 4]:
# 		if i != j:
# 			combined.append((i, j))
# print(combined)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# vector1 = [-4, -2, 0, 2, 4]
# print([co * 2 for co in vector1])
# print([co for co in vector1 if co >= 0])
# print([abs(co) for co in vector1])
# freshFruits = ["	 banana", "  loganberry ", "passion fruit  "]
# print([weapon.strip() for weapon in freshFruits])
# print([(i, i ** 2) for i in range(6)])  # To create a list of tuples.
# print([i, i ** 2] for i in range(6))
# vector1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([co for list9 in vector1 for co in list9])  # Flatten a list of tuples using listcomp.
# print([str(round(math.pi, i)) for i in range(1, 6)])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(matrix)
# print([[r[i] for r in matrix] for i in range(4)])
# transposed = []
# for i in range(4):
# 	transposed.append([r[i] for r in matrix])
# print(transposed)
# transposed = []
# for i in range(4):
# 	transposedRow = []
# 	# for r in matrix:
# 	# 	transposedRow.append(r[i])
# 	[transposedRow.append(r[i]) for r in matrix]
# 	transposed.append(transposedRow)
# print(transposed)
# print(list(zip(*matrix)))  # Better than list comprehension.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# list8 = [-1, 1, 66.25, 333, 333, 1234.5]
# del list8[0]
# print(list8)
# del list8[2 : 4]
# print(list8)
# del list8[:]
# print(list8)
# del list8  # Deletes entire variable.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# tuple1 = 12345, 54321, "hello!"
# print(tuple1[0])
# print(tuple1)
# tuple2 = tuple1, (1, 2, 3, 4, 5)
# print(tuple2)
# print(tuple1[0])
# tuple3 = ([1, 2, 3], [3, 2, 1])
# print(tuple3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# emptyTuple = ()
# singleton = ("hello",)
# print(len(emptyTuple))
# print(len(singleton))
# print(singleton)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# tuple4 = 12345, 54321, "hello!"  # Packing a tuple.
# print(tuple4)
# e1, e2, e3 = tuple4  # Unpacking a tuple.  This can work for any sequence.
# print(e1, e2, e3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# basket = {"apple", "orange", "apple", "pear", "banana"}
# print(basket)
# print("orange" in basket)
# print("crabgrass" in basket)
# set1 = set("abracadabra")
# set2 = set("alacazam")
# print(set1)
# print(set1 - set2)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 ^ set2)
# set3 = {c for c in "abracadabra" if c not in "abc"}
# print(set3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# tel = {"jack": 4098, "sape": 4139}
# tel["guido"] = 4127
# print(tel)
# print(tel["jack"])
# del tel["sape"]
# tel["irv"] = 4127
# print(tel)
# print(list(tel.keys()))  # List of all keys in arbitrary order.
# print(sorted(tel.keys()))  # Sorted keys.
# print("guido" in tel)
# print("jack" not in tel)
# print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
# print({it: it ** 2 for it in (2, 4, 6)})  # Dict comprehensions.
# print(dict(sape = 4139, guido = 4127, jack = 4098))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# knights = {"gallahad": "the pure", "robin": "the brave"}
# for k, v in knights.items():
# 	print(k, v)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i, e in enumerate(["tic", "tac", "toe"]):
# 	print(i, e)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# questions = ["name", "quest", "favorite color"]
# answers = ["lancelot", "the holy grail", "blue"]
# for e1, e2 in zip(questions, answers):
# 	print(f"What is your {e1}?  It is {e2}.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i in reversed(range(1, 10, 2)):
# 	print(i)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
# for m in sorted(set(basket)):  # "sorted" takes any sequence and returns a new list.
# 	print(m)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# rawData = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
# filteredData = []
# # for value in rawData:
# # 	if not math.isnan(value):
# # 		filteredData.append(value)
# filteredData = [filteredData.append(e) for e in rawData if not math.isnan(e)]
# print(filteredData)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string5, string6, string7 = "", "Trondheim", "Hammer Dance"
# nonNull = string5 or string6 or string7
# print(nonNull)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print((1, 2, 3) < (1, 2, 4))
# print([1, 2, 3] < [1, 2, 4])
# string8 = "C"
# string9 = "Pascal"
# string10 = "Python"
# print("ABC" < string8 < string9 < string10)
# print((1, 2, 3, 4) < (1, 2, 4))
# print((1, 2) < (1, 2, -1))
# print((1, 2, 3) == (1.0, 2.0, 3.0))
# print((1, 2, ("aa", "ab")) < (1, 2, ("abc", "a"), 4))
# # print((1, 2, 3) < [1, 2, 4])
# print(1 / 3 <= 100 / 300)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(moduleFib.fib(1000))
# print(moduleFib.fib1(100))
# print(moduleFib.__name__)
# fib = moduleFib.fib
# print(fib(500))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# if __name__ == "__main__":
# 	print(fib(int(sys.argv[1])))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# # print(sys.ps1)
# # print(sys.ps2)
# # sys.ps1 = "C> "
# # print(sys.ps1)
# sys.path.append("/home/punit/lib/python")
# print(sys.path)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("dir(moduleFib):", dir(moduleFib))
# print("dir(sys):", dir(sys))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# list9 = [1, 2, 3, 4, 5]
# fib2 = moduleFib.fib
# print("dir():", dir())
#
# print("dir(builtins):", dir(builtins))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(str(1))
# print(str(1.0))
# print(str(1.1))
# print(str("ab"))
# print(str((1, 2, 3)))
# print(str([1, 2, 3]))
# print(str({1, 2, 3}))
# print(str({"a": 1, "b": 2}))
# print(repr(1))
# print(repr(1.0))
# print(repr(1.1))
# print(repr("ab"))
# print(repr((1, 2, 3)))
# print(repr([1, 2, 3]))
# print(repr({1, 2, 3}))
# print(repr({"a": 1, "b": 2}))
# string11 = "Hello, world!"
# print(repr(string11))
# print(str(1 / 7))
# number9 = 10 * 3.25
# number10 = 200 * 200
# string12 = "Value of number9 is " + repr(number9) + " and number10 is " + repr(number10) + "..."
# print(string12)
# hello = "Hello, world!\n"
# helloAsRepr = repr(hello)
# print(helloAsRepr)
# print(repr((number9, number10, ("spam", "eggs"))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for i in range(1, 11):
# 	print(repr(i).rjust(2), repr(i * i).rjust(3), end = " ")
# 	print(repr(i * i * i).rjust(4))
#
# for i in range(1, 11):
# 	print(f"{i:2d} {i * i:3d} {i * i * i:4d}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("12".zfill(5))
# print("-3.14".zfill(7))
# print("3.14159265359".zfill(5))
# print('We are the {} who say "{}!"'.format("knights", "Ni"))
# print("{} and {}".format("spam", "eggs"))
# print("{} and {}".format("spam", "eggs"))
# print("This {food} is {adjective}.".format(food = "spam", adjective = "absolutely horrible"))
# print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other = "George"))
# contents = "eels"
# print("My hovercraft is full of {}.".format(contents))
# print("My hovercraft is full of {!r}.".format(contents))
# print("My hovercraft is full of {!s}.".format(contents))
# print("My hovercraft is full of {!a}.".format(contents))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(f"Value of PI is approximately {math.pi:.3f}.")
#
# table1 = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
# for name, phone in table1.items():
# 	print(f"{name:10} ==> {phone:10d}")
#
# table2 = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637378}
# print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}: Dcab: {0[Dcab]:d}".format(table2))
#
# table3 = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
# print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(f"The value of PI is approximately {math.pi:5.3f}.")
#
# # with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file1:
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file1:
# 	print("1:", file1.read())
# 	print("2:", file1.read())
# 	print("3:", file1.readline())
#
# # with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file2:
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file2:
# 	for l in file2:
# 		print(l, end = "")
#
# file3 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.txt", "w")
# file3.write("This is a test\n")
# tuple27 = ("the answer", 42)
# string13 = str(tuple27)
# print("string13:", string13)
# file3.write(string13)
# file3.close()
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.txt", "rb+") as file4:
# 	print(file4.write(b"0123456789abcdef"))
# 	print(file4.seek(5))
# 	print(file4.read(1))
# 	print("seek:", file4.seek(-3, 2))
# 	print("read:", file4.read(1))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file5:
# 	contents1 = file5.read()
# print(file5.closed)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(json.dumps([1, "simple", "list"]))
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out1.txt", "w") as file6:
# 	list11 = [1, "simple", "list"]
# 	json.dump(list11, file6)
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out1.txt") as file7:
# 	list12 = json.load(file7)
# 	print(list12)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# while True:
# 	try:
# 		number11 = int(input("Please enter a number: "))
# 		break
# 	except ValueError:
# 		print("Oops! Invalid number.")
# 	except (RuntimeError, TypeError, NameError):
# 		pass
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Error1(Exception):
# 	pass
#
#
# class Error2(Error1):
# 	pass
#
#
# class Error3(Error2):
# 	pass
#
#
# try:
# 	for Class2 in [Error1, Error2, Error3]:
# 		raise Class2
# except Error3:
# 	print("Error3")
# except Error2:
# 	print("Error2")
# except Error1:
# 	print("Error1")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# while True:
# 	try:
# 		with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in1.txt") as file8:
# 			string14 = file8.readline()
# 			number12 = int(string14.strip())
# 	except OSError as ex:
# 		print(f"OS error: {ex}.")
# 	except ValueError:
# 		print("Could not convert data to an integer.")
# 	except:
# 		print("Unexpected error:", sys.exc_info()[0])
# 		raise
# 	break
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# try:
# 	for a in sys.argv[2 :]:
# 		file9 = pathlib.Path.open(a)
# except OSError:
# 	print("can not open", a)
# else:
# 	print(a, "has", len(file9.readlines()), "lines")
# 	file9.close()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# try:
# 	message = "spam", "eggs", "thisIsATuple"
# 	# raise Exception(message)  # When we raised this exception, these arguments got packed into a tuple.
# 	raise Exception("spam", "eggs", "thisIsATuple")
# except Exception as ex:
# 	print(type(ex))
# 	print(ex.args)
# 	print("0:", ex.args[0])
# 	print("1:", ex.args[1])
# 	print("2:", ex.args[2])
# 	print(ex)  # Note that "__str__" may be overridden in exception subclasses.
# 	print("str(ex):", str(ex))
# 	print(ex.__str__())
# 	arg1, arg2, arg3 = ex.args
# 	print("arg1 = ", arg1)
# 	print("arg2 = ", arg2)
# 	print("arg3 = ", arg3)
#
#
# def tupleReversor(tuple5: tuple) -> None:
# 	reversedTuple = ()
# 	for it in tuple5[-1 ::-1]:
# 		reversedTuple += (it,)
# 	reversedTuple += (5,)
# 	reversedTuple += (6,)
#
# 	return reversedTuple
#
#
# print(tupleReversor((1, 2, 3, 4)))
#
# for it in reversed(("d", "c", "b", "a")):
# 	print(it)
#
#
# class AnotherTuple:
#
# 	def __init__(self, tuple6: tuple | None = None, dict1: dict | None = None) -> None:
# 		self.tuple6 = tuple6
# 		self.dict1 = dict1
#
# 	# def __init__(self, tuple6):
# 	# 	self.tuple6 = tuple6
#
# 	def printMe(self) -> None:
# 		print("Printing (self.tuple6):", self.tuple6)
# 		if self.dict1 is not None:
# 			print("Printing (self.dict1):", self.dict1)
#
#
# AnotherTuple(tuple6 = (1, 2, 3), dict1 = {"a": 1, "b": 2}).printMe()
# AnotherTuple(tuple6 = (1, 2, 3, 4)).printMe()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def this_fails() -> None:
# 	number14 = 1 / 0
#
#
# try:
# 	this_fails()
# except ZeroDivisionError as ex:
# 	print("ZeroDivisionError: Handling run-time error:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def raiseError(message: str) -> None:
# 	raise NameError(message)
#
#
# try:
# 	message = "Hi There"
# 	# raise NameError(message)
# 	raiseError(message)
# except NameError:
# 	print("NameError: An exception flew by!")  # raise
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# try:
# 	# raise KeyboardInterrupt
# 	pass
# finally:
# 	print("Goodbye, World!")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def divide(dividend: int, divisor: int) -> None:
# 	try:
# 		quotient = dividend / divisor
# 	except ZeroDivisionError:
# 		print("Division by zero!")
# 	else:
# 		print("Quotient is:", quotient)
# 	finally:
# 		print("In finally clause.")
#
#
# divide(2, 1)
# divide(2, 0)
# try:
# 	divide("2", "1")
# except TypeError as ex:
# 	print("TypeError:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def scope_test() -> None:
#
# 	def do_local() -> None:
# 		spam = "local spam"
#
# 	def do_nonlocal() -> None:
# 		nonlocal spam
# 		spam = "nonlocal spam"
#
# 	def do_global() -> None:
# 		global spam
# 		spam = "global spam"
#
# 	spam = "test spam"
# 	do_local()
# 	print("After local assignment:", spam)
# 	do_nonlocal()
# 	print("After nonlocal assignment:", spam)
# 	do_global()
# 	print("After global assignment:", spam)
#
#
# scope_test()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Complex:
#
# 	def __init__(self, realPart: float, imaginaryPart: float) -> None:
# 		self.realPart = realPart
# 		self.imaginaryPart = imaginaryPart
#
#
# complex2 = Complex(3.0, -4.5)
# print(complex2.realPart, complex2.imaginaryPart)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Class3:
# 	"""A simple example class."""
#
# 	number15 = 12345
#
# 	def function8(self) -> str:
# 		return "hello world"
#
#
# object1 = Class3()
# object1.counter = 1
# number15 = 10
# while object1.counter < number15:
# 	object1.counter = object1.counter * 2
# print(object1.counter)
# del object1.counter
#
# function9 = object1.function8
# # while True:
# print(function9())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Dog:
# 	kind = "canine"
#
# 	def __init__(self, name10: str) -> None:
# 		self.name10 = name
#
#
# dog1 = Dog("Fido")
# dog2 = Dog("Buddy")
# print(dog1.kind)
# print(dog2.kind)
# print(dog1.name10)
# print(dog2.name10)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class AnotherDog:
# 	tricks1: typing.ClassVar = []
#
# 	def __init__(self, name1: str) -> None:
# 		self.name1 = name1
#
# 	def another_add_trick(self, trick1: str) -> None:
# 		self.tricks1.append(trick1)
#
#
# anotherDog1 = AnotherDog("Fido")
# anotherDog2 = AnotherDog("Buddy")
# anotherDog1.another_add_trick("roll over")
# anotherDog2.another_add_trick("play dead")
# print("anotherDog1.tricks1:", anotherDog1.tricks1)
# print("anotherDog2.tricks1:", anotherDog2.tricks1)
#
# print("AnotherDog.tricks1:", AnotherDog.tricks1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class YetAnotherDog:
#
# 	def __init__(self, name2: str) -> None:
# 		self.name2 = name2
# 		self.tricks2 = []
#
# 	def yet_another_add_trick(self, trick2: str) -> None:
# 		self.tricks2.append(trick2)
#
#
# yetAnotherDog1 = YetAnotherDog("Fido")
# yetAnotherDog2 = YetAnotherDog("Buddy")
# yetAnotherDog1.yet_another_add_trick("roll over")
# yetAnotherDog2.yet_another_add_trick("play dead")
# print(yetAnotherDog1.tricks2)
# print(yetAnotherDog2.tricks2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# for e in [1, 2, 3]:
# 	print(e)
# for it in (1, 2, 3):
# 	print(it)
# for k in {"one": 1, "two": 2}:
# 	print(k)
# for c in "ABC":
# 	print(c)
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file10:
# 	for l in file10.readlines():
# 		print(l, end = "")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string15 = "abc"
# iterator1 = iter(string15)
# print(iterator1)
# print(next(iterator1))
# print(next(iterator1))
# try:
# 	while True:
# 		print(next(iterator1))
# except StopIteration as ex:
# 	print("StopIteration", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Reverse:
# 	"""Iterating for looping over a sequence backwards."""
#
# 	def __init__(self, string45: str) -> None:
# 		self.string45 = string45
# 		self.index = len(string45)
#
# 	def __iter__(self) -> Reverse:
# 		return self
#
# 	def __next__(self) -> str:
# 		if self.index == 0:
# 			raise StopIteration
# 		self.index = self.index - 1
# 		return self.string45[self.index]
#
#
# reversedSpam = Reverse("spam")
# print(iter(reversedSpam))
# for c in reversedSpam:
# 	print(c)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def reverse(string16: str) -> str:
# 	for i in range(len(string16) - 1, -1, -1):
# 		yield string16[i]
#
#
# for c in reverse("golf"):
# 	print(c)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(sum(i * i for i in range(10)))
# vector2 = [10, 20, 30]
# vector3 = [7, 5, 3]
# print(sum(x * y for x, y in zip(vector2, vector3)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# sineTable = {i: math.sin(i * math.pi / 180) for i in range(91)}
# print(sineTable)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string17 = "golf"
# print(list(string17[i] for i in range(len(string17) - 1, -1, -1)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(pathlib.Path.cwd())
# os.chdir("/home/punit/src/_not_mine/PythonTestBed/var/log/")
# # os.system("mkdir pythontestbed")
# print("chdir:", os.chdir("/home/punit/src/_not_mine/PythonTestBed/src/_not_mine"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print("dir(os):", dir(os))  # Returns a list of all module functions.
# print("help(os):", help(os))  # Returns an extensive manual page created from the module's docstrings.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(pathlib.Path.cwd())
# shutil.copyfile("/home/punit/src/_not_mine/PythonTestBed/var/in.txt", "/home/punit/src/_not_mine/PythonTestBed/var/copy_of_in.txt")
# shutil.move("/home/punit/src/_not_mine/PythonTestBed/var/copy_of_in.txt", "/home/punit/src/_not_mine/PythonTestBed/var/copy_of_in_moved.txt")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# # print(glob.glob("*.py"))
# print(pathlib.Path.glob(pathlib.Path("/home/punit/src/_not_mine/PythonTestBed"), "*.py"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(sys.argv)
# sys.stderr.write("Warning, log file not found starting a new one\n")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
# print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat"))
#
# print("tea for too".replace("too", "two"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(math.cos(math.pi / 4))
# print(math.log(1024 / 2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(random.choice(["apple", "pear", "banana"]))
# print(random.sample(range(100), 10))
# print(random.random())
# print(random.randrange(6))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# values1 = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
#
# print("statistics.mean(values1):", statistics.mean(values1))
# print("statistics.median(values1):", statistics.median(values1))
# print("statistics.mode(values1):", statistics.mode(values1))
# print("statistics.variance(values1):", statistics.variance(values1))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# try:
# 	# with urlopen("https://www.usno.navy.mil/USNO/time/display-clocks/simpletime") as response:
# 	with urllib.request.urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt", timeout = 5) as response:
# 		for l in response:
# 			l = l.decode("utf-8")
# 			if "EST" in l or "EDT" in l:
# 				print(l)
# 			else:
# 				print("l:", l)
# except (ConnectionResetError, urllib.error.URLError) as ex:
# 	print("ex:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# now = datetime.datetime.now(tz = datetime.timezone(datetime.timedelta(hours = 5.5))).date()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# birthday = datetime.date(1964, 7, 31)
# age = now - birthday
# print(age.days)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# bytes11 = b"which witch has which witch's wrist watch"
# print(len(bytes11))
# compressedBytes7 = zlib.compress(bytes11)
# print(len(compressedBytes7))
# print(zlib.decompress(compressedBytes7))
# print("crc32:", zlib.crc32(bytes11))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(timeit.Timer("t = a; a = b; b = t", "a = 1; b = 2").timeit())
# print(timeit.Timer("a, b = b, a", "a = 1; b = 2").timeit())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# def average(values2: list) -> float:
# 	"""Compute the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#
# 	return sum(values2) / len(values2)
#
#
# doctest.testmod(verbose = False)  # Automatically validate the embedded tests.
#
#
# class TestMyAverageFunction(unittest.TestCase):
#
# 	def test_average(self) -> None:
# 		number16 = 40.0
# 		# self.assertEqual(average([20, 30, 70]), 40.0)
# 		assert average([20, 30, 70]) == number16
# 		number17 = 4.3
# 		# self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
# 		assert round(average([1, 5, 7]), 1) == number17
# 		# with self.assertRaises(ZeroDivisionError):
# 		with self.pytest.Raises(ZeroDivisionError):
# 			average([])
# 		# with self.assertRaises(TypeError):
# 		# 	average([20, 30, 70])
#
#
# # unittest.main(argv = ["0"])  # Calling from the command line invokes all tests.
# unittest.main(exit = False)  # Calling from the command line invokes all tests.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(reprlib.repr(set("supercalifragilisticexpialidocious")))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# tuple8 = [[[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]]
#
# print("len(tuple8):", len(tuple8))
# print("len(tuple8[0]:", len(tuple8[0]))
# print("len(tuple8[0][0]):", len(tuple8[0][0]))  # Count the commas, 1 comma means 2 elements.
# print("len(tuple8[0][0][0]):", len(tuple8[0][0][0]))
# print("tuple8:", tuple8)
# print("tuple8[0]:", tuple8[0])
# print("tuple8[0][0]:", tuple8[0][0])
# print("tuple8[0][0][0]:", tuple8[0][0][0])
#
# pprint.pprint(tuple8, width = 30)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# docString1 = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
# print(textwrap.fill(docString1, width = 40))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# locale.setlocale(locale.LC_ALL, "en_US.utf-8")
# conventions = locale.localeconv()
# number18 = 1234567.8
# # print(locale.format("%d", number18, grouping=True))
# print(locale.format_string("%d", number18, grouping = True))
# print(locale.format_string("%s%.*f", (conventions["currency_symbol"], conventions["frac_digits"], number18), grouping = True))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# string19 = string.Template("${village} folk send $$10 to $cause.")
# print(string19.substitute(village = "Nottingham", cause = "the ditch fund"))
#
# string20 = string.Template("Return the $it to $owner.")
# dict2 = dict(item = "unladen swallow")
# try:
# 	print(string20.substitute(dict2))
# except KeyError as ex:
# 	print("KeyError:", ex)
# print(string20.safe_substitute(dict2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# photoFiles = ["img_1074.jpg", "img_1076.jpg", "img_1077.jpg"]
#
#
# class BatchRename(string.Template):
# 	delimiter = "%"
#
#
# string21 = input("Enter rename style (%d-date %n-seqnum %f-format): ")
# tuple9 = BatchRename(string21)
# date = time.strftime("%d%b%y")
# for i, fileName in enumerate(photoFiles):
# 	# base, extension = os.path.splitext(fileName)
# 	base, extension = pathlib.Path.stem, pathlib.Path.suffix
# 	newName = tuple9.substitute(d = date, n = i, f = extension)
# 	print(f"{fileName} --> {newName}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.zip", "rb") as file11:
# 	bytes6 = file11.read()
#
# start = 0
# for i in range(3):
# 	start += 14
# 	tuple24 = struct.unpack("<IIIHH", bytes6[start : start + 16])
# 	crc32, compressedSize, uncompressedSize, fileSize, extraSize = tuple24
#
# 	start += 16
# 	fileName = bytes6[start : start + fileSize]
# 	start += fileSize
# 	extra = bytes6[start : start + extraSize]
# 	print("Header ", i + 1, ":", sep = "", end = "")
# 	print(fileName, hex(crc32), compressedSize, uncompressedSize)
# 	start += extraSize + compressedSize
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class AsyncZip(threading.Thread):  # Like Java, we need to create a class that will create a thread object.
#
# 	def __init__(self, inputFile: string, outputFile: string) -> None:
# 		threading.Thread.__init__(self)  # This line should be there for every thread class in its "init".  Doesn't work.
# 		self.inputFile = inputFile  # Initialise other fields of your thread class.
# 		self.outputFile = outputFile
#
# 	def run(self) -> None:  # Define the operations to be done by the thread.
# 		zipFile1 = zipfile.ZipFile(self.outputFile, "w", zipfile.ZIP_DEFLATED)  # Operation step number one.
# 		zipFile1.write(self.inputFile)
# 		zipFile1.close()
# 		print("Finished background zip of:", self.inputFile)  # This thread is run in background ("background thread").
#
#
# background = AsyncZip("/home/punit/src/_not_mine/PythonTestBed/var/in.txt", "/home/punit/src/_not_mine/PythonTestBed/var/in1.zip")  # Create your thread.
# background.start()  # Start the execution of your thread.
# print("The main program continues to run in foreground.")  # This is main thread, running simultaneously.
#
# background.join()  # Wait for the background task to finish.
# print("Main program waited until background was done.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# logging.debug("Debugging information")
# logging.info("Informational message")
# logging.warning("Warning:config file %s not found", "server.conf")
# logging.error("Error occurred")
# logging.critical("Critical error -- shutting down")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
#
# class Class3:
#
# 	def __init__(self, value: any) -> None:
# 		self.value = value
#
# 	def __repr__(self) -> None:
# 		return str(self.value)
#
#
# object3 = Class3(10)
# weakDict1 = weakref.WeakValueDictionary()
# weakDict1["primary"] = object3
# print('weakDict1["primary"]:', weakDict1["primary"])
# del object3
# gc.collect()
# # print("weakDict1[\"primary\"]:", weakDict1["primary"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# array1 = array.array("H", [4000, 10, 700, 22222])  # "H" is typecode for 2-byte unsigned binary number, thus 2 bytes per entry.
# print("sum:", sum(array1))
# print("array1[1:3]:", array1[1 : 3])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# deque1 = collections.deque(["task1", "task2", "task3"])
# deque1.append("task4")
# print("Handling", deque1.popleft())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
# bisect.insort(scores, (300, "ruby"))
# print(scores)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# list13 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapq.heapify(list13)
# heapq.heappush(list13, -5)
# print([heapq.heappop(list13) for _ in range(3)])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(round(decimal.Decimal("0.70") * decimal.Decimal("1.05"), 2))
# print(round(0.70 * 1.05, 2))
#
# print(decimal.Decimal("1.00") % decimal.Decimal(".10"))
# print(1.00 % 0.10)
# print(sum([decimal.Decimal("0.1")] * 10) == decimal.Decimal("1.0"))
# print(sum([0.1] * 10) == 1.0)
#
# decimal.getcontext().prec = 36
# print(decimal.Decimal(1) / decimal.Decimal(7))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(format(math.pi, ".12g"))
# print(format(math.pi, ".2f"))
# print(repr(math.pi))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# number19 = 0.3
# print(number19 == 0.1 + 0.1 + 0.1)
#
# print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
#
# print(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# number20 = 3.14159
# print(number20.as_integer_ratio())  # Much more exact than smaller numbers for lossless recreation of original numbers.
# print(number20 == 3537115888337719 / 1125899906842624)
# print(number20.hex())
# print(number20 == float.fromhex("0x1.921f9f01b866ep+1"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(sum([0.1] * 10) == 1.0)
#
# print(math.fsum([0.1] * 10) == 1.0)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# print(2 ** 52 <= 2 ** 56 // 10 < 2 ** 53)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# quotient1, remainder1 = divmod(2 ** 56, 10)
# print(remainder1)
# print(quotient1 + 1)
#
# print(0.1 * 2 ** 55)
# print(3602879701896397 * 10 ** 55 // 2 ** 55)
# print(format(0.1, ".17f"))
#
# print(fractions.Fraction.from_float(0.1))
# print((0.1).as_integer_ratio())
# print(decimal.Decimal.from_float(0.1))
# print(format(decimal.Decimal.from_float(0.1), ".17"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# fileName = os.environ.get("PYTHONSTARTUP")
# if fileName is not None:
# 	# if os.path.isfile(".pythonrc.py"):
# 	if pathlib.Path.is_file(fileName):
# 		with pathlib.Path.open(fileName) as file121:
# 			fileContent = file121.read()
# 			exec(fileContent)
# else:
# 	print("Not defined.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # TUTORIAL
#
# fileName = os.environ.get("PYTHONSTARTUP")
# if fileName and pathlib.Path.is_file(fileName):
# 	with pathlib.Path.open(fileName) as file13:
# 		startUpFile = file13.read()
# 	exec(startUpFile)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # GLOSSARY
#
# print(site.getusersitepackages())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # GLOSSARY
#
# print(division)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # GLOSSARY.
#
# list14 = [f"{i:#04x}" for i in range(256) if i % 2 == 0]
# print(list14)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # GLOSSARY.
#
#
# class Class4:
#
# 	class Class5:
#
# 		def meth(self) -> None:
# 			pass
#
#
# print(Class4.__qualname__)
# print(Class4.Class5.__qualname__)
# print(Class4.Class5.__qualname__)
# print(Class4.Class5.meth.__qualname__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # GLOSSARY.
#
# print(email.mime.text.__name__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list15 = []
# print([e for e in dir(list15) if "__" not in e])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# number21 = 10
#
#
# def function10() -> None:
# 	print(number21)
#
#
# function10()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# number22 = 10
#
#
# def function11() -> None:
# 	print(number22)
#
#
# # number22 = 10
#
# function11()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# number23 = 10
#
#
# def function12() -> None:
# 	global number23
# 	print(number23)
# 	number23 = 20
#
#
# function12()
# print(number23)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function13() -> None:
# 	number24 = 10
#
# 	def function14() -> None:
# 		nonlocal number24
#
# 		print(number24)
# 		number24 += 1
#
# 	function14()
# 	print(number24)
#
#
# function13()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# squares4 = []
# for i in range(5):
# 	squares4.append(lambda: i ** 2)
#
# print(squares4)
# print(squares4[0](), squares4[1](), squares4[2]())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# squares5 = []
#
# for i in range(5):
# 	squares5.append(lambda number25 = i: number25 ** 2)
#
# print(squares5)
# print(squares5[0](), squares5[1](), squares5[2]())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print(module6.number1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function15(dict3: dict = {}) -> dict:  # Reference is shared with subsequent invocations.
# 	dict3["key2"] = 1
# 	print("dict3: 4:", dict3)
#
# 	return dict3
#
#
# dict4 = {}
# # dict4 = {"key1": 0, "key2": 1}
# dict4["key1"] = 0
# print("dict4: 1:", function15(dict4))  # r.t.l. evaluation and printing.
# print("dict4: 5:", dict4)
# print("dict4: 1:", function15(dict4))  # r.t.l. evaluation and printing.
# print("dict4: 5:", dict4)
# print("dict4: 2:", function15())
# print("dict4: 5:", dict4)
# print("dict4: 3:", function15())
# print("dict4: 5:", dict4)
#
#
# def addElement(e: any, list16: list = []) -> list:
# 	list16.append(e)
#
# 	return list16
#
#
# list17 = [0, 1, 2]
# print(addElement(3, list17))
# print(addElement(4, list17))
# print(addElement(0))
# print(addElement(1))  # Default argument's value is used and persisted across all invocations that don't specify that argument's value.
# print(addElement(5, list17))
# print(addElement(2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list18 = []
# list18 += [1, 2, 3]  # Is same as:
# list18.extend([1, 2, 3])
# print(list18)
# tuple10 = ()
# tuple10 += (1, 2, 3)  # Creates a new object, like:
# print(tuple10)
# number25 = 1
# number25 += 1
# print(number25)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function16(number26: int, number27: int) -> tuple(int, int):
# 	print("number26:", number26, "number27:", number27)
# 	number26 += 1
# 	number27 = number27 + 2
# 	print("number27:", number27, "number27:", number27)
# 	return number26, number27
#
#
# number28, number29 = 0, 1
# print("number28:", number28, "number29:", number29)
# number28, number29 = function16(number28, number29)
# print("number28:", number28, "number28:", number29)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function17(list19: list) -> None:
# 	list19[0] = 1
# 	list19[1] += 1
#
#
# args1 = [0, 1]
# function17(args1)
# print(args1[0], args1[1])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function18(dict22: dict) -> None:
# 	dict22["a"] = "1"
# 	dict22["b"] += "1"
#
#
# dict5 = {"a": "0", "b": "1"}
# function18(dict5)
# print(dict5["a"], dict5["b"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class CallByReference:
#
# 	def __init__(self, **dict23: dict) -> None:
# 		for k, v in dict23.items():
# 			setattr(self, k, v)
#
#
# def function19(dict24: dict) -> None:
# 	dict24.a = "1"
# 	dict24.b += 1
#
#
# object11 = CallByReference(a = "0", b = 1)
# function19(object11)
# print(object11.a, object11.b)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def Linear(number30: float, number31: float) -> None:
#
# 	def function20(number32: float) -> float:
# 		return number30 * number32 + number31
#
# 	return function20
#
#
# taxes = Linear(0.3, 2)
# print(taxes(10e6))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class Linear:
#
# 	def __init__(self, number33: float, number34: float) -> None:
# 		self.number33, self.number34 = number33, number34
#
# 	def __call__(self, number35: float) -> float:
# 		return self.number33 * number35 + self.number34
#
#
# taxes = Linear(0.3, 2)
# print(taxes(10e6))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class Counter:
# 	value = 0
#
# 	def up(self) -> None:
# 		self.value = self.value + 1
#
# 	def down(self) -> None:
# 		self.value = self.value - 1
#
# 	def set(self, value: int) -> None:
# 		self.value = value
#
#
# counter = Counter()
# increment, decrement, reset = counter.up, counter.down, counter.set
#
# print(increment, decrement, reset)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class Class8:
# 	pass
#
#
# Class9 = Class8
# object4 = Class9()
# object5 = object4
# print(object4)
# print(object5)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# string22 = "a"
# print(string22 in "b", string22)
# print((string22 in "b"), string22)
# print(string22 in ("b", string22))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print(list(filter(None, map(lambda y: y * functools.reduce(lambda x, y: x * y != 0, map(lambda x, y = y: y % x, range(2, int(pow(y, 0.5) + 1))), 1), range(2, 1000)))))
# print(list(map(lambda x, f = lambda x, f: (f(x - 1, f) + f(x - 2, f)) if x > 1 else 1: f(x, f), range(10))))
# number12 = 4.0
# print((lambda Ru, Ro, Iu, Io, IM, Sx, Sy: functools.reduce(lambda x, y: x + y, map(lambda y, Iu = Iu, Io = Io, Ru = Ru, Ro = Ro, Sy = Sy, L = lambda yc, Iu = Iu, Io = Io, Ru = Ru, Ro = Ro, i = IM, Sx = Sx, Sy = Sy: functools.reduce(lambda x, y: x + y, map(lambda x, xc = Ru, yc = yc, Ru = Ru, Ro = Ro, i = i, Sx = Sx, F = lambda xc, yc, x, y, k, f = lambda xc, yc, x, y, k, f: (k <= 0) or (x * x + y * y >= number12) or 1 + f(xc, yc, x * x - y * y + xc, 2.0 * x * y + yc, k - 1, f): f(xc, yc, x, y, k, f): chr(64 + F(Ru + x * (Ro - Ru) / Sx, yc, 0, 0, i)), range(Sx))): L(Iu + y * (Io - Iu) / Sy), range(Sy))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 5))  # Mandelbrot set.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# __import__("os").system("ls $HOME")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print(f"{144:04d}")
# print(f"{16:04x}")
# # print("{:.3f}".format(1.0 / 3.0))
# print(f"{1.0/3.0:.3f}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# string23 = "Hello, world!"
# stringIO = io.StringIO(string23)
# print(stringIO.getvalue())
# stringIO.seek(7)
# stringIO.write("there!")
# print(stringIO.getvalue())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# string24 = "Hello, world!"
# array2 = array.array("u", string24)
# print(array2)
# array2[0] = "y"
# print(array2)
# print(array2.tounicode())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function20() -> None:
# 	print("In function20.")
#
#
# def function21() -> None:
# 	print("In function21.")
#
#
# dispatch = {"call_function20": function20, "call_function21": function21}
# dispatch["call_function21"]()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class Char:
#
# 	def __init__(self, c: str) -> None:
# 		self.c = c
#
# 	def do_lower(self) -> str:
# 		return self.c.lower()
#
# 	def do_upper(self) -> str:
# 		return self.c.upper()
#
# 	do_u = do_upper
# 	do_l = do_lower
#
#
# operation = input("What do you want to do today ? ")
# if operation in ["lower", "l"]:
# 	char = Char("A")
# elif operation in ["upper", "u"]:
# 	char = Char("a")
# else:
# 	print("Invalid Choice.")
#
# function22 = getattr(char, "do_" + operation)
# print(function22())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def function23() -> None:
# 	print("Hello, world!")
#
#
# stringFunction = "function23"
# function24 = locals()[stringFunction]
# print("function24:", function24())
# function25 = eval(stringFunction)
# print("function25:", function25())
# try:
# 	function26 = ast.literal_eval(stringFunction)
# 	print("function26():", function26())
# except ValueError as ex:
# 	print("ValueError:", ex)
#
# # stringFunction1 = "var1 = 10"
# # stringFunction1 = "input('Enter a number:')"
# function27 = ast.literal_eval(input("Enter a number:"))
# # print("function27():", function27())
# number47 = ast.literal_eval(input("Enter a number:"))
# print("number47:", number47)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# string26 = "test\r\n"
# print(string26.rstrip("\r\n"))
#
# lines = "line\r\n\r\n\r\n"
# print(lines.rstrip("\n\r"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list19 = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]
# # list19 = ["a", "a", "b", "c", "d", "d", "e", "e", "f"]
# if list19:
# 	list19.sort()
#
# 	for i in range(len(list19) - 2, -1, -1):
# 		if list19[i] == list19[i + 1]:
# 			del list19[i + 1]
#
# print(list19)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list20 = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]
# # list20 = ["a", "a", "b", "c", "d", "d", "e", "e", "f"]
#
# if list20:
# 	list20.sort()
# 	last = list20[-1]
#
# 	for i in range(len(list20) - 2, -1, -1):
# 		if last == list20[i]:
# 			del list20[i]
# 		else:
# 			last = list20[i]
#
# print(list20)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list21 = ["f", "a", "c", "b", "a", "e", "d", "e", "d"]
#
# list21 = list(set(list21))
# print(list21)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# oneDimList = [1] * 2
# print("oneDimList:", oneDimList)
# oneDimList1 = [None] * 2
# print("oneDimList1:", oneDimList1)
# multiDimList = [[None] * 2] * 3
# print("multiDimList:", multiDimList)
# print("multiDimList[0][0]:", multiDimList[0][0])
# multiDimList[0][0] = 0
# print("multiDimList:", multiDimList)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list22 = [None] * 3
# for i in range(3):
# 	list22[i] = [None] * 2
# print(list22)
# list22[0][0] = 1
# print(list22)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# w, h = 2, 3
# list23 = [[None] * w for _ in range(h)]
# print(list23)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# tuple11 = (["1"], "2")
# # tuple11[0] += ["one"]
# print(tuple11)
# print(tuple11[0])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list24 = []
# list24 += [1]
# print(list24)
# list24.extend([2])
# print(list24)
# list24 = list24.__add__([3])
# print(list24)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# list25 = ["4", "8", "3", "2", "9", "1", "6", "0"]
# print(sorted(list25))
# list26 = ["c", "a", "g", "e", "b", "d"]
# print(sorted(list26))
# list27 = ["186", "185", "199", "131", "198", "121", "195", "105", "193", "183"]
# list27.sort(key = lambda s: int(s[1]))
# print(list27)
# list28 = [186, 185, 199, 131, 198, 121, 195, 105, 193, 183]
# list28.sort(key = lambda s: str(s)[1])
# print(list28)
# list29 = ["186", "185", "199", "131", "198", "121", "195", "105", "193", "183"]
# list29.sort(key = lambda s: s[1])
# print(list29)
# list30 = ["18606", "18335", "19569", "13421", "11918", "12281", "19255", "10575", "14923", "12813"]
# list30.sort(key = lambda s: s[1 : 3])
# print(list30)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# husbands = ["zero", "one", "two", "three", "four", "five", "six", "seven"]
# wives = ["eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
# children = ["sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty"]
# families = zip(husbands, wives, children)
# print("Families:", families)
# familiesSortedByHusbands = sorted(families)
# print("sortedFamilies:", familiesSortedByHusbands)
# sortedHusbands = [family[0] for family in familiesSortedByHusbands]
# print(sortedHusbands)
# sortedWives = [family[1] for family in familiesSortedByHusbands]
# print(sortedWives)
# sortedChildren = [family[2] for family in familiesSortedByHusbands]
# print(sortedChildren)
# wivesAnotherWay = []
# for family in familiesSortedByHusbands:
# 	wivesAnotherWay.append(family[1])
# print("wivesAnotherWay:", wivesAnotherWay)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class Class6:
# 	classVariableObjectsCount = 0
#
# 	def __init__(self) -> None:
# 		Class6.classVariableObjectsCount += 1
#
# 	def printCount(self) -> None:
# 		print("Class6.classVariable:", Class6.classVariableObjectsCount)
# 		print("self.classVariable:", self.classVariableObjectsCount)
#
#
# print("Class6.classVariableObjectsCount:", Class6.classVariableObjectsCount)
# object6 = Class6()
# print("printCount:")
# object6.printCount()
# print("Class6.classVariableObjectsCount:", Class6.classVariableObjectsCount)
# print("Creating module7 object:")
# object7 = Class6()
# print("Class6.classVariableObjectsCount:", Class6.classVariableObjectsCount)
# print("printCount:")
# object7.printCount()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print("0:", id(0))
# print("0:", id(0))
# print("0:", id(0))
# print("1:", id(1))
# print("0:", id(0))
# print("1:", id(1))
# print("2:", id(2))
# print("0:", id(0))
# print("1:", id(1))
# var300 = 0
# var301 = 1
# var302 = 2
# var303 = 3
# print("var300:", id(var300))
# print("var301:", id(var301))
# print("var302:", id(var302))
# print("var303:", id(var303))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# py_compile.compile("/home/punit/src/_not_mine/PythonTestBed/src/_not_mine/main.py")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print("module4.module4Var:", module4.module4Var)
# # print("module5Var:", module5.module5Var)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# print("os:")
# for k, v in inspect.getmembers(os):
# 	print("KEY:", k)
# 	print("VALUE:", v, end = "\n\n")
#
# print("os.path:")
# for k, v in inspect.getmembers(os.path):
# 	print("KEY:", k)
# 	print("VALUE:", v, end = "\n\n")
#
# print("os.path.samestat:")
# for k, v in inspect.getmembers(os.path.samestat):
# 	print("KEY:", k)
# 	print("VALUE:", v, end = "\n\n")
#
# print("os.path.genericpath.samestat:")
# for k, v in inspect.getmembers(os.path.genericpath.samestat):
# 	print("KEY:", k)
# 	print("VALUE:", v, end = "\n\n")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# importlib.reload(module4)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# object8 = module2.Class1(1)
# print(module2.Class1.getMember(object8))
# object8 = module2.Class1(2)
# print(module2.Class1.getMember(object8))
# print(isinstance(object8, module2.Class1))
# print(hex(id(object8.__class__)))
# print(hex(id(module2.Class1)))
# importlib.reload(module2)
# print(isinstance(object8, module2.Class1))
# print(hex(id(object8.__class__)))
# print(hex(id(module2.Class1)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def caseA() -> int:
# 	return hex(ord("A"))
#
#
# def caseB() -> int:
# 	return hex(ord("B"))
#
#
# def caseC() -> int:
# 	return hex(ord("C"))
#
#
# switch = {"A": caseA, "B": caseB, "C": caseC}
# executeSwitch = switch["A"]
# print(executeSwitch())
# executeSwitch = switch["B"]
# print(executeSwitch())
# executeSwitch = switch["C"]
# print(executeSwitch())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# print(os.listdir("."))  # Returns all files in the current directory.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# class GoToLabelError(Exception):
# 	print("GoToLabelError.")
#
#
# def raiseGoToLabel() -> None:
# 	raise GoToLabelError
#
#
# try:
# 	if True:
# 		raiseGoToLabel()
# except GoToLabelError:
# 	print("Except.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
#
# def threadTask(threadName: str, threadNum: int) -> None:
# 	time.sleep(1)
# 	print("Entering thread:", threadNum)
# 	# print("Entering sleep:", threadNum)
# 	# print("Exiting sleep:", threadNum)
# 	for _ in range(threadNum):
# 		print(threadName, threadNum)
# 	print("Exiting thread:", threadNum)
#
#
# for i in range(10):
# 	print("Starting thread:", i)
# 	thread1 = threading.Thread(target = threadTask(str(i), i))
# 	thread1.start()
# 	print("Ending thread:", i)
#
# # time.sleep(12)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# """
# The job of the worker is to take an element from the queue and print it.
# """
#
#
# def worker() -> None:
# 	print("Running Worker:", threading.current_thread().name)
# 	time.sleep(0.1)
# 	while True:
# 		try:
# 			arg = tasksQueue.get(block = False)
# 		except queue.Empty:
# 			print("Worker:", threading.current_thread().name, "Empty.")
# 			break
# 		else:
# 			print("Worker:", threading.current_thread().name, "\b: Argument:", arg)
# 			time.sleep(0.5)
#
#
# tasksQueue = queue.Queue()
#
# for i in range(5):
# 	tuple12 = threading.Thread(target = worker, name = chr(i + ord("A")))
# 	tuple12.start()
#
# print("Enqueueing...")
# for i in range(50):
# 	tasksQueue.put(i)
# print("Finished.")
#
# print("Main Thread Sleeping...")
# time.sleep(5)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # FAQ.
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/randEight.txt", "w+b") as file14:
# 	randomBytes = random.randbytes(8)
# 	print("randomBytes:", randomBytes)
# 	file14.write(randomBytes)
# 	short1, short2, list100 = struct.unpack("<hhl", randomBytes)
# 	print("short1:", short1, "short2:", short2, "list100:", list100)
# 	long2 = -2147483648
# 	long3 = -1
# 	long4 = 1
# 	long5 = 2147483647
# 	bytes1 = struct.pack("<llll", long2, long3, long4, long5)
# 	file14.write(bytes1)
# 	file14.seek(-16, os.SEEK_CUR)
# 	bytes12 = file14.read(16)
# 	print("bytes12:", bytes12)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# circularImportExample = 10
# x = 1
# y = 2
# print("main: x:", x)
# print("main: y:", y)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(sys.get_int_max_str_digits())
# sys.set_int_max_str_digits(100000)
# print(sys.get_int_max_str_digits())
# print(len(str(2 ** 100000)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string27 = "shrubbery"
# list31 = list(string27)
# list31[1] = "c"
# list31 = "".join(list31)
# print(list31)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# byteArray1 = bytearray(b"spam")
# byteArray1.extend(b"eggs")
# print(byteArray1)
# print(byteArray1.decode())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string28 = "spam"
# print(string28.find("pa"))
# print(string28.replace("pa", "XYZ"))
# print(string28)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string29 = "aaa,bbb,ccccc,dd"
# print(string29.split(","))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string30 = "spam"
# print(string30 + "NI!")
# print(string30.__add__("NI!"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(help(str.replace))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("sp\xc4\u00c4\U000000c4m")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# match = re.match("Hello[ \t]*(.*)world", "Hello		Python world")
# print(match.group(1))
#
# match = re.match("[/:](.*)[/:](.*)[/:](.*)", "/usr/home:lumberjack")
# match = re.match("(.*)[/:](.*)[/:](.*)[/:](.*)", "lumberjack:/home/user")
#
# print(match.groups())
#
# print(re.split("[/:]", "/usr/home/lumberjack"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list33 = [1, 2]
# print(list33 + [3])
# print(list33 * 2)
# list33.append("WOMAN")
# print(list33)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# secondColumn = [r[1] + 1 for r in matrix if r[1] % 2 == 0]
# print(secondColumn)
# diagonal = [matrix[e][e] for e in [0, 1, 2]]
# print(diagonal)
# doubledLetters = [c * 2 for c in "WOMAN"]
# print(doubledLetters)
# list33 = list(range(30))
# print(list33)
# list33 = list(range(-6, 7, 2))
# print(list33)
# list33 = [[e ** 2, e ** 3] for e in list(range(4)) if e % 2 == 0]
# print(list33)
# generator1 = ([e ** 2, e ** 3] for e in list(range(4)) if e % 2 == 0)
# print(next(generator1))
# print(next(generator1))
# print("list map sum:" + str(list(map(sum, matrix))))
# print(list(map(sum, matrix)))
# print(matrix)
# print({sum(r) for r in matrix})
# print({i: sum(matrix[i]) for i in range(3)})
# print([ord(c) for c in "DAMSELINDISTRESS"])
# print({ord(c) for c in "DAMSEL"})
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict5 = {"key1": "value1", "key2": "value2", "key3": "value3"}
# print(dict5["key1"] + str(1))
# dict5["key3"] = "value3"
#
# print(dict5["key3"])
# dict6 = dict(key4 = "value4")
# print(dict6["key4"])
# dict7 = dict(zip(["name", "age", "salary"], ["Woman", 27, 1000000]))
# print(dict7)
# print(dict7.get("name2", "Punit"))
# print(dict7["name"] if "name2" in dict7 else "Punit")
# keys1 = list(dict7.keys())
# print(keys1)
# for k in sorted(dict7):
# 	print(dict7[k])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# Class7 = {"a": 1, "b": 2, "c": 3}
# value = Class7.get("x", 0)
# print(value)
# value = Class7["x"] if "x" in Class7 else 0
# print(value)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(list(map(ord, "spam")))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print([1, 2] + list("34"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(list(map(abs, [-1, -2, 0, 1, 2])))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list34 = ["a", "b", "c", "d", "e", "f", "g", "h"]
# print("list34:", list34)
# list34[2 : 5] = list34[3 : 6]  # Overlapping works fine because first fetching is done, then deletion.
# print("list34:", list34)
# list34[1 : 1] = ["x", "y"]
# print("list34:", list34)
# list35 = [1]
# list35[: 0] = [2, 3, 4]
# print("list35:", list35)
# list35[len(list35):] = [5, 6, 7]
# print("list35:", list35)
#
# list36 = ["a", "b", "c", "d", "e", "f", "g", "h"]
# print("list36:", list36)
# list36[len(list36):] = ["i"]  # Is same as:
# print("list36:", list36)
# list36.append("i")  # And:
# print("list36:", list36)
# list36.insert(len(list36), "i")
# print("list36:", list36)
#
# list36[: 0] = ["0"]  # Prepending.  Same as:
# print("list36:", list36)
# list36.insert(0, "0")
# print("list36:", list36)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list37 = ["abc", "ABD", "aBe"]
# list37.sort(key = str.lower)
# print("list37:", list37)
#
# list38 = ["abc", "ABD", "aBe"]
# list38.sort(key = str.lower, reverse = True)
# print("list38:", list38)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list39 = ["spam", "eggs", "ham", "toast"]
# del list39[1 :]  # Delete entire section.  Same as:
# print("list39:", list39)
# list40 = ["spam", "eggs", "ham", "toast"]
# list40[1 :] = []
# print("list40:", list40)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list41 = ["Already", "got", "one"]
# list41[0] = []  # Does not delete.  Instead, puts a reference to an empty list at that index.
# print("list41:", list41)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict8 = dict([("name", "Bob"), ("age", 40)])
# dict9 = dict.fromkeys(["name", "age"])
# print("dict8.items():", dict8.items())  # All key, value tuples.
# print('"Name" in dict8:', "Name" in dict8)
# print("dict8.update(dict8):", dict8.update(dict8))  # Merge by keys.
# print('dict8.get("name", "Punit"):', dict8.get("name", "Punit"))  # Fetch by key, if absent default (or "None").
# print('dict8.pop("age", "29"):', dict8.pop("age", "29"))  # Remove by key, same as above.
# print('dict8.setdefault("name", "Punit"):', dict8.setdefault("name", "Punit"))  # Fetch by key, if absent: set default, or "None".
# print("dict8.popitem():", dict8.popitem())
# print("dict8:", dict8)
# print("dict8:", dict8)
# dict10 = {"name": "Bob", "age": 40}
# del dict10["name"]  # Delete entries by key.
# print("list(dict10.keys():", list(dict10.keys()))  # Dictionary views.
# print("dict10.keys() & dict8.keys():", dict10.keys() & dict8.keys())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# table4 = {"Holy Grail": "1975", "Life of Brian": "1979", "The Meaning of Life": "1983"}
# print(list(table4.items()))
# print([title for (title, year) in table4.items() if year == "1975"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# matrix = {(2, 3, 4): 88, (7, 8, 9): 99}
# x = 2
# y = 3
# z = 4
# print("matrix[(x, y, z)]:", matrix[(x, y, z)])
# origin = (7, 8, 9)
# print("matrix[origin]:", matrix[origin])
# print("matrix:", matrix)
#
# try:
# 	print(matrix[(2, 3, 6)])
# except KeyError:
# 	print(0)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print('list(zip(["a", "b", "c"], [1, 2, 3])):', list(zip(["a", "b", "c"], [1, 2, 3])))
# dict11 = {k: v for (k, v) in zip(["a", "b", "c"], [1, 2, 3])}
# print("dict11:", dict11)
# keys2 = dict11.keys()
# print('keys2 | {"x" : 4}:', keys2 | {"x": 4})
# tuple13 = dict11.values()
# try:
# 	print('tuple13 | {"x" : 4}:', tuple13 | {"x": 4})
# except TypeError:
# 	print("Value error.")
# try:
# 	print('tuple13 | {"x" : 4}.values():', tuple13 | {"x": 4}.values())
# except TypeError:
# 	print("Value error.")
# print('keys2 & {"c": 3}:', keys2 & {"c": 3})
# print("dict11.items() | dict11.keys():", dict11.items() | dict11.keys())
# print('dict(dict11.items() | {("d", 4), ("e", 5)}):', dict(dict11.items() | {("d", 4), ("e", 5)}))
# print('dict({("a", 1), ("b", 2)}):', dict({("a", 1), ("b", 2)}))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict12 = {"a": 1, "b": 2}
# dict13 = {"a": 1, "c": 3}
# print("sorted(dict12.items()) < sorted(dict13.items()):", sorted(dict12.items()) < sorted(dict13.items()))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dbFile = dbm.open("/home/punit/src/_not_mine/PythonTestBed/var/in.dbm", "c")
# dbFile["key"] = "Any Random String"
# value5 = dbFile["key"]
# print("value5:", value5)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# shelf = shelve.open("/home/punit/src/_not_mine/PythonTestBed/var/in.shelve", "c")
# shelf["key"] = {"a": 1, "b": 2, "c": 3}
# value6 = shelf["key"]
# print("value6:", value6)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(dict.fromkeys("a", 0))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# x = 1
# y = 2
# try:
# 	assert x > y, "x is smaller than y"
# except AssertionError as ex:
# 	print(ex)
# sys.exit()
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# [a, b, c] = (1, 2, 3)
# print("a:", a)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# a, b, c = range(3)
# print(a, b, c)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list41 = [3, 1, 4, 1, 5, 9]
# while list41:
# 	head, list41 = list41[0], list41[1 :]
# 	print("head:", head)
# 	print("list41:", list41)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# a, *b, c = "spam"
# print("a:", a, "b:", b, "c:", c)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list42 = [3, 1, 4, 1, 5, 9]
#
# while list42:
# 	head, *list42 = list42
# 	print("head:", head)
# 	print("list42:", list42)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list43 = ["a", "b", "c", "d"]
# a, b, c, *d = list43
# print("a:", a, "b:", b, "c:", c, "d:", d)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list44 = ["a", "b", "c", "d"]
# a, b, c, d, *e = list44
# print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list45 = ["a", "b", "c", "d"]
# a, b, *c, d, e = list45
# print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list46 = []
# list46 += "spam"  # Works.
# print("list46:", list46)
# list46.append("spam")  # Works.
# print("list46:", list46)
# list46.extend("spam")  # Works.
# print("list46:", list46)
# try:
# 	list46 = list46 + "spam"  # Doesn't.
# except TypeError as ex:
# 	print("TypeError:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("a", file = sys.stderr)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out2.txt", "w") as file17:
# 	print("A", file = file17)
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out2.txt") as file18:
# 	print("out2.txt:", file18.read())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# number36 = 0x16_FF_9A
# string31 = "\u1f9e"
# tuple14 = number36, string31
# list48 = [number36, string31]
# set4 = {number36, string31}
# dict14 = {number36: string31}
# print(number36, string31, tuple14, list48, set4, dict14, sep = "")  # Is same as:
# sys.stdout.write(str(number36) + str(string31) + str(tuple14) + str(list48) + str(set4) + str(dict14))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# stream1 = sys.stdout
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out3.txt", "a") as sys.stdout:
# 	print("B")
# sys.stdout = stream1
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# stream2 = sys.stdout
# print("A")
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out4.txt", "a") as sys.stdout:
# 	print("B")
# 	sys.stdout = stream2
# 	print("C")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string32 = """
# A
# B	# Comment not ignored.
# C
# """
# print("string32:", string32, "len(string32):", len(string32))
# string32 = "ABC"
# print("string32:", string32)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(1 and 1)
# print("a" and 0)
# print("a" and "0")
# print("a" or "0")
# print(("a", "1") and ("", 0))
# print(("a", "1") and ("b", 1))
# print(("a", "1") or ("b", 1))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# for it1 in (False, True):
# 	for it2 in (False, True):
# 		for it3 in (False, True):
# 			print("it1:", it1, "it2:", it2, "it3:", it3)
# 			bool100 = (it1 and it2) or it3
# 			print("bool100:", bool100)
# 			var100 = it2 if it1 else it3  # Always same as:
# 			print("var100:", var100)
# 			var101 = [it3, it2][bool(it1)]  # This.
# 			print("var101:", var101)
# 			bool101 = it1 or it2 or it3 or None
# 			print("bool101:", bool101)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list47 = ["a", 0, "b", [], "c", {}]
# print(list(filter(bool, list47)))
# print(any(list47), all(list47))
# print(list(filter(str, list47)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# table5 = [("Bob", 120129, "DB Admin", "Calicut"), ("Alice", 108420, "Python Expert", "Kozhikode"), ("Carl", 109481, "AI Engineer", "Trivandrum")]
# for _, iden, _, _ in table5:
# 	print("ID:", iden)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# for (a, b), c in [([1, 2], 3), ["XY", 4]]:
# 	print("a:", a, "b:", b, "c:", c)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list49 = ["aaa", 111, (4, 5), 2.01]
# list50 = [(4, 5), 3.14]
#
# for e1 in list50:
# 	for e2 in list49:
# 		if e1 == e2:
# 			print(e1, "was found")
# 			break
# 	else:
# 		print(e1, "not found!")
#
# # This is better because Python is doing all the work.
#
# for e in list50:
# 	if e in list49:
# 		print(e, "was found")
# 	else:
# 		print(e, "not found!")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# output = os.popen("/usr/bin/ls")
# print("readline:", output.readline())
# output = os.popen("/usr/bin/ls")
# print("read(5):", output.read(5))
# output = os.popen("/usr/bin/ls")
# print("readlines()[0]:", output.readlines()[0])
# print("read()[:5]:", os.popen("/usr/bin/ls").read()[: 5])
#
# print("Line iteration in for loop:")
# for l in os.popen("/usr/bin/ls"):
# 	print(l.rstrip())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in4.txt") as file19:
# 	print(file19 is iter(file19) and iter(file19) is file19.__iter__())
# 	print(file19.__next__())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list51 = ["A", "B", "C", "Class3"]
# file20 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# list51.extend(file20)
# print("list51:", list51)
# file20 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# list51.append(file20)
# print("list51:", list51)
# file20 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in5.txt")
# list51.append(list(file20))
# print("list51:", list51)
# print("list51[8]:", list51[8])
# print("list(list51[8]):", list(list51[8]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# tuple15 = (1, 2)
# tuple16 = (3, 4)
# print("list(zip(tuple15, tuple16)):", list(zip(tuple15, tuple16)))
# tuple17, tuple18 = zip(*zip(tuple15, tuple16))
# print("tuple17:", tuple17, "tuple18:", tuple18)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# map1 = map(abs, [-1, 0, 1])
# print("map1:", map1)
# iterator2 = iter(map1)
# print("type(map1):", type(map1))
# print("type(iterator2):", type(iterator2))
#
# print("next(map1):", next(map1))
# print("next(iterator2):", next(iterator2))
#
# for i in map1:
# 	print("i:", i)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(len(dir(sys)))
# print(len([s for s in dir(sys) if not s.startswith("_")]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(docstrings.__doc__)
# print(docstrings.square.__doc__)
# print(docstrings.Employee.__doc__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# help("sys")  # If not imported.
# help("email.message")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("help(docstrings.square):")
# help(docstrings.square)
# print("help(docstrings.Employee):")
# help(docstrings.Employee)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# var101 = "old"
#
#
# def changer() -> None:
# 	global var101
# 	var101 = "new"
#
#
# def outer() -> None:
# 	var101 = "old"
#
# 	def changer() -> None:
# 		nonlocal var101
# 		var101 = "new"
#
#
# print("var101:", var101)
# changer()
# print("var101:", var101)
#
#
# def squares(var101: int) -> int:
# 	for i in range(var101):
# 		yield i ** 2
#
#
# print(list(squares(5)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# tuple19 = 1, 2
# tuple20 = 2, 3, 4
# print(tuple19 + tuple20)
# print(tuple19 * 3)
# tuple21 = "spam"
# # print([c ** 2 for c in tuple21])	# Can't apply the exponentiation operator on a string.
# tuple22 = "item1", 2, 3.0, ["four1", "four2"], "item1"
# print("tuple22[1]:", tuple22[1])
# print("tuple22.index(2):", tuple22.index(2))
# print("tuple22.index(3, 1):", tuple22.index(3, 1))
# print('tuple22.count("item1"):', tuple22.count("item1"))
# print("tuple22[3]:", tuple22[3])
# namedTuple3 = collections.namedtuple("Employee", ["name", "designation"])
# print(namedTuple3)
# print(namedTuple3["Employee"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# tuple23 = (1, [2, 3], 4)
# # tuple23[1] = [2]
# tuple23[1][0] = 20
# print(tuple23)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# namedTuple4 = collections.namedtuple("namedTuple4", ["name", "age", "jobs"])  # Create the class.
# bob = namedTuple4("Bob", age = 30, jobs = ["dev", "mgr"])
# print(bob)
# print(bob[0], bob[2])
# print(bob.name, bob.jobs)
# dict15 = bob._asdict()
# print(dict15)
# print(dict15["name"])
# print(dict15["age"])
# name1, age1, jobs1 = bob
# print("jobs1:", jobs1)
#
#
# class NamedTuple1(typing.NamedTuple):
# 	name: str
# 	age: int
# 	jobs: list
#
#
# namedTuple5 = NamedTuple1("arya", "30", ["dev", "mgr"])
# for it in namedTuple5:  # Iteration context.
# 	print(it)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.bin", "rb") as file21:
# 	bytes8 = file21.read()
# 	print(bytes8)
# 	print("bytes8[4:7]:", bytes8[4 : 7].decode())
# 	print("str(bytes8):", str(bytes8, "utf-8"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# bytes5 = struct.pack(">i9sh", 7, b"MANNA DEY", 8)  # Create bytes5 binary data.
# print(bytes5)
# file22 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/bytestring.bin", "wb")  # Open binary output file.
# file22.write(bytes5)
# file22.close()
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/bytestring.bin", "rb") as file23:
# 	bytes9 = file23.read()
# 	print(bytes9)
# 	print(bytes9[4 : 8])
# 	print(len(bytes9))
# 	print(list(bytes9))
# 	print("Read:" + bytes9.decode())
# 	print(struct.unpack(">i9sh", bytes9))  # Unpack to objects again.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string33 = "sp\xc4m"
# print(string33)
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/unicode_data.txt", "w", encoding = "utf-8") as file24:
# 	file24.write(string33)
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/unicode_data.txt", encoding = "utf-8") as file25:
# 	string34 = file25.read()
# 	print(string34)
# 	print(len(string34))
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/unicode_data.txt", "rb") as file26:
# 	bytes7 = file26.read()
# 	print(bytes7)
# 	print(len(bytes7))
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/utf-16-le.txt", "rb") as file26:
# 	string44 = file26.read()
# 	print(string44)
# 	print(len(string44))
#
# print('string34.encode("utf-8"):', string34.encode("utf-8"))
# print('bytes7.decode("utf-8"):', bytes7.decode("utf-8"))
# print('string34.encode("utf-16"):', string34.encode("utf-16"))
# print('string44.decode("utf-16"):', string44.decode("utf-16"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# set5 = set("spam")
# set6 = {"h", "a", "m"}
# print(set5, set6)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# set7 = set("woman")
# set8 = set("man")
# print(set7)
# print(set7 & set8)
# print(set7 - set8)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# {i ** 2 for i in [1, 2, 3, 4]}  # Set comprehension.
# print(list(set("woman")))
#
# print(set("spam") == set("asmp"))  # Order-neutral equality test.
# string36 = "p"
# print(string36 in set("spam"), string36 in "spam", "ham" in ["eggs", "spam", "ham"])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# decimal1 = decimal.Decimal("3.141")
# print(decimal1 + 1)
#
# decimal.getcontext().prec = 2
# print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# fraction1 = fractions.Fraction(1, 4)
# print(fraction1 + 1)
# print(fraction1 + fractions.Fraction(1, 2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(bool("spam"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# var102 = None
# print(var102)
# list52 = [None] * 100
# print(list52)
# print(type(list52))
# print(type(type(list52)))
# if type(list52) == type([]):  # Type testing.
# 	print("yes")
# print(type("a"))
# print(type(str))
# list53 = []
# if type(list53) is list:
# 	print("type function output matches type name (as keyword)")
# if isinstance(list53, list):  # OO test.
# 	print("isInstance working")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# class Lovers:
#
# 	def __init__(self, name1: str, salary1: float) -> None:  # Initialize when created.
# 		self.name1 = name1
# 		self.salary1 = salary1
#
# 	def giveHike(self, percent1: float) -> None:
# 		self.salary1 += self.salary1 * percent1 / 100
#
# 	def getLastName(self) -> str:
# 		return self.name1.split()[-1]
#
#
# woman = Lovers("Woman", 1000)
# man = Lovers("Man", 1000)
# print(man.getLastName())
# print(woman.giveHike(20))
# print(man.salary1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(int(3.1415))
# print(float(3))  # Converts to float.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(repr("spam"))
# print(str("spam"))
# print(str(b"xy", "utf8"))  # Alternative to "bytes.decode" method.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# number31 = 2
# number32 = 4
# number33 = 6
#
# print(number31 < number32 < number33)  # Range test.
# print(number31 < number32 and number32 < number33)
# print(number31 < number32 > number33)
# print(number31 < number32 and number32 > number33)
# number34 = 2
# number35 = 3.0
# number36 = 4
# print(1 < number34 < number35 < number36)
# print(1 > number34 > number35 > number36)
# print(1 == number34 < number35)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# number37 = 3.3
# print(number37 == 1.1 + 2.2)
# print(1.1 + 2.2)
# print(int(1.1 + 2.2) == int(3.3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(1j * 1j)
# print(2 + 1j * 3)
# print((2 + 1j) * 3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(oct(64), hex(64), bin(64))
# print(64, 0o100, 0x40, 0b1000000)
# print(int("64"), int("100", 8), int("40", 16), int("1000000", 2))
# print(int("0x40", 16), int("0b10000000", 2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(f"{64:0}, {64:o}, {64:X}, {64:x}, {64:b}")  # Returns digits not strings.
# print("%o, %x, %x, %X" % (64, 64, 255, 255))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# number38 = 99
# print(bin(number38), number38.bit_length(), len(bin(number38)) - 2)
# print(bin(256), (256).bit_length(), len(bin(256)) - 2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(math.pi, math.e)
# print(math.sin(2 * math.pi / 180))
# print(math.sqrt(144), math.sqrt(2))
# print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
# print(abs(-42.0), sum((1, 2, 3, 4)))  # Summation.
# print(min(3, 1, 2, 4), max(3, 1, 2, 4))
# print(math.floor(2.567), math.floor(-2.567))
# print(math.trunc(2.567), math.trunc(-2.567))
# print(round(2.567), round(2.467), round(2.567, 2))
# print(f"{2.567:.1f}", f"{2.567:.2f}")
# print((1 / 3.0), round(1 / 3.0, 2), ("%.2f" % (1 / 3.0)))
# print(math.sqrt(144))
# print(144 ** 0.5)
# print(pow(144, 0.5))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(hex(15))
# print(bin(15))
# print(int("0b1111", 2))
# complex1 = complex(2, 3)
# print(complex1)
# number39 = 25.0
# print(number39.as_integer_ratio())
# if number39.is_integer():
# 	print("yes integer")
# number40 = 5
# print(number40.bit_length())
# print("OK" if False else True)
# print("OK" if False else "NOK")
# print("not in" if "s" not in "spam" else "in")
# list54 = list55 = [1]
# print("same" if list54 is not list55 else "different")
# print("abcdefghi"[1 :-1 : 2])
# string37 = "abcdefghi"
# string38 = string37[slice(1, 2, -1)]
# print(string38)
# dict16 = {"key3": "value1", "key2": "value2", "key1": "value3"}
# print(sorted(dict16.items()))
# print(int(3.14), int(3.54), int(3.84))
# print(float(3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string39 = "print(oct(8))"
# eval(string39)
# # ast.literal_eval(myCode)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("{16:o}, {16:x}, {16:b}")
# print(f"{15:o}, {15:x}, {15:X}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(random.randint(1, 10))
# print(random.randint(1, 10))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# suits = ["hearts", "clubs", "diamonds", "spades"]
# random.shuffle(suits)
# print(suits)
# random.shuffle(suits)
# print(suits)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(0.1 + 0.1 + 0.1 - 0.3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(decimal.Decimal.from_float(1.25))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(decimal.Decimal("0.1") + decimal.Decimal("0.1") + decimal.Decimal("0.1") - decimal.Decimal("0.3"))
# print(decimal.Decimal("0.1") + decimal.Decimal("0.10") + decimal.Decimal("0.10") - decimal.Decimal("0.30"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(decimal.Decimal(1) / decimal.Decimal(7))  # Default: 28 digits.
# decimal.getcontext().prec = 4
# print(decimal.Decimal(1) / decimal.Decimal(7))
# print(decimal.Decimal(0.1) + decimal.Decimal("0.1") + decimal.Decimal("0.1") - decimal.Decimal("0.3"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with decimal.localcontext() as ctx:
# 	ctx.prec = 2
# 	print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))
# print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# fraction2 = fractions.Fraction(1, 3)
# fraction3 = fractions.Fraction(4, 6)
#
# print(fraction2 + fraction3)
# print(fraction2 - fraction3)
# print(fraction2 * fraction3)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(fractions.Fraction(".25"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(fractions.Fraction("0.25"))
# number41 = 0.25
# print(fractions.Fraction(*number41.as_integer_ratio()))
# print(fractions.Fraction(*(0.25).as_integer_ratio()))
# fraction4 = fractions.Fraction(4 / 3)
# print(fraction4.limit_denominator(3))
#
# print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))
#
# print((2.5).as_integer_ratio())
#
# number42 = 2.5
# fraction5 = fractions.Fraction(*number42.as_integer_ratio())  # "*" converts a tuple in to individual arguments.
# print(fraction5)
# print(float(fraction5))
# print(fractions.Fraction.from_float(1.75))
# print(fractions.Fraction(*(1.75).as_integer_ratio()))
# print(fraction5 + 2)  # "fractions.Fraction" + "int" -> "fractions.Fraction"
# print(fraction5 + 2.0)  # "fractions.Fraction" + "float" -> "float"
# print(fraction5 + fractions.Fraction(4, 3))  # "fractions.Fraction" + "fractions.Fraction" -> "fractions.Fraction"
# fraction6 = fraction5 + fractions.Fraction(*(4.0 / 3).as_integer_ratio())
# print(fraction6)
# print(fraction6.limit_denominator(10))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# set9 = set("abcde")
# set10 = set("bdxyz")
# set11 = set9.intersection(set10)  # Same as "x & y".
# print(set11)
# print(set11.add("SPAM"))
# print(set11.update(set(["X", "Y"])))  # Merge, i.e., in-place union.
# print(set11.remove("b"))
#
# for m in set("abc"):
# 	print(m * 3)
#
# set12 = {1, 2, 3}
# print(set12 | {3, 4})
# try:
# 	print(set12 | [3, 4])
# except TypeError as ex:
# 	print(ex)
#
# print(set12.union([3, 4]))
# print(set12.issubset(range(-5, 5)))
#
# set13 = {1, 2, 3, 4}
# print(set13 - {1, 2, 3, 4})
# print(type({}))
# set13 = set()  # Initialize an empty set.
# print(set13.add(1.23))
# print({1, 2, 3}.union([3, 4]))
#
# print(set(dir(bytes)) - set(dir(bytearray)))
# print(set(dir(bytearray)) - set(dir(bytes)))
#
# list56, list57 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
# print(list56 == list57)  # Order matters in sequence.
# print(set(list56) == set(list57))  # It doesn't in sets.
# print(sorted(list56) == sorted(list57))
#
# engineers = {"bob", "sue", "ann", "vic"}
# managers = {"tom", "sue"}
#
# print(engineers > managers)
# print((managers | engineers) - (managers ^ engineers))  # Intersection.
#
# print(type(True))
# var20 = 1
# print(isinstance(var20, int))
# print(var20 == True)
# print(True is 1)
# print(True + 4)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# set14 = {1, 2, 3}
# print(set14)
#
# set15 = set14.copy()
# print(set15)
#
# set16 = set(set15)
# print(set16)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list58 = [1, 2, (1, 2, [1, 2, (1, 2, [1, 2])])]
#
# print(list58)
# list59 = copy.copy(list58)
#
# print(list59)
# list60 = copy.deepcopy(list58)
#
# print(list60)
# list61 = list58.copy()
#
# print(list61)
# print(len(list61))
#
# list62 = copy.copy(list58)
# print(len(list62))
#
# list63 = copy.deepcopy(list58)
# print(len(list63))
#
# list64 = list58.copy()
# print(len(list64))
#
# print(type(list58[2]))
# print(type(list58[2][2]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("knight's", 'knight"s')
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# path = r"C:\new\text.dat"
# print(path)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(hex(255))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict17 = {"spam": 2, "ham": 1, "eggs": 3}
# print(list(dict17.values()))
# print(list(dict17.items()))
# print(dict17.get("spam"))
# print(dict17.get("toast"))
# print(dict17.get("toast", 88))
#
# # LP
#
# file27 = pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt", encoding = "utf-8")
# print(len(file27.read()))
#
# for l in pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt"):
# 	print(l.rstrip())
#
# 	words = l.split()
# 	print(words)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in3.txt") as file28:
# 	line = file28.readline()
# 	print("line:", line)
# 	listLines = line.split("$")
# 	print("listLines:", listLines)
# 	object9 = ast.literal_eval(listLines[0])
# 	print("object9:", object9)
# 	object10 = ast.literal_eval(listLines[1])
# 	print("object10:", object10)
# 	listObjects = [ast.literal_eval(l) for l in listLines]
# 	print("objectsRead:", listObjects)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict18 = {"a": 1, "0x29cc": "⧌", "0x29c9": "⧉", "0x29c6": "⧆", "0x29c1": "⧁"}
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.pkl", "wb") as file29:
# 	pickle.dump(dict18, file29)
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.pkl", "rb") as file30:
# 	dictUnpickled = pickle.load(file30)
# 	print("dictUnpickled:", dictUnpickled)
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.pkl", "rb") as file31:
# 	print("Pickled Objects:", file31.read())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.csv") as file32:
# 	cSVFile = csv.reader(file32)
# 	for l in cSVFile:
# 		print(l)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.bin", "wb") as file33:
# 	bytes2 = struct.pack(">i4sh", -2147483647, b"pyth", -32768)
# 	print("bytes2:", bytes2)
# 	print("file33.write(bytes2):", file33.write(bytes2))
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out.bin", "rb") as file34:
# 	bytes3 = file34.read()
# 	print("bytes3:", bytes3)
# 	bytes4 = struct.unpack(">i4sh", bytes3)
# 	print("bytes4:", bytes4)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list65 = [0, 1]
# list66 = [-1, list1, 2]
# dict19 = {"a": 1, "reference": list66, "b": 2}
# print("list165:", list65)
# print("list66:", list66)
# print("dict19:", dict19)
# list65.append(0.5)
# print("list65:", list65)
# print("list66:", list66)
# print("dict19:", dict19)
#
# tuple25 = 0, 1
# list67 = [0, tuple25, 1]
# dict19 = {"a": 1, "reference": list67, "b": 2}
# print("tuple25:", tuple25)
# print("list67:", list67)
# print("dict19:", dict19)
# tuple26 = 0, 0.5, 1
# print("tuple26:", tuple26)
# print("list67:", list67)
# print("dict19:", dict19)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(bool(0.0))
# print(bool({}))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(type([1]) == type([]))
# print(list is type([]))
# print(isinstance([1], list))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(type(lambda arg100: arg100 * 2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list68 = [0, 1, 2]
# list69 = list68 * 4
# print("list69:", list69)
# list70 = [list69] * 4
# print("list70:", list70)
# list70[1] = 0.5
# print("list68:", list68)
# print("list69:", list69)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list71 = [0, 1, 2]
# list72 = [list71] * 4
# list73 = [list(list72)] * 4
# print("list71:", list71)
# print("list72:", list72)
# print("list73:", list73)
# list73[1] = 0.5
# print("list73:", list73)
# print("list72:", list72)
# print("list71:", list71)
# list73[2][1] = 0.25
# print("list73:", list73)
# list74 = [list(list73) for _ in range(4)]
# print("list74:", list74)
# list74[1] = 0.0625
# list74[2][1] = 0.125
# print("list74:", list74)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list75 = ["grail"]
# list75.append(list75)
# print(list75)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list76 = [0, 0xA, 0b10, "d"]
# print("list76:", list76)
# print("list76[3:1]:", list76[3 : 1])
# list76[3 : 1] = "?"
# print("list76:", list76)
# print("list76[10:-10]:", list76[10 :-10])
# list76[10 :] = "V"
# print("list76:", list76)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# dict20 = {}
# dict20[1] = "a"
# print("dict20:", dict20)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string40 = "spam"
# print("string40[0][0][0][0][0]:", string40[0][0][0][0][0])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string41 = ["s", "p", "a", "m"]
# print("string41[0][0][0][0][0]:", string41[0][0][0][0][0])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# string42 = "spam"
# print("string42:", string42)
# string43 = string42[0 : 1] + "list76" + string42[2 : 4]
# print("string43:", string43)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(zip is builtins.zip)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# # print(builtins is __builtin__)
# print(builtins is __builtins__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# try:
# 	print("var103:", var103)
# except NameError as ex:
# 	print("NameError:", ex)
#
#
# def function28() -> None:
# 	global var104
# 	var104 = 10
#
#
# function28()
# print("var104:", var104)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("main: module1.var105:", module1.var105)
# module1.var105 = 1
# print("main: module1.var105:", module1.var105)
#
# print("main: module1.var105:", module1.var105)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# var106 = 0
#
#
# def local() -> None:
# 	var106 = 1
# 	print("local: var106:", var106)
#
#
# def global1() -> None:
# 	global var106
# 	print("global1: var106:", var106)
# 	var106 = 2
# 	print("global1: var106:", var106)
#
#
# def global2() -> None:
# 	var106 = 3
#
# 	print("global2: __main__.var106:", __main__.var106)
# 	__main__.var106 = 4
# 	print("global2: __main__.var106:", __main__.var106)
#
#
# def global3() -> None:
# 	var106 = 5
#
# 	globals = sys.modules["__main__"]
# 	print("global3: globals.var106:", globals.var106)
# 	globals.var106 = 6
# 	print("global3: globals.var106:", globals.var106)
#
#
# def test() -> None:
# 	print("test: var106:", var106)
# 	local()
# 	global1()
# 	global2()
# 	global3()
# 	print("test: var106:", var106)
#
#
# test()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# var140 = 0
#
#
# def function29() -> None:
# 	var140 = 1
# 	print("function29: var140:", var140)
#
# 	def function30() -> None:
# 		print("function30: var140:", var140)
#
# 	print("function30: var140:", var140)
# 	function30()
# 	print("function30: var140:", var140)
#
#
# print("main: var140:", var140)
# function29()
# print("main: var140:", var140)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function32() -> None:
# 	var109 = 0
#
# 	def function33() -> None:
# 		print("var109:", var109)
#
# 	return function33
#
#
# action = function32()
# action()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def returnClosure(base: int) -> callable:
#
# 	def closure(exponent: int) -> callable:
# 		return base ** exponent
#
# 	base = 3  # Return me powers of 3 instead.
#
# 	return closure
#
#
# myClosure = returnClosure(2)  # Return me powers of 2.
# print("myClosure:", myClosure)
# # myClosure: <function returnClosure.<locals>.closure at 0x7fb8391e8430>
#
# threePoweredThree = myClosure(3)  # A different power of 3 (cubed).
# print("threePoweredThree:", threePoweredThree)
# # threePoweredThree: 9
#
# threePoweredFour = myClosure(4)  # Another power of 3.
# print("threePoweredFour:", threePoweredFour)
# # threePoweredFour: 81
#
# threePoweredFive = myClosure(5)  # A different name and a different object.
# print("threePoweredFive:", threePoweredFive)
# # 243
#
# print("returnClosure(2) is returnClosure(3):", returnClosure(2) is returnClosure(3))
# print("returnClosure(2) is returnClosure(2):", returnClosure(2) is returnClosure(2))
# myClosure1 = returnClosure(3)
# myClosure2 = returnClosure(4)
# print("myClosure1 is myClosure2:", myClosure1 is myClosure2)
# print("myClosure1(2) is myClosure2(2):", myClosure1(2) is myClosure2(2))
# print("myClosure1(3) is myClosure2(3):", myClosure1(3) is myClosure2(3))
# print("myClosure1(4) is myClosure2(4):", myClosure1(4) is myClosure2(4))
# print("myClosure1(5) is myClosure2(5):", myClosure1(5) is myClosure2(5))
# print("myClosure1(4) is myClosure2(5):", myClosure1(4) is myClosure2(5))
# print("myClosure1(6) is myClosure2(6):", myClosure1(6) is myClosure2(6))
# print("myClosure1(7) is myClosure2(7):", myClosure1(7) is myClosure2(7))
# print("myClosure1(8) is myClosure2(8):", myClosure1(8) is myClosure2(8))
# print("myClosure1(9) is myClosure2(9):", myClosure1(9) is myClosure2(9))
# print("myClosure1(6):", myClosure1(6))
# print("myClosure2(6):", myClosure2(6))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def returnLambda(base: float) -> callable:
# 	return lambda exponent: base ** exponent
#
#
# lambda100 = returnLambda(3)
# print("lambda100:", lambda100)
#
# threePoweredThree = lambda100(3)
# print("threePoweredThree:", threePoweredThree)
#
# threePoweredFour = lambda100(4)
# print("threePoweredFour:", threePoweredFour)
#
# threePoweredFive = lambda100(5)
# print("threePoweredFive:", threePoweredFive)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function34() -> None:
# 	var107 = 0
# 	var108 = 10
#
# 	def function35(var107: any = var107) -> None:
# 		var107 += 1
# 		nonlocal var108
# 		var108 += 1
# 		print("function35: var107:", var107)
# 		print("function35: var108:", var108)
#
# 	function35()
# 	function35()
#
#
# function34()
# function34()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function34() -> None:
# 	var109 = 0
#
# 	function35(var109)
# 	function35(var109)
#
#
# def function35(var109: int) -> None:
# 	var109 += 1
# 	print("function35: var109:", var109)
#
#
# function34()
# function34()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function36() -> callable:
# 	base = 2
#
# 	return lambda exponent: base ** exponent
#
#
# lambda101 = function36()
# print("lambda101(3):", lambda101(3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("h")
# # nonlocal a
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def tester(start: int) -> callable:
# 	state = start
#
# 	def nested(label: str) -> None:
# 		print(label, start)
#
# 	return nested
#
#
# function37 = tester(0)
# print(function37("spam"))
# print(function37("ham"))
# function38 = tester(1)
# print(function38("spam"))
# print(function37 is function38)
# print(tester(0) is tester(0))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def tester(start: int) -> callable:
# 	state = start
#
# 	def nested(label: str) -> None:
# 		nonlocal state
#
# 		print(label, state)
# 		state += 1
#
# 	return nested
#
#
# function37 = tester(0)
# print(function37("spam"))
# print(function37("ham"))
# print(function37("eggs"))
# function38 = tester(42)
# print(function38("spam"))
# print(function38("eggs"))
# print(function37("bacon"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def demonstrateFunctionAttributes(arg110: any) -> callable:
#
# 	def nestedFunction(arg111: any) -> None:
# 		print("arg110:", arg110, "arg111:", arg111, "nestedFunction.attribute1:", nestedFunction.attribute1)
# 		nestedFunction.attribute1 += 1
#
# 	nestedFunction.attribute1 = arg110  # This statement attaches the attribute to the nested function.
#
# 	return nestedFunction  # Return the function object.
#
#
# function39 = demonstrateFunctionAttributes(0)  # Assign the function object to "function39".  This function object has an "attribute1" attribute.
# print('function39("spam"):', function39("spam"))
# print('function39("ham"):', function39("ham"))
# print("function39.attribute1:", function39.attribute1)  # Access the function attribute.
#
# function40 = demonstrateFunctionAttributes(42)  # Create another copy of the nested function.
# print("function40.attribute1:", function40.attribute1)
# print("function40.attribute1:", function40.attribute1)
# function40('Incrementing the state ("attribute1"):')
# print("function40.attribute1:", function40.attribute1)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def CustomizedOpen(customizationId: int) -> callable:
# 	print("builtins.open:", builtins.open)
# 	originalOpen = builtins.open
#
# 	def customOpen(*keywordArguments: typing.Iterable, **positionalArguments: typing.Iterable) -> callable:
# 		print('Customizing "open" using classes.  ID: %r:' % id, keywordArguments, positionalArguments)
# 		print("customOpen: originalOpen:", originalOpen, " customizationId:", customizationId)
# 		return originalOpen(*keywordArguments, **positionalArguments)
#
# 	builtins.open = customOpen
#
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in6.txt") as file35:
# 	print("file35:", file35.read())
# CustomizedOpen("hell2")
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in7.txt") as file36:
# 	print("file36:", file36.read())
# CustomizedOpen("hell1")
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in8.txt") as file37:
# 	print("file37:", file37.read())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# class CustomizedOpen:
#
# 	def __init__(self, customizationId: int) -> None:
# 		self.id = customizationId
# 		self.originalOpen = builtins.open
# 		builtins.open = self
#
# 	def __call__(self, *keywordArguments: typing.Iterable, **positionalArguments: typing.Iterable) -> callable:
# 		print('Customizing "open" using classes.  ID: %r:', self.id, keywordArguments, positionalArguments)
# 		print("customOpen: originalOpen:", self.originalOpen, " customizationId:", self.id)
# 		return self.originalOpen(*keywordArguments, **positionalArguments)
#
#
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in6.txt") as file38:
# 	print("file38:", file38.read())
# CustomizedOpen("hell2")
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in7.txt") as file39:
# 	print("file39:", file39.read())
# CustomizedOpen("hell1")
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in8.txt") as file40:
# 	print("file40:", file40.read())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def changer(var111: int, var112: list) -> None:
# 	var111 = 2
# 	var112[0] = "spam"
#
#
# var111 = 1
# list77 = [1, 2]
# print("var111:", var111, "list77:", list77)
# changer(var111, list77)
# print("var111:", var111, "list77:", list77)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def multiple(var112: int, list78: list) -> tuple:
# 	var112 = 2
# 	list78 = [3, 4]
#
# 	return var112, list78
#
#
# var113 = 1
# list79 = [1, 2]
# print("var113:", var113, "list79:", list79)
# var113, list79 = multiple(var113, list79)
# print("var113:", var113, "list79:", list79)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function41(arg140: any, arg141: any) -> None:
# 	print("function41: arg140:", arg140, "arg141:", arg141)
#
#
# def function42(arg142: any, arg143: any) -> None:
# 	print("function42: arg142:", arg142, "arg143:", arg143)
#
#
# if sys.argv[4] == "function41":
# 	function43, arg144 = function41, (1, 2)
# elif sys.argv[4] == "function42":
# 	function43, arg144 = function42, (3, 4)
# else:
# 	function43, arg144 = (None,) * 2
# print("function43:", function43, "arg144:", arg144)
# if function43 is not None:
# 	function43(*arg144)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def keywordOnlyDemo(var114: any, *var115: typing.Iterable, var116: any) -> None:
# 	print("var114:", var114, "var115:", var115, "var116:", var116)
#
#
# keywordOnlyDemo(0, 1, 2, 3, var116 = "var116")
# keywordOnlyDemo(0, var116 = "var116")
# keywordOnlyDemo(0, 1, var116 = 2)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def keywordOnlyDemo(var117: any, *, var118: any, var119: any) -> None:
# 	print("var117:", var117, "var118:", var118, "var119:", var119)
#
#
# keywordOnlyDemo(0, var118 = 3, var119 = "var119")
#
# try:
# 	keywordOnlyDemo(0, var119 = "var119")
# 	keywordOnlyDemo(0)
# except TypeError as ex:
# 	print(sys.exc_info()[0].__name__ + ":", ex, "\n")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def keywordOnlyArgumentsDemo(var120: any, *, var121: int = 0, var122: int = 1, var123: int = 2) -> None:
# 	print("var120:", var120, "var121:", var121, "var122:", var122, "var123:", var123)
#
#
# keywordOnlyArgumentsDemo(3, var121 = 4)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def argumentsOrderDemo(var124: any, *var125: typing.Iterable, var126: int = 0, **var127: typing.Iterable) -> None:
# 	print("var124:", var124, "var125:", var125, "var126:", var126, "var127:", var127)
#
#
# argumentsOrderDemo(0, 1, 2, var126 = 3, arg145 = 4, arg146 = 5)
# argumentsOrderDemo(0, 1, 2, arg145 = 4, arg146 = 5, var126 = 3)
# argumentsOrderDemo(0, 1, 2, arg145 = 4, var126 = 3, arg146 = 5)
#
#
# def argumentsOrderDemo(var128: any, var129: int = 0, *var130: typing.Iterable, **var131: typing.Iterable) -> None:
# 	print("var128:", var128, "var129:", var129, "var130:", var130, "var131:", var131)
#
#
# argumentsOrderDemo(0, 1, 2, var130 = 3, arg147 = 4, arg148 = 5)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def argumentsOrderDemo(var132: int, *var133: typing.Iterable, var134: int = 0, **var135: typing.Iterable) -> None:
# 	print("var132:", var132, "var133:", var133, "var134:", var134, "var135:", var135)
#
#
# argumentsOrderDemo(0, *(2, 3), var134 = 1, arg149 = 4, arg150 = 5)
# try:
# 	argumentsOrderDemo(0, 2, 3, var134 = 1, arg149 = 4, arg150 = 5)
# except SyntaxError as ex:
# 	print("SyntaxError:", ex)
#
# argumentsOrderDemo(0, *{1, 2, 2}, **dict(var134 = 3, arg149 = 4, arg150 = 5))
# try:
# 	argumentsOrderDemo(0, *{1, 2}, **{"arg149": 4, "arg150": 5}, var134 = 3)
# except TypeError as ex:
# 	print("TypeError:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def findMinimum1(*iterable100: typing.Iterable) -> any:
# 	firstItem = iterable100[0]
# 	for it in iterable100[1 :]:
# 		firstItem = min(it, firstItem)
# 	return firstItem
#
#
# print("findMinimum1: Smallest item:", findMinimum1("b", "c", "a", "d"))
#
#
# def findMinimum2(firstItem: any, *iterable101: typing.Iterable) -> any:
# 	for it in iterable101:
# 		minimum = min(it, firstItem)
# 	return minimum
#
#
# print("findMinimum2: Smallest item:", findMinimum2(["b", "c"], ["a", "d"], ["a", "b"], ["a", "a", "b"], ["a", "a"], ["a", "a", "a"]))
#
#
# def findMinimum3(*items: any) -> typing.Iterable:
# 	return sorted(items)[0]
#
#
# print("findMinimum3: Smallest item:", findMinimum3(("b", "c"), ("a", "d"), ("a", "b"), ("a", "a", "b"), ("a", "a"), ("a", "a", "a")))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def findMinOrMax(minOrMax: any, firstItem: any, *restItems: typing.Iterable) -> any:
# 	for it in restItems:
# 		if minOrMax(it, firstItem):
# 			firstItem = it
# 	return firstItem
#
#
# def findMinimum(item: any, firstItem: any) -> None:
# 	return item <= firstItem
#
#
# def findMaximum(item: any, firstItem: any) -> None:
# 	return item >= firstItem
#
#
# print('findMinOrMax(findMinimum, "b", "a", "d", "c"):', findMinOrMax(findMinimum, "b", "a", "d", "c"))
# print('findMinOrMax(findMaximum, "b", "a", "d", "c"):', findMinOrMax(findMaximum, "b", "a", "d", "c"))
#
# print('findMinOrMax(eval(findMinimum.__name__), "b", "a", "d", "c"):', findMinOrMax(eval(findMinimum.__name__), "b", "a", "d", "c"))
# print('findMinOrMax(eval(findMaximum.__name__), "b", "a", "d", "c"):', findMinOrMax(eval(findMaximum.__name__), "b", "a", "d", "c"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def myPrint(*positionalArguments: typing.Iterable, **keywordArguments: typing.Iterable) -> None:
# 	sep = keywordArguments.pop("sep", " ")
# 	end = keywordArguments.pop("end", "\n")
# 	file = keywordArguments.pop("file", sys.stdout)
# 	if keywordArguments:
#
# 		def raiseTypeError(message: str) -> None:
# 			raise TypeError(message)
#
# 		try:
# 			message = f"extra keywords: {keywordArguments}"
# 			raiseTypeError(message)
# 		except TypeError as ex:
# 			print(sys.exc_info()[0].__name__ + ":", ex, "\n")
# 	output = ""
# 	for i, a in enumerate(positionalArguments):
# 		output += str(a) + (sep if i != len(positionalArguments) - 1 else end)
# 	file.write(output)
#
#
# print("myPrint(): Start.")
# myPrint()
# print("myPrint(): End.")
# print()
# myPrint(0, "a", (1, "b"))
# print()
# myPrint(0, "a", (1, "b"), sep2 = "invalid")
# print()
# myPrint(0, "a", (1, "b"), sep = "  ")
# print()
# myPrint(0, "a", (1, "b"), end = "$")
# print()
# myPrint(0, "a", (1, "b"), sep = "|", end = "$")
# print()
# myPrint(0, "a", (1, "b"), sep = "|", end = "$", file = sys.stderr)
# print()
# with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/out5.txt", "w") as file41:
# 	myPrint(0, "a", (1, "b"), sep = "|", end = "$", file = file41)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def summateRecursively(list80: list) -> int:
# 	if not list80:
# 		return 0
# 	return list80[0] + summateRecursively(list80[1 :])
#
#
# print(summateRecursively([0, 1, 2, 3, 4, 5]))
# print(summateRecursively([0]))
# print(summateRecursively([]))
# print(summateRecursively(None))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def summateRecursively(list81: list) -> int:
# 	return 0 if not list81 else list81[0] + summateRecursively(list81[1 :])
#
#
# print(summateRecursively([0, 1, 2, 3, 4, 5]))
# print(summateRecursively([0]))
# print(summateRecursively([]))
# print(summateRecursively(None))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def summateRecursively(list82: list) -> int:
# 	return list82[0] if len(list82) == 1 else list82[0] + summateRecursively(list82[1 :])
#
#
# print(summateRecursively([0, 1, 2, 3, 4, 5]))
# print(summateRecursively([0]))
# print(summateRecursively(["s", "p", "a", "m"]))
# print(summateRecursively(["spam"]))
# print(summateRecursively(["s"]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def summateRecursively(list83: list) -> int:
# 	firstElement, *restElements = list83
# 	return firstElement if not restElements else firstElement + summateRecursively(restElements)
#
#
# print(summateRecursively([0, 1, 2, 3, 4, 5]))
# print(summateRecursively([0]))
# print(summateRecursively(["s", "p", "a", "m"]))
# print(summateRecursively(["spam"]))
# print(summateRecursively(["s"]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def indirectlySummateRecursively(list84: list) -> bool:
# 	if not list84:
# 		return 0
# 	return nonEmpty(list84)
#
#
# def nonEmpty(list85: list) -> int:
# 	return list85[0] + indirectlySummateRecursively(list85[1 :])
#
#
# print(indirectlySummateRecursively([0, 1, 2, 3, 4]))
#
# # LP
#
# list86 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# sum9 = 0
# while list86:
# 	sum9 += list86[0]
# 	list86 = list86[1 :]
# print("sum9:", sum9)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list87 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
#
#
# def sumTree(list87: list) -> int:
# 	sum10 = 0
# 	for e in list87:
# 		if not isinstance(e, list):
# 			sum10 += e
# 		else:
# 			sum10 += sumTree(e)
# 	return sum10
#
#
# print("sumTree(list87):", sumTree(list87))
# list88 = [1, [2, [3, [4, [5]]]]]  # Pathological case (right-heavy).
# print("sumTree(list88):", sumTree(list88))
# list89 = [[[[[1], 2], 3], 4], 5]  # Pathological case (left-heavy).
# print("sumTree(list89):", sumTree(list89))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list90 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
# list90Sum = 0
# list90Copy = list(list90)
# while list90Copy:
# 	print("list90:", list90Copy)
# 	element = list90Copy.pop(0)
# 	if type(element) is not list:
# 		list90Sum += element
# 	else:
# 		list90Copy.extend(element)
# print("list90:", list90)
# print("list90Sum:", list90Sum)
#
# list91 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
# list91Sum = 0
# while list91:
# 	print("list91:", list91)
# 	element = list91.pop(0)
# 	if type(element) is not list:
# 		list91Sum += element
# 	else:
# 		list91.extend(element)
# print("list91:", list91)
# print("list91Sum:", list91Sum)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list92 = [1, [2, [3, 4], 5], 6, [7, 8], [9]]
# sum11 = 0
# while list92:
# 	print("list92:", list92)
# 	print("sum11:", sum11)
# 	element = list92.pop(0)
# 	if type(element) is not list:
# 		sum11 += element
# 	else:
# 		list92[: 0] = element
# print("sum11:", sum11)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print("sys.getrecursionlimit():", sys.getrecursionlimit())
# sys.setrecursionlimit(1048576)
# print("sys.getrecursionlimit():", sys.getrecursionlimit())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function44(number43: int) -> None:
# 	string43 = "spam"
# 	print("string43:", string43)
# 	return string43 * number43
#
#
# print("function44.__code__:", function44.__code__)
# print("dir(function44.__code__):", dir(function44.__code__))
#
# print("function44.__code__.co_varnames:", function44.__code__.co_varnames)
# print("function44.__code__.co_argcount:", function44.__code__.co_argcount)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function510(var1: "spam", var2: (1, 10), var3: float, var4: 2 + 3) -> int:
# 	return var1 + var2 + var3
#
#
# print("function510(1, 2, 3):", function510(1, 2, 3, 4))
# print("function510.__annotations__:", function510.__annotations__)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(lambda var1, var2, var3: var1 + var2 + var3(0, 1, 2))
# lambda100 = lambda var1, var2, var3: var1 + var2 + var3(0, 1, 2)
# try:
# 	lambda100()
# except TypeError as ex:
# 	print("TypeError:", ex)
# lambda101 = lambda var1, var2, var3: var1 + var2 + var3
# print(lambda101(0, 1, 2))
# print(lambda var1, var2, var3: var1 + var2 + var3(0, 1, 2)())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# list93 = [lambda n: n ** 2, lambda n: n ** 3, lambda n: n ** 4]
# for e in list93:
# 	print(e(2))
#
# number100 = {"square": (lambda n: n ** 2), "cube": (lambda n: n ** 2)}["cube"](4)
# print("number100:", number100)
#
# printAll = lambda list100: list(map(print, list100))
# printAll(["spam", "toast", "eggs"])
#
# printAllWithFor = lambda list100: [print(e) for e in list100]
# printAllWithFor(["spam", "toast", "eggs"])
#
# print(lambda list100: [print(e) for e in list100](["spam2", "toast2", "eggs2"]))
#
# lambdaOuter = lambda number100: (lambda number101: number100 - number101)
# lambdaInner = lambdaOuter(1)  # number100 = 1
# number102 = lambdaInner(2)  # number101 = 2
# print(number102)
#
# button1 = tk.Button(text = "Click me!", command = (lambda: print("Clicked me!")))
# button1.pack()
# tk.mainloop()
#
# salariesInLPA = [10, 20, 15]
# print(*(map(lambda salary: salary + (salary * 0.1), salariesInLPA)))
# print(*[salary + (salary * 0.1) for salary in salariesInLPA])
# print(*list(map(lambda a, b: a ** b, [1, 2, 3, 4], [2, 3])))
# print(*list(map(lambda a, b: a ** b, [1, 2, 3, 4], [2, 3, 4, 5])))
# print(*filter(lambda n: n > 0, range(-5, 5)))
# print(*filter(bool, range(-5, 5)))
# print(functools.reduce(lambda a, b: a + b, [1, 2, 3, 4]))
# print(functools.reduce(lambda a, b: a * b, [1, 2, 3, 4]))
# try:
# 	print(functools.reduce(lambda a, b, c: a + b + c, [1, 2, 3, 4]))
# except TypeError:
# 	print("can't pass three args in functools.reduce.")
# print(functools.reduce(lambda currentDifference, e: currentDifference - e, [1, 2, 3, 4]))
# print(functools.reduce(lambda currentDifference, e: currentDifference - e, [100, 2, 3, 4]))
# print(functools.reduce(lambda currentDifference, e: e - currentDifference, [100, 2, 3, 4]))
# try:
# 	print(functools.reduce(lambda currentDifference, e: e - currentDifference, math.nan, []))
# except TypeError:
# 	print("default value in case of empty iterable doesn't work.")
# print(functools.reduce(lambda a, b: operator.add(a, b), [1, 2, 3, 4]))
# print(*list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, range(10)))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# matrix100 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix101 = [ce + 10 for r in matrix100 for ce in r]
# print("matrix101:", matrix101)
# matrix102 = [[ce + 10 for ce in r] for r in matrix100]
# print("matrix102:", matrix102)

# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP

# list96 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list97 = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
# list98 = [list96[r][c] * list97[r][c] for r in range(3) for c in range(3)]
# print("list98:", list98)
# list99 = [[list96[r][c] * list97[r][c] for c in range(3)] for r in range(3)]
# print("list99:", list99)
# list100 = [[ce1 * ce2 for (ce1, ce2) in zip(r1, r2)] for (r1, r2) in zip(list96, list97)]
# print("list100:", list100)
#

# # LP
#
# try:
# 	list101 = [l.rstrip() for l in open("var/in9.txt").readlines()]
# 	print("list101:", list101)
# except:
# 	pass
# try:
# 	list102 = [l.rstrip() for l in open("var/in9.txt")]
# 	print("list102:", list102)
# except:
# 	pass
#
# list103 = list(map(lambda l: l.rstrip(), open("var/in9.txt")))
# print("list103:", list103)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# listOfTuples = [("bob", 35, "mgr"), ("sue", 40, "dev")]
# list104 = [age for (_, age, _) in listOfTuples]
# print("list104:", list104)
# list105 = list(map(lambda r: r[1], listOfTuples))
# print("list105:", list105)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
#
# def generatorFunction1(number103):
# 	for i in range(number103):
# 		yield i ** 2
#
#
# for i in generatorFunction1(5):
# 	print(i, end = " : ")
# print()
#
# print("generatorFunction1:", generatorFunction1)
# generator1 = generatorFunction1(4)
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# try:
# 	print(next(generator1))
# except StopIteration as ex:
# 	print("ex:", ex)
#
# generator2 = generatorFunction1(5)
# print(iter(generator2) is generator2)
# print(next(generator2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# LP

# def capitalizeFields(line):
# 	for field in line.split(","):
# 		yield field.upper()
#
#
# print(tuple(capitalizeFields("aaa,bbb,ccc")))
#
# print({i: s for i, s in enumerate(capitalizeFields("aaa,bbb,ccc"))})
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
#
# def generatorFunction3():
# 	for i in range(10):
# 		j = yield i  # j is assigned the value sent by the caller, since this value doesn't show up in function parameter list.
# 		print("j:", j)
#
#
# generator3 = generatorFunction3()
# print("Calling next.")
# print("next(generator3):", next(generator3))
# print("Sending 77.")
# print("generator3.send(77):", generator3.send(77))
# print("Sending 88.")
# print("generator3.send(88):", generator3.send(88))
# print("Calling next.")
# print("next(generator3):", next(generator3))
# print("Calling next.")
# print("next(generator3):", next(generator3))
# print("Calling next.")
# print("next(generator3):", next(generator3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# generator4 = (i ** 2 for i in range(4))
# print(iter(generator4) is generator4)
# print(next(generator4))
# print(next(generator4))
# print(next(generator4))
# print(next(generator4))
# try:
# 	print(next(generator4))
# except StopIteration as ex:
# 	print("ex:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# for j in (i ** 2 for i in range(4)):
# 	print("%s, %s" % (j, j / 2.0))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# print("".join(e.upper() for e in "aaa,bbb,ccc".split(",")))
#
# e1, e2, e3 = (e + "\n" for e in "aaa,bbb,ccc".split(","))
# print((e1, e3))
#
# print(sum((i ** 2) for i in range(4)))
#
# print(sorted(i ** 2 for i in range(4)))
# print(sorted((i ** 2 for i in range(4)), reverse = True))
#
# print(list(abs(e) for e in (-1, -2, 3, 4)))
#
# line = "aaa,bbb,ccc"
# print("".join(map(str.upper, line.split(","))))
#
# print(list(map(lambda e: e * 2, map(abs, (-1, -2, 3, 4)))))  # Nested map.
# print(list(e * 2 for e in (abs(e) for e in (-1, -2, 3, 4))))  # Nested generators.
# print(list(map(math.sqrt, (e ** 2 for e in range(4)))))
# print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))
# print(list(abs(i) for i in (abs(i) for i in (abs(i) for i in (-1, 0, 1)))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# line = "aa bbb c"
# print("".join(e for e in line.split() if len(e) > 1))  # Generator expression here is simpler than this filter equivalent:
# print("".join(filter(lambda e: len(e) > 1, line.split())))
#
# print("".join(e.upper() for e in line.split() if len(e) > 1))
# print("".join(map(str.upper, filter(lambda e: len(e) > 1, line.split()))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# list106 = [1, 2, 3, 4]
# iterator1, iterator2 = iter(list106), iter(list106)
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator2))
# del list106[2 :]
# try:
# 	print(next(iterator1))
# except StopIteration as ex:
# 	print("ex:", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def function20(n):
# 	for i in range(n):
# 		yield i
# 	for i in (i ** 2 for i in range(n)):
# 		yield i
#
#
# print(list(function20(5)))
#
#
# def function21(n):
# 	yield from range(5)
# 	yield from (i ** 2 for i in range(5))
#
#
# print(list(function21(5)))
# print(" : ".join(str(i) for i in function21(5)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# dict21 = {"a": 1, "b": 2, "c": 3}
# iterator3 = iter(dict21)
# print(next(iterator3))
# print(next(iterator3))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# for _, subdirectory, files in os.walk("."):
# 	for file in files:
# 		if file.startswith("."):
# 			print("file:", file)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
#
# def function22(a, b, c):
# 	print("%s, %s, and %s" % (a, b, c))
#
#
# function22(*range(3))
# function22(*(i for i in range(3)))
#
# dict40 = dict(a = "Bob", b = "dev", c = 40.5)
# print('function22(a = "Bob", b = "dev", c = 40.5):', function22(a = "Bob", b = "dev", c = 40.5))
# print("function22(**dict40):", function22(**dict40))
# print("function22(*dict40):", function22(*dict40))
# print("function22(*dict40.values()):", function22(*dict40.values()))
#
# print(list(print(c.upper(), end = " ") for c in "spam"))
# print(*(c.upper() for c in "spam"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# list99, string99 = [1, 2, 3], "spam"
# for i in range(len(string99)):
# 	string99 = string99[1 :] + string99[: 1]
# 	print(string99, end = " ")
#
# print()
#
# for i in range(len(list99)):
# 	list99 = list99[1 :] + list99[: 1]
# 	print("list99:", list99, end = " ")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def permute1(seq):
# 	if not seq:
# 		return [seq]
# 	else:
# 		res = []
# 		for i in range(len(seq)):
# 			rest = seq[: i] + seq[i + 1 :]
# 			for e in permute1(rest):
# 				res.append(seq[i : i + 1] + e)
# 		return res
#
#
# print("permute1([1, 2, 3, 4, 5, 6]):", permute1([1, 2, 3, 4, 5, 6]))
# for permutation in permute1([1, 2, 3, 4, 5, 6]):
# 	print("permutation:", permutation)
#
#
# def permute2(seq):
# 	if not seq:
# 		yield seq
# 	else:
# 		for i in range(len(seq)):
# 			rest = seq[: i] + seq[i + 1 :]
# 			for e in permute2(rest):
# 				yield seq[i : i + 1] + e
#
#
# print("permute2([1, 2, 3, 4, 5, 6]):", permute2([1, 2, 3, 4, 5, 6]))
# for permutation in permute2([1, 2, 3, 4, 5, 6]):
# 	print("permutation:", permutation)
#
# seq = list(range(10))
# p1 = permute1(seq)  # Only took ~12 seconds.
# print("permute1: done.")
#
# p2 = permute2(seq)  # Returned immediately.
# print("permute2: done.")
#
# p2 = list(permute2(seq))  # Took ~7 seconds.
# print("permute2: done.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# string1 = "abc"
# string2 = "xzy123"
# print(list(zip(string1, string2)))  # Truncates the shorter one.
#
# print(list(zip([-2, -1, 0, 1, 2])))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
# print(list(map(pow, [1, 2, 3, 4], [1, 2, 3, 4])))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def myMap(function1, *sequences):
# 	retval = []
# 	print(sequences)
# 	for args in zip(*sequences):
# 		retval.append(function1(*args))
# 	return retval
#
#
# print(myMap(abs, [-1, -2, 1]))
# print(myMap(pow, [1, 2, 3], [1, 2, 3]))
#
#
# def myMap1(function1, *args):
# 	return [function1(*arg) for arg in zip(*args)]
#
#
# print(myMap1(abs, [-2, -1, 0, 1, 2]))
# print(myMap1(pow, [1, 2, 3], [1, 2, 3]))
#
#
# def myMap2(function1, *args):
# 	for arg in zip(*args):
# 		yield function1(*arg)
#
#
# def myMap3(function1, *args):
# 	return (function1(*arg) for arg in zip(*args))
#
#
# print(list(myMap2(abs, [-2, -1, 0, 1, 2])))
# print(list(myMap2(pow, [1, 2, 3], [1, 2, 3])))
# print(list(myMap3(abs, [-2, -1, 0, 1, 2])))
# print(list(myMap3(pow, [1, 2, 3], [1, 2, 3])))
#
# print(list(map(pow, [1, 2, 3], [1, 2, 3, 4])))
# try:
# 	print(list(map(None, [1, 2, 3], [1, 2, 3, 4])))
# except TypeError as ex:
# 	print("ex: Padding map not available in Python 3.", ex)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def myZip(*sequences):
# 	sequencesAsList = [list(se) for se in sequences]
# 	retval = []
# 	while all(sequencesAsList):
# 		retval.append(tuple(se.pop(0) for se in sequencesAsList))
# 	return retval
#
#
# seq1, seq2 = "abc", "xyz123"
# print(myZip(seq1, seq2))
#
#
# def myPaddingMap(*sequences, pad = None):
# 	sequences = [list(se) for se in sequences]
# 	retval = []
# 	while any(sequences):
# 		retval.append(tuple((se.pop(0) if se else pad) for se in sequences))
# 	return retval
#
#
# print(myPaddingMap(seq1, seq2))
# print(myPaddingMap(seq1, seq2, pad = "AA"))
#
#
# def myZip1(*sequences):
# 	sequences = [list(e) for e in sequences]
# 	while all(sequences):
# 		yield tuple(e.pop(0) for e in sequences)
#
#
# seq1, seq2 = "abc", "xyz123"
# print(list(myZip1(seq1, seq2)))
#
#
# def myPaddingMap1(*sequencesInTuple, pad = None):
# 	sequencesInListOfLists = [list(e) for e in sequencesInTuple]
# 	while any(sequencesInListOfLists):
# 		yield tuple((e.pop(0) if e else pad) for e in sequencesInListOfLists)
#
#
# print(list(myPaddingMap1(seq1, seq2)))
# print(list(myPaddingMap1(seq1, seq2, pad = "AA")))
#
#
#
# def myZip2(*sequences):
# 	minLen = min(len(e) for e in sequences)
# 	return [tuple(e[i] for e in sequences) for i in range(minLen)]
#
#
# seq1, seq2 = "abc", "xyz123"
# print(list(myZip2(seq1, seq2)))
#
#
# def myPaddingMap2(*sequences, pad = None):
# 	maxLen = max(len(e) for e in sequences)
# 	return [tuple((e[i] if len(e) > i else pad) for e in sequences) for i in range(maxLen)]
#
#
# print(list(myPaddingMap2(seq1, seq2)))
# print(list(myPaddingMap2(seq1, seq2, pad = "AA")))

# def myZip3(*sequences):
# 	minLen = min(len(e) for e in sequences)
# 	return (tuple(e[i] for e in sequences) for i in range(minLen))
#
#
# seq1, seq2 = "abc", "xyz123"
# print(myZip3(seq1, seq2))
# print(list(myZip3(seq1, seq2)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP

# dict1 = {k: v for k in [1, 2, 3] for v in [1, 2, 3]}  # Adding another pair with existing key overwrote the value.
# print("dict1:", dict1)

# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
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
# print(timer(pow, 2, 1000))
# print(timer(str.upper, "spam"))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# timer = time.clock if sys.platform[: 3] == "win" else time.time
#
#
# def total(reps, function, *positionals, **keywords):
# 	"""total: total wall clock time taken to run the function reps number of times."""
#
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
# 	"""bestof: best time to execute the funtion reps2 (1000) times, out of reps1 (5) number of times."""
#
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
# 	retval = bestof(reps1, total, reps2, function, *positionals, **keywords)  # Two values for duration because one is of "total" call and the other is for "bestof".  Differences in the values highlight the time taken for the "total" function invocation.
# 	return retval
#
#
# def total(function, *pargs, **kargs):
# 	_reps = kargs.pop("_reps", 1000)
# 	repsList = list(range(_reps))
# 	start = timer()
# 	for i in repsList:
# 		retval = function(*pargs, **kargs)
# 	elapsed = timer() - start
# 	return (elapsed, retval)
#
#
# def bestof(function, *pargs, **kargs):
# 	_reps = kargs.pop("_reps", 5)
# 	best = 2 ** 32
# 	for i in range(_reps):
# 		start = timer()
# 		retval = function(*pargs, **kargs)
# 		elapsed = timer() - start
# 		if elapsed < best:
# 			best = elapsed
# 	return (best, retval)
#
#
# def bestoftotal(function, *pargs, **kargs):
# 	_reps1 = kargs.pop("_reps1", 5)
# 	return min(total(function, *pargs, **kargs) for i in range(_reps1))

# print("total(1000, pow, 2, 1000)[0]:", total(1000, pow, 2, 1000)[0])
# print("total(1000, str.upper, 'spam'):", total(1000, str.upper, "spam"))
# print("bestof(1000, pow, 2, 1000000)[0]:", bestof(1000, pow, 2, 1000000)[0])
# print("bestof(1000, str.upper, 'spam'):", total(1000, str.upper, "spam"))
# print("bestof(50, total, 1000, str.upper, 'spam'):", bestof(50, total, 1000, str.upper, "spam"))
# print("bestoftotal(50, 1000, str.upper, 'spam'):", bestoftotal(50, 1000, str.upper, "spam"))
#
# print("total(1000, pow, 2, 1000)[0]:", total(1000, pow, 2, 1000000)[0])
# print("bestof(1000, pow, 2, 1000)[0]:", bestof(1000, pow, 2, 1000000)[0])
# sys.set_int_max_str_digits(43000)
# print("bestoftotal(5, 100000, pow, 2, 1000000):", bestoftotal(5, 100000, pow, 2, 1000000))  # Execute the total function 5 times.  Prints the best time out of 5.  The total function executes the function 10 times.
# print(min(total(100000, pow, 2, 10000000) for i in range(5)))

# if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
# 	timer = time.perf_counter
# else:
# 	timer = time.clock if sys.platform[: 3] == "win" else time.time
# print(timer)
#

# reps = 10000
# repsList = list(range(reps))

# def forLoop():
# 	retval = []
# 	for i in repsList:
# 		retval.append(abs(i))
# 	return retval
#
#
# def listComp():
# 	return [abs(i) for i in repsList]
#
#
# def mapFunction():
# 	return list(map(abs, repsList))
#
#
# def genExpr():
# 	return list(abs(i) for i in repsList)
#
#
# def genFunc():
#
# 	def gen():
# 		for i in repsList:
# 			yield abs(i)
#
# 	return list(gen())
#
#
# print(sys.version)

# def forLoop():
# 	retval = []
# 	for i in repsList:
# 		retval.append(i + 10)
# 	return retval
#
#
# def listComp():
# 	return [i + 10 for i in repsList]
#
#
# def mapFunction():
# 	return list(map(lambda i: i + 10, repsList))
#
#
# def genExpr():
# 	return list(i + 10 for i in repsList)
#
#
# def genFunc():
#
# 	def provider():
# 		for i in repsList:
# 			yield i + 10
#
# 	return list(provider())

# for test in (forLoop, listComp, mapFunction, genExpr, genFunc):
# 	(bestval, (totalval, retval)) = bestoftotal(5, 1000, test)
# 	print("%-9s: %.5f : %f => [%s...%s]" % (test.__name__, bestval, totalval, retval[0], retval[-1]))

# for test in (forLoop, listComp, mapFunction, genExpr, genFunc):
# 	(totalval, retval) = bestoftotal(test, _reps1 = 5, _reps = 1000)
# 	print("%-9s: %.5f => [%s...%s]" % (test.__name__, totalval, retval[0], retval[-1]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# print(min(timeit.repeat(stmt = "[i ** 2 for i in range(1000)]", number = 1000, repeat = 5)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# x = 0
#
#
# def function102():
# 	print(x)
#
#
# function102()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
# var101 = 0
#
#
# def function103():
# 	import __main__  # Import enclosing module.
#
# 	print("__main__.var101:", __main__.var101)  # Qualify it to get the global name.
# 	var101 = 1  # Unqualified refers to the local scope.
# 	print(var101)
#
#
# function103()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP

# def function110():
# 	function110.list110.append(0)
# 	print(function110.list110)
#
#
# function110.list110 = []
# function110()
# function110()
# function110()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")

# # LP
#
#
# def decorator1(function500: callable) -> callable:
# 	print("decorator1:")
# 	return function500
#
#
# @decorator1
# def function500() -> None:
# 	print("function500:")
#
#
# print("function500():", function500())
#
#
# def decorator2(function502: callable,) -> callable:
# 	print("decorator2:")
# 	print("Before calling function explicitly from decorator.")
# 	function502()
# 	print("After calling function explicitly from decorator.")
# 	return function502
#
#
# @decorator2
# def function501() -> None:
# 	print("function501:")
#
#
# print("function501():", function501())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# def decorator10(function503: callable,) -> callable:
# 	print("decorator10:", decorator10, "function503:", function503,)
#
# 	def wrapper(*iterable500: typing.Iterable,) -> None:
# 		print("wrapper: iterable500:", iterable500,)
# 		function503(*iterable500)
#
# 	return wrapper
#
#
# @decorator10
# def function503(var500: any, var501: any) -> None:
# 	print("function503: var500:", var500, "var501:", var501,)
# 	tuple500 = var500, var501
# 	print("function503: tuple500:", tuple500,)
#
#
# function503(100, 101)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # LP
#
#
# class Decorator1:
#
# 	def __init__(self, function500: callable) -> None:  # On "@" decoration.
# 		print("__init__: function500:", function500)
# 		self.function500 = function500
#
# 	def __call__(self, *args: typing.Iterable) -> None:  # On wrapped function call.
# 		print("self.function500:", self.function500)
# 		print("self.function500(1000, 1001):", self.function500(1000, 1001))
# 		print("self.function500(*args):", self.function500(*args))
#
#
# @Decorator1
# def function501(arg1: any, arg2: any) -> None:
# 	print("function501: arg1:", arg1, "arg2:", arg2)  # Passed to "__init__".
#
#
# function501(100, 101)  # Passed to "__call__".
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(math.log2(1024))
#
# print(2 ** 31)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# try:
# 	with pathlib.Path.open("/home/punit/src/_not_mine/PythonTestBed/var/in.txt") as file42:
# 		for l in file42:
# 			print(l.strip())
# 			print(int(l.strip()))
# except OSError as ex:
# 	print(f"I/O Error: ({ex.errno}): {ex.strerror})")
# 	print(sys.exc_info()[0])
# except ValueError as ex:
# 	print("ValueError: Could not convert data to an integer.", ex)
# except:
# 	print("Unexpected error:", sys.exc_info()[0])
#
# 	print(sys.exc_info())
# 	print(type(sys.exc_info()))
#
# 	raise
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
#
# def counter(threadId: int, count: int) -> None:
# 	for i in range(count):
# 		print(f"Thread ID: {threadId}.  i: {i}.")
# 		time.sleep(2)
#
#
# print("Main thread running.")
#
# for i in range(5):
# 	_thread.start_new_thread(counter, (i, 5))
#
# time.sleep(12)
#
# print("Main thread exiting.")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN [OLD VERSION OF TUTORIAL PROBABLY]
#
#
# def asyncZip(inputFile: str, outputFile: str) -> None:
# 	print("Background thread started.")
# 	with zipfile.ZipFile(outputFile, "w") as zipFile2:
# 		zipFile2.write(inputFile)
# 	print("Background thread ended. ", inputFile)  # This thread is run in background (background thread).
#
#
# print("Main thread started.")
#
# _thread.start_new_thread(asyncZip, ("/home/punit/src/_not_mine/PythonTestBed/doc/Changelog.org", "/home/punit/src/_not_mine/PythonTestBed/var/new.zip"))
# time.sleep(1)
#
# print("Main thread ended.")  # This is main thread, running simultaneously.
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# with zipfile.ZipFile("/home/punit/src/_not_mine/PythonTestBed/tmp/Changelog.zip", "w") as zipFile3:
# 	zipFile3.write("/home/punit/src/_not_mine/PythonTestBed/doc/Changelog.org")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(readline.get_history_length())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# # def merge_lists() -> None:
# # 	lengthList1 = input()
# # 	lengthList2 = input()
# # 	count = 0
# # 	list1 = list2 = list3 = []
# # 	while count < int(lengthList1):
# # 		list1.append(int(input()))
# # 		count += 1
# # 	count = 0
# # 	while count < int(lengthList2):
# # 		list2.append(int(input()))
# # 		count += 1
# #
# # 	number6 = number7 = 0
# # 	while number6 < int(lengthList1) and number7 < int(lengthList2):
# # 		if int(list1[number6]) < int(list2[number7]):
# # 			list3.append(list1[number6])
# # 			number6 += 1
# # 		else:
# # 			list3.append(list2[number7])
# # 			number7 += 1
# #
# # 	list3 = list3 + list1[number6:] + list2[number7:]
# #
# #
# # if __name__ == "__main__":
# # 	merge_lists()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(math.pi)
#
# try:
# 	print(math.sqrt(-1))
# except ValueError as ex:
# 	print("ValueError:", ex)
#
# print(str(math.sqrt(10))[0])
#
# print(str(math.pi)[len(str(math.pi)) - 2])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(len(list(string44)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(f"{'wham'}, {'bang'}, and {'thank you'}, ma'am")
# print("{}, {}, and {}, ma'am".format("wham", "bang", "thank you"))
#
# print(f"{3000.14159:,.2f} and {3:+04d}")
# print(f"{3:+04d} and {30.300999:.3f}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(list("🌥".encode()))
# print(list("🌥".encode("utf-16")))
#
# print(list("🌥".encode("utf-32")))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(platform.version(), platform.release(), platform.python_version())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(f"{31415.926:e}")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# number43 = 3.3
# print("Equal" if number43 == 1.1 + 2.3 else "Unequal")
# print((99999999999999999999999).bit_length() + 1)
#
# print(complex(2 + -3j) * 3)
# print(2 + -3j * 3)
#
# print(cmath.cos(complex(2, -3)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(1 / math.e)
#
# print(math.sqrt(math.sin(math.pi / 2)))
# print(pow(2, 4))
#
# print(abs(-2))
# print(max(1, 2, 3, 4), min(1, 2, 3, 4))
#
# print(math.floor(-2.1))
# print(math.trunc(-2.1))
#
# print(round(-2.1111, 2))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# set17 = set("set17")
# set18 = set("set18")
#
# set19 = set17.intersection(set18)
# print(set17)
#
# set19.add("sets")
# print(set19)
#
# set19.update(["s", "e", "t", "1", "9"])
# print(set19)
#
# set19.update("set19")
# print(set19)
#
# set19 = set19.union("set1")
# print(set19)
#
# print("Is subset" if {1, 2, 3, 9}.issubset(range(10)) else "Not subset")
# print(dir(set19))
#
# list93 = [1, 2, 3, 4, 5, 4, 3, 2]
# list93 = list(set(list93))
#
# print(list93)
# print(set([1, 3, 5]) - {1, 2, 3, 4, 5})
#
# print(set(dir(str)) - set(dir(bytes)))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print(True + 4)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# list94 = [1, 2, 3]
# list95 = list94
# list95[2] = 4
# print("list95:", list95)
# list95 = list94[:]
# list95[2] = 5
# print("list94:", list94, "list95:", list95)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print("sys.argv[0]:", sys.argv[0], "len(sys.argv[0]):", len(sys.argv[0]))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# number44 = 14
# number45 = 21
# if (number44 // number45) * number45 + (number44 % number45) == number44:
# 	print("True")
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# list96 = [4, 3, 1, 2]
# list96.sort()
# print("list96:", list96)
# try:
# 	list96.shuffle()
# except AttributeError as ex:
# 	print("AttributeError:", ex)
#
# random.shuffle(list96)
# print("list96:", list96)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# list97 = [(20, 21), (11, 10), (00, 40)]
# try:
# 	list97.sort(key = 2)
# 	list97.sort(key = 1)
# except TypeError as ex:
# 	print("TypeError:", ex)
# list97.sort(key = lambda mykey: mykey[1])
# print(list97)
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# print(fruits.count("apple"))
# print(fruits.count("tangerine"))
# print(fruits.index("banana"))
# print(fruits.index("banana", 4))
# print(fruits.reverse())
# print(fruits)
# print(fruits.append("grape"))
# print(fruits)
# print(fruits.sort())
# print(fruits)
# print(fruits.pop())
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# row1 = ["00", "01", "02"]
# row2 = ["10", "11", "12"]
# matrix = [row1, row2]
# print(matrix)
# print(matrix[0][1])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print([1, 2] < [2, 1])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# print("Decimal is fixed-precision unlike floating-points" if decimal.Decimal("1.11") + decimal.Decimal("2.22") == decimal.Decimal("3.33") else "it's not")
# print(decimal.Decimal.from_float(1.11))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # UNKNOWN
#
# pprint.pprint([[[["test", "ok", "4", "3"]], [["test", "1", "2", "1"]]]], width = 1)
# list98 = [[[["test", "ok", "4", "3"]], [["test", "1", "2", "1"]]]]
# [print(e) for e in list98]
# for e in list98:
# 	print(" ".join(map(str, e)))
#
#
# def function501(list99: list) -> list:
# 	yield from list99
#
#
# for i in function501(list98):
# 	print(*i)
#
# print("\n".join(" ".join(map(str, e)) for e in list98))
#
# for _ in list98:
# 	print(*[e[0] for e in list98])
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
#
# # #MIRAGE-CLIENT@MATRIX.ORG:
# print(hex(ord(b"\xef\xb8\x8f".decode("utf-8"))))
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, sep = "", end = "\n\n")
