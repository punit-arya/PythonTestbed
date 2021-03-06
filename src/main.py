'''
PythonTestbed: Python testbed.
'''

from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())


print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# TUTORIAL.  3.5.2.
the_world_is_flat = True
if the_world_is_flat:
	print("Be careful not to fall off!")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(17 / 3)
print(17 // 3)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(5 ** 2)
print(-3 ** 2)
print((-3) ** 2)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print('C:\some\name')
print(r'C:\some\name')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print("""\
Usage: thingy [OPTIONS]
		-h		Display this usage message
		-H hostname	Hostname to connect to
""")
text = ('''A
	B''')
print(text)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(3 * 'un' + 'ium')
print('Py' 'thon')	# Concatenation.  Works with literals only, no variables or expressions.  Works across literal newline characters if enclosed within parentheses.
prefix = 'Py'
print(prefix + 'thon')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
word = 'Python'
print(word[0])
print(word[-1])
print(word[0:2])
print(word[:2] + word[2:])
print(word[4:42])
# word[0] = 'J'
print('J' + word[1:])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
s = 'supercalifragilisticexpialidocious'
print(len(s))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print("Shallow copy: ", squares[:])
squares = squares + [36, 49, 64, 81, 100]
print(squares)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
print(cubes.append(216))
cubes.append(7 ** 3)
print(cubes)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a + b

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a, b = 0, 1
while b < 1000:
	print(b, end = ',')	# Don't append a newline to output, instead replace it with ','.  'end' is a keyword.
	a, b = b, a + b
print()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
x = int(input("Integer ? "))
if x < 0:
	x = 0
	print('Negative changed to zero.')
elif x == 0:
	print('Zero.')
elif x == 1:
	print('Single.')
else:
	print('More')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
words = ['cat', 'window', 'defenestrate']
for w in words:	# 'for' iterates over the items of any sequence (a list or a string).  This form can not modify the items.
	print(w, len(w))

for w in words[:]:	# Makes a copy of 'words' to enable modification.
	if len(w) > 6:
		words.insert(0, w)
print(words)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for i in range(5):
	print(i)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):	# Use 'enumerate()' function instead.
	print(i, a[i])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(range(10))	# 'range(0, 10)' Doesn't work because range doesn't return a list.  Instead, it returns an iterator object to save space.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(list(range(5)))	# Creates list from iterables.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n // x)
			break
		else:
			print(n, 'is a prime number')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
# while True:
#	  pass

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class MyEmptyClass:
	pass

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def initlog(*args):
	pass

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def fib(n):
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a + b
	print()

fib(2000)
f = fib
f(100)
fib(0)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def fib2(n):
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
f100 = fib2(100)
print(f100)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def ask_ok(prompt, retries = 4, reminder = 'Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):	# 'in' is a keyword.  Tests whether a value is in a sequence.
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)
ask_ok('Do you really wanna quit ? ')
ask_ok('OK to overwrite the file ? ', 2)
ask_ok('OK to overwrite the file ? ', 2, 'Come on, only yes or no!')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
i = 5

def f(arg = i):
	print(arg)

i = 6
f()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def f(a, L = []):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def f(a, L = None):
	if L is None:
		L = []
	L.append(a)
	return L

print(f(1))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
# 'parrot' accepts one positional argument (the value of this argument is taken from the first argument in the function call) and three keyword (or optional) arguments.
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
	print("-- This parrot wouldn't", action, end = ' ')
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")

parrot(1000)	# 1 positional argument.
parrot(voltage = 1000)	# 1 keyword argument.
parrot(voltage = 1000, action = 'VOOOOOM')	# 2 keyword arguments.
parrot(action = 'VOOOOOM', voltage = 1000000)	# 2 keyword arguments.
parrot('a million', 'bereft of life', 'jump')	# 3 positional arguments.
parrot('a thousand', state = 'pushing up the daisies')	# 1 positional, 1 keyword.
# parrot(voltage = 5.0, 'dead')	# Invalid call because 'dead' is a nonkeyword argument so should be at the first position.  i.e., keyword arguments must follow positional arguments.
# parrot(110, voltage = 220)	# Invalid, because duplicate values for same argument.
# parrot(actor = 'John Cleese')	# Keyword argument name is mispelt.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper = "Michael Palin", client = "John Cleese", sketch = "Cheese Shop Sketch")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def concat(*args, sep = "/"):
	return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep = "."))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def parrot(voltage, state = 'a stiff', action = 'voom'):
	print("-- This parrot wouldn't", action, end = ' ')
	print('if you put', voltage, 'volts through it.', end = ' ')
	print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)	# make_incrementor makes and returns the adder and assigns to 'f' which is a reference to a function.
print(f(0))	# Calling 'f' with '0', calls the lambda function and assigns the '0' argument to 'x'.  0 = x, 42 = n.
print(f(1))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]	# Two-dimensional array: two rows, two columns.
pairs.sort(key = lambda pair: pair[1])	# 'sort' takes no arguments, or one argument which should be a lambda function.  This lambda function should return the key.  The elements of the 'pairs' array is passed as an argument to the lambda function that is known as 'pair' inside the lambda function.
print(pairs)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def myfunction():
	"""Do nothing, but document it.

	No, really, it doesn't do anything.
	"""
	pass

