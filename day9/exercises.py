# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
    # user_age = int(input("Enter your age: "))
    # required_age = 18
    # if user_age >= required_age:
    #     print("You are old enough to learn to drive.")
    # else:
    #     print(f"You need {required_age - user_age} more years to learn to drive.")
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    # my_age = 23
    # your_age = int(input("Enter your age: "))
    # if my_age < your_age:
    #     if your_age - my_age == 1:
    #         print(f"You are {your_age - my_age} year older than me.")
    #     else:
    #         print(f"You are {your_age - my_age} years older than me.")
    # elif my_age > your_age:
    #     if my_age - your_age == 1:
    #         print(f"You are {my_age - your_age} year younger than me.")
    #     else:
    #         print(f"You are {my_age - your_age} years younger than me.")
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
    # a = int(input("Enter number one: "))
    # b = int(input("Enter number two: "))
    # if a > b:
    #     print(f"{a} is greater than {b}")
    # elif a < b:
    #     print(f"{a} is smaller than {b}")
    # else:
    #     print(f"{a} is equal to {b}")
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores
# grade = int(input("Enter your grade: "))
# if grade >= 90 and grade <= 100:
#     print("A")
# elif grade >= 80 and grade <= 89:
#     print("B")
# elif grade >= 70 and grade <= 79:
#     print("C")
# elif grade >= 60 and grade <= 69:
#     print("D")
# elif grade < 60:
#     print("F")
# else:
#     print("Invalid grade")
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# user_month = input("Enter month: ").title()
# seasons = ["Autumn", "Winter", "Spring", "Summer"]
# if user_month == "September" or user_month == "October" or user_month == "November":
#     print("Autumn")
# elif user_month == "December" or user_month == "January" or user_month == "February":
#     print("Winter")
# elif user_month == "March" or user_month == "April" or user_month == "May":
#     print("Spring")
# elif user_month == "June" or user_month == "July" or user_month == "August":
#     print("Summer")
# else:
#     print("Invalid month")
# The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']
    # prompt = input("enter fruit: ")

    # if not prompt.lower() in fruits:
    #     fruits.append(prompt)
    #     print(fruits)
    # else:
    #     print('That fruit already exist in the list')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# import math
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# if 'skills' in person:
#     print("exsist", f"{person["skills"][math.floor(len(person['skills']) / 2)]}")
# #  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# if 'skills' in person and 'Python' in person['skills']:
#     print(person['skills'][-1])
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ('JavaScript' and 'React' in person['skills']) and len(person['skills']) == 2:
    print("He is a front end developer")
elif ('Node' and 'Python' and 'MongoDB' in person['skills']) and len(person['skills']) == 3:
    print("He is a backend developer")
elif ('Node' and 'React' and 'MongoDB' in person['skills']) and len(person['skills']) > 2:
    print("He is a fullstack developer")
else:
    print("unknown title")
#  * If the person is married and if he lives in Finland, print the information in the following format
if person['is_married'] and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")