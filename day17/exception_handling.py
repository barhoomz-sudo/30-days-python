# try:
#     print(11 + 'f')
# except:
#     print("Something went wrong")

# try:
#     name = input("name: ")
#     year_born = input("date of birth: ")
#     age = 2026 - int(year_born)
#     print(f"You are {name}. And your age is {age}.")
# except TypeError:
#     print("Type Error occur")
# except ValueError:
#     print("Value Error occur")
# else:
#     print(f"100\\% accurate code with 0 Errors!")
# finally:
#    print("Will always run, no matter what!")

# unpacking
# def add(a,b,c,d):
#     return a + b + c + d
# nums = [1,2,3,4]
# print(add(*nums))

# lst = [1, 11]
# nums = range(*lst)
# print(list(nums))

# def infos(name, country, city, age):
#     return f"my name is {name} and i live in {country}, {city}. and i am {age} years old"
# dt = {'name': "Ibrahim Hussain", 'country': "Somalia", 'city': "Mogadishu", 'age': 24}
# print(infos(**dt))

# packing
# def add(*args):
#     counter = 0
#     for num in args:
#         counter += num
#     return counter
# print(add(1,2))
# print(add(1,2,88))
# print(add(1,2, 1000, 222))

# def person(**infos):
#     for key in infos:
#         print(f"{key} {infos[key]}")
#     return infos

# print(person(name="Ibrahim", age="24"))

# spreading
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9]
# l3 = [0, *l1, *l2]
# print(l3)

# enumerate() -> gets index of items in list
# names = ["Ibrahim", "Hussain", "Hassan", "Ali"]
# for i, name in enumerate(names):
#     print(f"{name} is in index {i}")

# zip() -> combine lists when looping through them
# subjects = ["E", "Math", "Biology", "Somali Studies"]
# points = [89, 81, 95, 99]
# grades = []
# for subject, point in zip(subjects, points):
#     grades.append({"Subject": subject, "Result": point})
# print(grades)