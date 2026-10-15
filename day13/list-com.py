# lst = [i for i in range(10)]
# print(lst)
# print(type(lst))

# lst2 = [(i, i + 1) for i in range(10)]
# print(lst2)

# even_numbers = [i for i in range(10) if i % 2 == 0]
# print(even_numbers)

# list_of_list = [[1,2,3], [4,5,6], [7,8,9]]
# flattened_lst = [num for i in list_of_list for num in i]
# print(flattened_lst)

# add = lambda x, y: x + y
# print(add(2,3))

# print((lambda a, s: a - s)(3,2))
def power(x):
    return lambda y: x ** y

print(power(7)(2))