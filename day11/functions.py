# def name():
#     first_name = "Ibrahim"
#     last_name = "Hussain"

#     print(f"{first_name} {last_name}")

# name()

# def sum():
#     x = 8
#     y = 3
#     return x + y

# z = sum()
# print(z)

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(44,55,66,77,88,99,110))

# def teams(team, *members):
#     print(team)
#     for member in members:
#         print(member)

# teams("Arsenal", "BArhoomz", "Rice", "Saka", "Gyokeres")

def student(name, id):
    print(f"Your name is {name}, your ID is {id}")

students_details = {"name": "Ibrahim Hussain", "id": 4282}

student(**students_details)

def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27