print(myfunction.__doc__)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def f(ham: str, eggs: str = 'eggs') -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs

f('spam')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)	# 'x' will be inserted at the index 'i'.  So, 'a.insert(len(a), x)' is same as 'a.append(x)'.
a.append(333)	# Equivalent to: 'a[len(a):] = [x]'
print(a)
print(a.index(333))	# Return the index of the item 'x'.
a.remove(333)	# Removes the first occurrence of 'x'.  Returns an error if item 'x' is not found.
print(a)
a.reverse()	# Reverse the elements of the list in place.
print(a)
a.sort()
print(a)
a.pop()	# If 'i' is not given, it removes and returns the last item in the list.
print(a)
print(a.extend(a))	# Equivalent to: a[len(a):] = L
print(a.count(333))	# Return the number of times '333' appears in the list.
print(a.sort(key = None, reverse=False))	# Sort the items of the list in place.  See 'sorted()' for explanation of the optional arguments.
# print(a.pop([2]))	# List passed instead of integer.
a.clear()	# Equivalent to 'del a[:].
copyOfA = a.copy()	# Return a shallow copy of the list.  Equivalent to 'a[:]'.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
squares = []
for x in range(10):
	squares.append(x ** 2)
print(squares)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
squares = list(map(lambda x: x ** 2, range(10)))	# Equivalent.  List comprehension.
print(squares)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
squares = [x ** 2 for x in range(10)]
print(squares)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])	# Equivalent to:

combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))
print(combs)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
freshfruit = ['	 banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print([(x, x ** 2) for x in range(6)])	# To create a list of tuples.
print([x, x ** 2] for x in range(6))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])	# Flatten a list of tuples using listcomp.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print(transposed)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
print(transposed)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(list(zip(*matrix)))		# Better than listcomp.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a		# Deletes entire variable.
# print(a)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
# t[0] = 88888	# Tuples are immutable.  They can contain mutable objects.
print(t[0])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
v = ([1, 2, 3], [3, 2, 1])
print(v)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
t = 12345, 54321, 'hello!'	# Packing a tuple.
print(t)
x, y, z = t	# Unpacking a tuple.  This can work for any sequence.
print(x, y, z)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))	# List of all keys in arbitrary order.
print(sorted(tel.keys()))	# Sorted keys.
print('guido' in tel)
print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print({x: x ** 2 for x in (2, 4, 6)})		# Dict comprehensions.

print(dict(sape = 4139, guido = 4127, jack = 4098))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}?  It is {1}.'.format(q, a))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for i in reversed(range(1, 10, 2)):
	print(i)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):	# sorted() takes any sequence and returns a new list.
	print(f)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)
print(filtered_data)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import fibo

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)
fib = fibo.fib
print(fib(500))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from fibo import fib, fib2

print(fib(500))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from fibo import *

print(fib(500))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import sys

# print(sys.ps1)
# print(sys.ps2)
# sys.ps1 = 'C> '
# print(sys.ps1)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import sys

sys.path.append('/home/punit/lib/python')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import fibo, sys

print('dir(fibo):', dir(fibo))
print('dir(sys):', dir(sys))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import fibo

a = [1, 2, 3, 4, 5]
fib = fibo.fib
print('dir():', dir())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import builtins

print('dir(builtins):', dir(builtins))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print('sys.path:', sys.path)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
s = 'Hello, world!'
print(repr(s))
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'Value of x is ' + repr(x) + ' and y is ' + repr(y) + '...'
print(s)
hello = 'Hello, world!\n'
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('spam', 'eggs'))))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ')
	print(repr(x * x * x).rjust(4))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food = 'spam', adjective = 'absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other = 'George'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

print('Value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
	print('{0:10} ==> {1:10d}'.format(name, phone))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637378}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}: Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

print('Value of PI is approx. %5.3f.' % math.pi)

f = open('../var/in.txt', 'r')
print(f.read())
print(f.read())
print(f.readline())
print(f.readline())
f.close()

f = open('../var/in.txt', 'r')
for line in f:
	print(line, end = '')

f = open('../var/out.txt', 'w')
f.write('This is a test\n')
value = ('answer', 42)
s = str(value)
f.write(s)
f.close()

