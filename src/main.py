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
#
# myClosure = encloseClosure()
# myClosure()
#
# print("\n", "-" * 4, " ", inspect.getframeinfo(inspect.currentframe()).lineno, " ", "-" * 4, "\n", sep = "")
