collection = list()
# print(collection)

#unpacking list
items = ["car", "keys", "phone", "watch", "coat", "airpods"]
item1, item2, item3, *rest = items
print(item1)
print(item2)
print(item3)
print(rest)
print(rest[1:])
print('coat' in rest)

# uu = []
# for i in range(10):
#     print(f"{i+1}.",end='')
#     u = input("add item: ")
#     uu.append(u)
# print(uu[-3])

fruits = ["Apple", "Orange", "Lime", "Cherry"]
print(fruits)
fruits.insert(0, "Banana")
print(fruits)
fruits.insert(-1, "Cantaloupe")
print(fruits)

fruits.remove("Lime")
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

del fruits[1]
print(fruits)
# del fruits
# print(fruits)
# fruits.clear()
# print(fruits)

fruits_copy = fruits.copy()
print(f"This is fruits: {fruits}")
print(f"This is fruits_copy: {fruits_copy}")

negative_nums = [-5, -4, -3, -2, -1]
zero = [0]
positive_nums = [1, 2, 3, 4, 5]
negative_nums.extend(zero)
negative_nums.extend(positive_nums)
integers = negative_nums.copy()
print(integers)
print(integers.count(0))

print(integers.index(-2))
integers.reverse()
print(integers)

# integers.sort()
# print(integers)

sorted(integers)
print(integers)