f = open('../var/out.txt', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()
# f.read()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
with open('../var/in.txt', 'r') as f:
	read_data = f.read()
print(f.closed)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import json

print(json.dumps([1, 'simple', 'list']))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
f = open('../var/out1.txt', 'w')
x = [1, 'simple', 'list']
json.dump(x, f)
f.close()
f = open('../var/out1.txt', 'r')
y = json.load(f)
print(y)
f.close()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
while True:
	try:
		x = int(input('Please enter a number: '))
		break
	except ValueError:
		print('Oops! Invalid number.')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class B(Exception):
	pass

class C(B):
	pass

class D(C):
	pass

for myClass in [B, C, D]:
	try:
		raise myClass()
	except D:
		print('D')
	except C:
		print('C')
	except B:
		print('B')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import sys

while True:
	try:
		f = open('../var/in1.txt')
		s = f.readline()
		i = int(s.strip())
	except OSError as e:
		print("OS error: {0}".format(e))
	except ValueError:
		print("Could not convert data to an integer.")
	except:
		print("Unexpected error:", sys.exc_info()[0])
	break

for arg in sys.argv[1:]:
	try:
		f = open(arg, 'r')
	except IOError:
		print('can not open', arg)
	else:
		print(arg, 'has', len(f.readlines()), 'lines')
		f.close()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)
	x, y = inst.args
	print('x = ', x)
	print('y = ', y)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def this_fails():
	x = 1 / 0

try:
	this_fails()
except ZeroDivisionError as error:
	print('Handling run-time error:', error)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
try:
#	 raise NameError('Hi There')
	pass
except NameError:
	print('An exception flew by!')
	raise

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Error(Exception):
	""" Base class for exceptions in this module. """
	pass

class InputError(Error):
	""" Exceptions raised for errors in the input.

	Attributes:
		expression -- input expression in which the error occurred
		message -- explanation of the error
	"""

	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class TransitionError(Error):
	""" Raised when an operation attempts a state transition that's not
	allowed.

	Attributes:
		previous -- state at beginning of transition
		next -- attempted new state
		message -- explanation of why the specific transition is not allowed
	"""

	def __init__(self, previous, next, message):
		self.previous = previous
		self.next = next
		self.message = message

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
try:
	# raise KeyboardInterrupt
	pass
finally:
	print('Goodbye, World!')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def divide(x, y):
	try:
		result = x + y
	except ZeroDivisionError:
		print('Division by zero!')
	else:
		print('Result is:', result)
	finally:
		print('Executing finally clause.')

divide(2, 1)
divide(2, 0)
# divide('2', '1')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def scope_test():
	def do_local():
		spam = 'local spam'

	def do_nonlocal():
		nonlocal spam
		spam = 'nonlocal spam'

	def do_global():
		global spam
		spam = 'global spam'

	spam = 'test spam'
	do_local()
	print('After local assignment:', spam)
	do_nonlocal()
	print('After nonlocal assignment:', spam)
	do_global()
	print('After global assignment:', spam)
scope_test()
print('In global scope:', spam)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class MyClass:
	""" A simple example class """
	i = 12345

	def f(self):
		return 'Hello, world!'

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
x = MyClass()
x.counter = 1
while x.counter < 10:
	x.counter = x.counter * 2
print(x.counter)
del x.counter

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
xf = x.f
# while True:
print(xf())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Dog:
	kind = 'canine'

	def __init__(self, name):
		self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Dog:
	tricks = []

	def __init__(self, name):
		self.name = name

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def f1(self, x, y):
	return min(x, x + y)

class C:
	f = f1

	def g(self):
		return 'Hello, world!'

	h = g

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Bag:
	def __init__(self):
		self.data = []

	def add(self, x):
		self.data.append(x)

	def addtwice(self, x):
		self.add(x)
		self.add(x)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update

class MappingSubclass(Mapping):
	def update(self, key, values):
		for items in zip(key, values):
			self.items_list.append(item)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Employee:
	pass

john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
for element in [1, 2, 3]:
	print(element)
for element in (1, 2, 3):
	print(element)
for key in {'one': 1, 'two': 2}:
	print(key)
for char in '123':
	print(char)
for line in open('../var/in.txt'):
	print(line, end = '')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
class Reverse:
	''' Iterating for looping over a sequence backwards. '''
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]
rev = Reverse('spam')
print(iter(rev))
for char in rev:
	print(char)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
def reverse(data):
	for index in range(len(data) - 1, -1, -1):
		yield data[index]

	for char in reverse('golf'):
		print(char)

