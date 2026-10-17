from functools import reduce
# function as a param
# def add(nums):
#     return sum(nums)

# def higher_order_function(func, lst):
#     summation = func(lst)
#     return summation

# result = higher_order_function(add, [3,4,5,6])
# print(result)

# function as a return value
# def square(x):
#     return x ** 2
# def cube(x):
#     return x ** 3
# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def higher_order_func(type):
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube
#     elif type == "absolute":
#         return absolute

# res = higher_order_func("square")
# print(res(3))
# res = higher_order_func("cube")
# print(res(3))
# res = higher_order_func("absolute")
# print(res(-3))

# python closures
# def add_five():
#     five = 5
#     def add(num):
#         return five + num
#     return add
# # add_five() will return add(num) and add(num) needs num arg
# result = add_five()
# print(result(7))

# python decrator
# def uppercase_decorator(ff):
#     def wrapper():
#         func = ff()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# @uppercase_decorator 
# def greeting():
#     return "barhoomz"
# print(greeting())

# multiple decorator to single function
# def upper_case_decorator(func):
#     def wrapper():
#         arg_func = func()
#         upper_case_result = arg_func.upper()
#         return upper_case_result
#     return wrapper

# def split_decorator(func):
#     def wrapper():
#         arg_func = func()
#         splitted_result = arg_func.split()
#         return splitted_result
#     return wrapper

# @split_decorator
# @upper_case_decorator
# def greeting():
#     return "Welcome To my Livestream"
# print(greeting())

# accepting params in decorators
# def decorator_with_params(func):
#     def wrapper(arg1, arg2, arg3):
#         func(arg1, arg2, arg3)
#         print(f"I live in {arg3}")
#     return wrapper

# @decorator_with_params
# def full_name(first, last, country):
#     print(f"I am {first} {last}. I love Coding.")

# full_name("Ibrahim", "Hussain", "Somalia")

# map function -> takes a function and iterable
# nums = [1,2,3,4,5,6,7,8,9]
# cubed_nums = map(lambda x: x ** 2, nums)
# print(nums)
# print(list(cubed_nums))

# filter function -> filters items of list based on the given criteria
# nums = [1,2,3,4,5,6,7,8,9,10]
# evens = filter(lambda x: x % 2 == 0, nums)
# odds = filter(lambda x: x % 2 != 0, nums)
# print("Even numbers: ", list(evens))
# print("Odd numbers: ", list(odds))

# names = ["Ibrahim", "Hussain", "Hassan", "Ali"]
# short_names = filter(lambda name: not len(name) > 5, names)
# long_names = filter(lambda name: len(name) > 5, names)
# print(list(long_names))
# print(list(short_names))

# reduce function -> it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value
# subjects_grades = [90, 92, 77, 81, 83]
# result = reduce(lambda x, y: x + y, subjects_grades)
# print("Your Average is:", result / len(subjects_grades))