print(sum(i * i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x * y for x, y in zip(xvec, yvec)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from math import pi, sin

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print(sine_table)
# unique_words = set(word for line in page for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)
data = 'golf'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import os

print(os.getcwd())
os.chdir('../var/log/')
os.system('mkdir pythontestbed')
os.chdir('/home/punit/src/PythonTestbed/src/')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import os

print(dir(os))
# print(help(os))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import shutil

print(os.getcwd())
shutil.copyfile('../var/in.txt', '../var/copy_of_in.txt')
shutil.move('../var/copy_of_in.txt', '../var/copy_of_in_moved.txt')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import glob

print(glob.glob('*.py'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import sys

print(sys.argv)
sys.stderr.write('Warning, log file not found starting a new one\n')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import re

print(re.findall(r'\bf[a-z]*', 'which foot fell on hand fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat'))

print('tea for too'.replace('too', 'two'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

print(math.cos(math.pi / 4))
print(math.log(1024 / 2))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from urllib.request import urlopen

# with urlopen('https://www.usno.navy.mil/USNO/time/display-clocks/simpletime') as response:
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
	for line in response:
		line = line.decode('utf-8')
		if 'EST' in line or 'EDT' in line:
			print(line)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
# import smtplib
#
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# 	"""To: jcaesar@example.org
# 	From: soothsayer@example.org'
#
# 	Beware the Ides of March.
# 	""")
# server.quit()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from datetime import date

now = date.today()
print(now)
print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))
birthday = date(2020, 3, 15)
age = now - birthday
print(age.days)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
print('crc32:', zlib.crc32(s))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from timeit import Timer

print(Timer('t = a; a = b; b = t', 'a = 1; b = 2').timeit())
print(Timer('a, b = b, a', 'a = 1; b = 2').timeit())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
# not able to debug.

# def average(values):
# 	""" Computes the arithmetic mean of a list of numbers.
#
# 	>>> print(average([20, 30, 70]))
# 	40.0
# 	"""
# 	return sum(values) / len(values)
#
# import doctest
#
# doctest.testmod()
#
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
# 	def test_average(self):
# 		self.assertEqual(average([20, 30, 70]), 40.0)
# 		self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#
# 		with self.assertRaises(zeroDivisionError):
# 			average([])
# 		with self.assertRaises(TypeError):
# 			average([20, 30, 70])
#
# unittest.main()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import reprlib

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import pprint

t = [[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]
print('len(t):', len(t))
print('len(t[0]:', len(t[0]))
print('len(t[0][0]):', len(t[0][0]))
print('len(t[0][0][0]):', len(t[0][0][0]))
print('t:', t)
print('t[0]:', t[0])
print('t[0][0]:', t[0][0])
print('t[0][0][0]:', t[0][0][0])
pprint.pprint(t, width = 30)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import textwrap

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width = 40))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
conv = locale.localeconv()

x = 1234567.8
print(locale.format('%d', x, grouping = True))
print(locale.format_string('%s%.*f', (conv['currency_symbol'], conv['frac_digits'], x), grouping = True))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from string import Template

t = Template('${village} folk send $$10 to $cause.')
print(t.substitute(village = 'Nottingham', cause = 'the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item = 'unladen swallow')
# t.substitute(d)
print(t.safe_substitute(d))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
	delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')

for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename)
	newname = t.substitute(d = date, n = i, f = ext)
	print('{0} --> {1}'.format(filename, newname))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import struct

with open('/mnt/pc4-windows/Users/punit/Documents/_OOS/Hacking/CEH/Hacker School/metasploitable-linux-2.0.0.zip', 'rb') as f:
	data = f.read()

start = 0
for i in range(3):
	start += 14
	fields = struct.unpack('<IIIHH', data[start:start+16])
	crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

	start += 16
	filename = data[start:start+filenamesize]
	start += filenamesize
	extra = data[start:start+extra_size]
	print("Header ", i + 1, ":", sep = '', end = '')
	print(filename, hex(crc32), comp_size, uncomp_size)

	start += extra_size + comp_size

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import threading, zipfile

class AsyncZip(threading.Thread):	# Like Java, we need to create a class that will create a thread object.
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)	# This line should be there for every thread class in its 'init'.  Doesn't work.
		self.infile = infile	# Initialise other fields of your thread class.
		self.outfile = outfile
		# pass

	def run(self):	# Define the operations to be done by the thread.
		f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)	# Operation step number one.
		f.write(self.infile)
		f.close()
		print('Finished backgound zip of: ', self.infile)	# This thread is run in background (background thread).

background = AsyncZip('../var/in.txt', '../var/in.zip')		# Create your thread.
background.start()	# Start the execution of your thread.
print('The main program continues to run in foreground')	# This is main thread, running simultaneously.

background.join()	# Wait for background task to finish.
print("Background done.")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import logging

logging.debug('Debug message')
logging.info('Informational message')
logging.warning('Warning: %s', 'server.conf')
logging.error('Error')
logging.critical('Critical error')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import weakref, gc

class A:
	def __init__(self, value):
		self.value = value
	def __repr__(self):
		return str(self.value)
a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print("d['primary']:", d['primary'])
del a
gc.collect()
# print("d['primary']:", d['primary'])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from array import array

a = array('H', [4000, 10, 700, 22222])	# 'H' is typecode for 2-byte unsigned binary number, thus 2 bytes per entry.
print('sum:', sum(a))
print('a[1:3]:', a[1:3])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(0.70 * 1.05, 2))

print(Decimal('1.00') % Decimal('0.10'))
print(1.00 % 0.10)
print(sum([Decimal('0.1')] * 10) == Decimal('1.0'))
print(sum([0.1] * 10) == 1.0)

getcontext().prec = 36
print(Decimal(1) / Decimal(7))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

print(format(math.pi, '.12g'))
print(format(math.pi, '.2f'))
print(repr(math.pi))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(.1 + .1 + .1 == .3)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
print(round(0.1, 20) + round(0.1, 20) + round(0.1, 20) == round(0.3, 20))
print(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
import math

x = 3.14159
print(x.as_integer_ratio())	# Much more exact than smaller numbers for lossless recreation of original numbers.
print(x.hex())
print(x == float.fromhex('0x1.921f9f01b866ep+1'))

print(sum([0.1] * 10) == 1.0)

print(math.fsum([0.1] * 10) == 1.0)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(2 ** 52 <= 2 ** 56 // 10 < 2 ** 53)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
q, r = divmod(2 ** 56, 10)
print(r)
print(q + 1)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
print(0.1 * 2 ** 55)
print(3602879701896397 * 10 ** 55 // 2 ** 55)

print(format(0.1, '.17f'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# TUTORIAL.  3.5.2.
from decimal import Decimal
from fractions import Fraction

print(Fraction.from_float(0.1))
print(0.1.as_integer_ratio())
print(Decimal.from_float(0.1))
print(format(Decimal.from_float(0.1), '.17'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 97.
print(len(str(2 ** 1000000)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 102.
S = 'shrubbery'
L = list(S)
L[1] = 'c'
L = ''.join(L)
print(L)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5. p. 102.
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5. p. 102.
S = 'spam'
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))
print(S)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 103.
line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 104.
S = 'spam'
print(S + 'NI!')
print(S.__add__('NI!'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 104.
print(help(S.replace))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 107.
print('sp\xc4\u00c4\U000000c4m')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 108.
import re

match = re.match('Hello[ \t]*(.*)world', 'Hello		Python world')
print(match.group(1))

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
# match = re.match('(.*)[/:](.*)[/:](.*)[/:](.*)', 'lumberjack:/home/user')
print(match.groups())

print(re.split('[/:]', '/usr/home/lumberjack'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p.112.  NOT ALL THE STUFF.
myList = [1, 2]
print(myList + [3])
print(myList * 2)
myList.append('PALLAVI')
print(myList)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
secondColumn = [row[1] + 1 for row in matrix if row[1] % 2 == 0]
print(secondColumn)
diagonal = [matrix[row][row] for row in [0, 1, 2]]
print(diagonal)
doubledLetters = [character * 2 for character in 'PALLAVI']
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
print('list map sum: ' + str(list(map(sum, matrix))))
print(list(map(sum, matrix)))
print(matrix)
print({sum(row) for row in matrix})
print({row: sum(matrix[row]) for row in range(3)})
print([ord(character) for character in 'PALLAVIBABY'])
print({ord(character) for character in 'PALLAVI'})

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 115, 116, and so on.
myDictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(myDictionary['key1'] + str(1))
# myDictionary1['key3'] = 'value3'
# print(myDictionary1['key3'])
myDictionary1 = dict(key4 = 'value4')
print(myDictionary1['key4'])
myDictionary2 = dict(zip(['name', 'age', 'salary'], ['Pallavi', 27, 1000000]))
print(myDictionary2)
print(myDictionary2.get('name2', 'Punit'))
print(myDictionary2['name'] if 'name2' in myDictionary2 else 'Punit')
keys = list(myDictionary2.keys())
print(keys)
for key in sorted(myDictionary2):
	print(myDictionary2[key])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 118.
D = {'a': 1, 'b': 2, 'c': 3}
value = D.get('x', 0)
print(value)
value = D['x'] if 'x' in D else 0
print(value)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 121.
myTuple = 'item1', 2, 3.0, ['four1', 'four2'], 'item1'
print(myTuple[1])
print(myTuple.index(2))
print(myTuple.count('item1'))
print(myTuple[3])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 121.
T = (1, 2, 3, 4)
T = (2,) + T[1:]
print(T)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 124.
import struct

packed = struct.pack('>i10sh', 7, b'PALLAVI', 8)	# Create packed binary data.
print(packed)
myFile = open('/home/punit/src/PythonTestbed/var/bytestring.bin', 'wb')	# Open binary output file.
myFile.write(packed)
myFile.close()

readString = open('/home/punit/src/PythonTestbed/var/bytestring.bin', 'rb').read()
print(readString)
print(readString[4:8])
print(len(readString))
print(list(readString))
print('Read: ' + readString.decode())
print(struct.unpack('>i10sh', readString))	# Unpack in to objects again.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 124.
S = 'sp\xc4m'
print(S)

file = open('../var/unicode_data.txt', 'w', encoding = 'utf-8')
file.write(S)
file.close()

text = open('../var/unicode_data.txt', encoding = 'utf-8').read()
print(text)
print(len(text))

raw = open('../var/unicode_data.txt', 'rb').read()
print(raw)
print(len(raw))

print(text.encode('utf-8'))
print(raw.decode('utf-8'))
print(text.encode('utf-16'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 126.
X = set('spam')
Y = {'h', 'a', 'm'}
print(X, Y)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 126.
mySet = set(str('pallavi'))
mySet1 = set('punit')
print(mySet)
print(mySet & mySet1)
print(mySet - mySet1)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 127.
{n ** 2 for n in [1, 2, 3, 4]}	# Set comprehension.
# print(list(set('pallavi')))
print(set('spam') == set('asmp'))	# Order-neutral equality test.
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 127.
import decimal

d = decimal.Decimal('3.141')
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 127.
from fractions import Fraction

myFraction = Fraction(1, 4)
print(myFraction + 1)
print(myFraction + Fraction(1, 2))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 128.
print(bool('spam'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 128.
variable = None
print(variable)
L = [None] * 100
print(L)
print(type(L))
print(type(type(L)))
if type(L) == type([]):	# Type testing.
	print('yes')
print(type('a'))
print(type(type('a')))
myList = []
if type(myList) == list:
	print('type function output matches type name (as keyword)')
if isinstance(myList, list):	# OO test.
	print('isInstance working')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 129.
class Lovers:
	def __init__(self, name, salary):	# Initialize when created.
		self.name = name
		self.salary = salary
	def giveHike(self, percent):
		self.salary += self.salary * percent / 100
	def getLastName(self):
		return self.name.split()[-1]

pallaviArya = Lovers('Pallavi Arya', 1000)
punitArya = Lovers('Punit Kumar Arya', 1000)
print(punitArya.getLastName())
print(pallaviArya.giveHike(20))
print(pallaviArya.salary)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 140.
print(int(3.1415))
print(float(3))	# Converts to float.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 144.
print(repr('spam'))
print(str('spam'))
print(str(b'xy', 'utf8'))	# Alternative to 'bytes.decode' method.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 145.
X = 2
Y = 4
Z = 6

print(X < Y < Z)	# Range test.
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y and Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print(1 == 2 < 3)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 145.
print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 151.
print(1j * 1J)
print(2 + 1j * 3)
print((2 + 1j) * 3)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 152.
print(oct(64), hex(64), bin(64))
print(64, 0o100, 0x40, 0b1000000)
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b10000000', 2))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 152.
print('{0:0}, {1:x}, {2:b}'.format(64, 64, 64))	# Returns digits not strings.
print('%o, %x, %x, %X' % (64, 64, 255, 255))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 154.
X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 155.
import math

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
print(abs(-42.0), sum((1, 2, 3, 4)))	# Summation.
print(min(3, 1, 2, 4), max(3, 1, 2, 4))
print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(round(2.567), round(2.467), round(2.567, 2))
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))
print((1 / 3.0), round(1 / 3.0, 2), ('%.2f' % (1 / 3.0)))
print(math.sqrt(144))
print(144 ** .5)
print(pow(144, .5))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 151.
print(hex(15))
print(bin(15))
print(int('0b1111', 2))
myComplex = complex(2, 3)
print(myComplex)
myFloat = 25.
print(myFloat.as_integer_ratio())
if myFloat.is_integer():
	print('yes integer')
myInteger = 5
print(myInteger.bit_length())
print('OK' if False else True)
print('OK' if False else 'NOK')
print('not in' if 's' not in 'spam' else 'in')
myList2 = myList = [1]
print('yes' if myList is not myList2 else 'not')
print('abcdefghi'[1:-1:2])
myString = 'abcdefghi'
myString2 = myString[slice(1, 2, -1)]
print(myString2)
myDictionary = {'key3': 'value1', 'key2': 'value2', 'key1': 'value3'}
print(sorted(myDictionary.items()))
print(int(3.14), int(3.54), int(3.84))
print(float(3))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 152.
myCode = 'print(oct(8))'
eval(myCode)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 152.
print('{0:o}, {1:x}, {2:b}'.format(16, 16, 16))
print('%o, %x, %X' % (15, 15, 15))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 156.
import random

print(random.randint(1, 10))
print(random.randint(1, 10))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 156.
import random

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(suits)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 158.
print(0.1 + 0.1 + 0.1 - 0.3)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 158.
import decimal

print(decimal.Decimal.from_float(1.25))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 158.
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 159.
import decimal

print(decimal.Decimal(1) / decimal.Decimal(7))	# Default: 28 digits.
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 159.
with decimal.localcontext() as ctx:
	ctx.prec = 2
	print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 160.
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x + y)
print(x - y)
print(x * y)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 160.
print(Fraction('.25'))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  P. 162.
import fractions

print(fractions.Fraction('0.25'))
myDecimal = 0.25
print(fractions.Fraction(*myDecimal.as_integer_ratio()))
print(fractions.Fraction(*(0.25).as_integer_ratio()))
myFraction = fractions.Fraction(4 / 3)
print(myFraction.limit_denominator(3))

print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))

print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())	# '*' converts a tuple in to individual arguments.
print(z)
print(float(z))
print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))
print(x + 2)	# 'Fraction' + 'int' -> 'Fraction'
print(x + 2.0)	# 'Fraction' + 'float' -> 'float'
print(x + Fraction(4, 3))	# 'Fraction' + 'Fraction' -> 'Fraction'
a = x + Fraction(*(4.0 / 3).as_integer_ratio())
print(a)
print(a.limit_denominator(10))

x = set('abcde')
y = set('bdxyz')
z = x.intersection(y)	# Same as 'x & y'.
print(z)
print(z.add('SPAM'))
print(z.update(set(['X', 'Y'])))	# Merge, i.e., in-place union.
print(z.remove('b'))

for item in set('abc'):
	print(item * 3)

S = set([1, 2, 3])
print(S | set([3, 4]))
# print(S | [3, 4])
print(S.union([3, 4]))
print(S.issubset(range(-5, 5)))

S1 = {1, 2, 3, 4}
print(S1 - {1, 2, 3, 4})
print(type({}))
S = set()	# Initialize an empty set.
print(S.add(1.23))
print({1, 2, 3}.union([3, 4]))

print(set(dir(bytes)) - set(dir(bytearray)))
print(set(dir(bytearray)) - set(dir(bytes)))

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)	# Order matters in sequence.
print(set(L1) == set(L2))	# It doesn't in sets.
print(sorted(L1) == sorted(L2))

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

print(engineers > managers)
print((managers | engineers) - (managers ^ engineers))	# Intersection.

print(type(True))
print(isinstance(True, int))
print(True == 1)
print(True is 1)
print(True + 4)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 183.
# mySet = {1, 2, 3, 3}
# print(mySet)
# copyOfMySet = mySet.copy()
# print(copyOfMySet)
# copyOfCopyOfMySet = set(copyOfMySet)
# print(copyOfCopyOfMySet)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 183.
# import copy
#
# mySet = [1, 2, (1, 2, [1, 2, (1, 2, [1, 2])])]
# print(mySet)
# copyOfMySet = copy.copy(mySet)
# print(copyOfMySet)
# copyOfCopyOfMySet = copy.deepcopy(mySet)
# print(copyOfCopyOfMySet)
# copyOfcopyOfCopyOfMySet = mySet.copy()
# print(copyOfcopyOfCopyOfMySet)
# print(len(mySet))
# copyOfMySet = copy.copy(mySet)
# print(len(copyOfMySet))
# copyOfCopyOfMySet = copy.deepcopy(mySet)
# print(len(copyOfCopyOfMySet))
# copyOfcopyOfCopyOfMySet = mySet.copy()
# print(len(copyOfcopyOfCopyOfMySet))
# print(type(mySet[2]))
# print(type(mySet[2][2]))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p.193.
# print('knight\'s', "knight\"s")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 197.
# path = r'C:\new\text.dat'
# print(path)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 226.
# print(hex(255))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# LP5.  p. 255.
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))
print(D.get('spam'))
print(D.get('toast'))
print(D.get('toast', 88))


# LP5.  p. 289.
# allTheFile = open('../var/in.txt', encoding = 'utf-8')
# print(len(allTheFile.read()))
# for line in open('../var/in.txt'):
# 	print(line.rstrip())
# 	words = line.split()
# 	print(words)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# http://urwid.org/tutorial/index.html
# import urwid

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# txt = urwid.Text(u"Hello World")
# fill = urwid.Filler(txt, 'top')
# loop = urwid.MainLoop(fill)
# loop.run()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# http://urwid.org/tutorial/index.html
# import urwid
#
# def exit_on_q(key):
# 	if key in ('q', 'Q'):
# 		raise urwid.ExitMainLoop()
#
# palette = [('banner', 'black', 'light gray'), ('streak', 'black', 'dark red'), ('bg', 'black', 'dark blue'), ]
#
# txt = urwid.Text(('banner', u" Hello World "), align = 'center')
# map1 = urwid.AttrMap(txt, 'streak')
# fill = urwid.Filler(map1)
# map2 = urwid.AttrMap(fill, 'bg')
# loop = urwid.MainLoop(map2, palette, unhandled_input = exit_on_q)
# loop.run()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import matplotlib.style as mplstyle
#
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
# plt.figure(1, figsize=(9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import math

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# print(log2(1024))
# print(2 ** 31)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import sys
#
# try:
#     f = open('../var/in.txt')
#     for line in f:
#	  print(line.strip())
#	  print(int(line.strip()))
# except IOError as e:
#     print('I/O Error ({0}): {1})'.format(e.errno, e.strerror))
# #    print(sys.exc_info()[0])
# # except ValueError:
# #	print("Could not convert data to an integer.")
# except:
#     print('Unexpected error:', sys.exc_info()[0])
#     print(sys.exc_info())
#     print(type(sys.exc_info()))
#     raise

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import _thread as thread, time
# import os

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# def counter(myId, count):
#	for i in range(count):
#		print('Thread ID: %s.  i: %s.' % (myId, i))
#		time.sleep(2)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# print('Main thread running.')
# for i in range(5):
#	thread.start_new_thread(counter, (i, 5))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# time.sleep(12)
# print('Main thread exiting.')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN [OLD VERSION OF TUTORIAL PROBABLY]
# import _thread as thread
# import time
# import zipfile

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# def asyncZip(infile, outfile):
#	print('Background thread started.')
#	with zipfile.ZipFile(outfile, 'w') as myzip:
#		myzip.write(infile)
#	print('Background thread ended. ', infile)	# This thread is run in background (background thread).

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# print('Main thread started.')
# thread.start_new_thread(asyncZip, ('/home/punit/src/_not_mine/py3testbed/tmp/ChangeLog.org', '/home/punit/src/_not_mine/py3testbed/tmp/new.zip'))
# time.sleep(1)
# print('Main thread ended.')	# This is main thread, running simultaneously.

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import zipfile

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# with zipfile.ZipFile('/home/punit/src/_not_mine/py3testbed/tmp/ChangeLog.zip', 'w') as myzip:
#	myzip.write('/home/punit/src/_not_mine/py3testbed/tmp/ChangeLog.org')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import readline

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# print(readline.get_history_length())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# def merge_lists():
#	lengthList1 = input()
#	lengthList2 = input()
#	count = 0
#	list1 = list2 = list3 = []
#	while count < int(lengthList1):
#		list1.append(int(input()))
#	count = 0
#	while count < lengthList2:
#		list2.append(int(input()))
#
#	i = j = 0
#	while i < lengthList1 and j < lengthList2:
#		if int(list1[i]) < int(list2[j]):
#			list3.append(list1[i])
#			i += 1
#		else:
#			list3.append(list2[j])
#			j += 1
#
#	list3 = list3 + list1[i:] + list2[j:]
#
# if __name__ == '__main__':
#	merge_lists()

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import math
#
# print(math.pi)
# print(math.sqrt(-1))
# print(str(math.sqrt(10))[0])
# print(str(math.pi)[len(str(math.pi))-2])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print(len(list(myString)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print("%s, %s, and %s, ma'am" %('wham', 'bang', 'thank you'))
# print("{}, {}, and {}, ma'am".format('wham', 'bang', 'thank you'))
# print('{:,.2f} and {:+04d}'.format(3000.14159, 3))
# print('%+04d and %.3f' %(3, 30.300999))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print(list('????'.encode('utf-8')))
# print(list('????'.encode('utf-16')))
# print(list('????'.encode('utf-32')))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import platform
#
# print(platform.version(), platform.release(), platform.python_version())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print('%e' % 31415.926)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print('Yes' if 1.1 + 2.3 == 3.3 else 'No')
# print((99999999999999999999999).bit_length() + 1)
# print(complex(2 + -3j) * 3)
# print(2 + -3j * 3)
#
# import cmath
# print(cmath.cos(complex(2, -3)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import math
#
# print(1 / math.e)
# print(math.sqrt(math.sin(math.pi / 2)))
# print(pow(2, 4))
# print(abs(-2))
# print(max(1, 2, 3, 4), min(1, 2, 3, 4))
# print(math.floor(-2.1))
# print(math.trunc(-2.1))
# print(round(-2.1111, 2))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# mySet1 = set('mySet1')
# mySet2 = set('mySet2')
# mySet1 = mySet1.intersection(mySet2)
# print(mySet1)
# mySet1.add('sets')
# print(mySet1)
# mySet2.update(['m', 'y', 'S', 'e', 't', '3'])
# print(mySet2)
# mySet2.update('mySet4')
# print(mySet2)
# mySet2 = mySet2.union('mySet1')
# print(mySet2)
# print('yes subset' if {1, 2, 3, 9}.issubset(range(10)) else 'not a subset')
# print(dir(mySet2))
# myList = [1, 2, 3, 4, 5, 4, 3, 2]
# myList = list(set(myList))
# print(myList)
# print(set([1, 3, 5]) - set([1, 2, 3, 4, 5]))
# print(set(dir(str)) - set(dir(bytes)))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# print(True + 4)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# list1 = [1, 2, 3]
# list2 = list1
# list2[2] = 4
# print(list1)
# list2 = list1[:]
# list2[2] = 5
# print(list1, list2)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# import sys

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')

# print(sys.argv[0], len(sys.argv[0]))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# a = 14
# b = 21
# if (a // b) * b + (a % b) == a:
#	print("True")

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN
# for x in range(2, 10):
#	if x < 5:
#		print(x)
#	else:
#		break
# else:
#	print('all less than 5 printed')

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
num = [4, 3, 1, 2]
num.sort()
print(num)
num.shuffle()
print(num)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
ab = [(20, 21), (11, 10), (00, 40)]
ab.sort(key = 2)
ab.sort(key = 1)
ab.sort(key = lambda mykey : mykey[1])
print(ab)

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
print(fruits.reverse())
print(fruits)
print(fruits.append('grape'))
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.pop())

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
row1 = ['00', '01', '02']
row2 = ['10', '11', '12']
matrix = [row1, row2]
print(matrix)
print(matrix[0][1])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
print([1, 2] < [2, 1])

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')


# UNKNOWN:
import decimal

print('Decimal is fixed-precision unlike floating-points' if decimal.Decimal('1.11') + decimal.Decimal('2.22') == decimal.Decimal('3.33') else 'it\'s not')
print(decimal.Decimal.from_float(1.11))

print('\n', '-' * 4, ' ', getframeinfo(currentframe()).lineno, ' ', '-' * 4, '\n', sep='')
