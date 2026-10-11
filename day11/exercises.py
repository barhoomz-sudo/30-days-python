# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers(a, b):
#     return a + b
# print(add_two_numbers(9, 2))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    # def area_of_circle(r):
    #     print(3.14 * r * r)
    # area_of_circle(5)
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    # def all_nums(*nums):
    #     total = 0
    #     for num in nums:
    #         if int(num) or float(num):
    #             total += num
    #         else:
    #             print("argument not a number!")
    #             break
    #     print(total)
    # all_nums(8,8,4.4)
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    # def convert_celsius_to_fahrenheit(c):
    #     f = c * (9/5) + 32
    #     return f
    # print(convert_celsius_to_fahrenheit(32))
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    # def check_season(month):
    #     autumn = ["september", "october", "november"]
    #     winter = ["december", "january", "february"]
    #     spring = ["march", "april", "may"]
    #     summer = ["june", "july", "august"]

    #     if month in autumn:
    #         return "Autumn"
    #     elif month in winter:
    #         return "Winter"
    #     elif month in spring:
    #         return "Spring"
    #     else:
    #         return "Summer"

    # print(check_season("june"))
# Write a function called calculate_slope which return the slope of a linear equation
    # y2-y1 / x2 - x1
    # def calculate_slope(y2,y1,x2,x1):
    #     return (y2-y1) / (x2-x1)
    # print(calculate_slope(8,9,0,1))
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    # def solve_quadratic_eqn(x):
    #     a = 5
    #     b = 2
    #     c = 7

    #     qe = a * x**2 + b*x + c
    #     return qe
    # print(solve_quadratic_eqn(3))
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    # def print_list(ls):
    #     for ele in ls:
    #         print(ele)
    # print_list(["hello", "world", "!"])
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
    # def reverse_list(ls):
    #     rv_ls = []
    #     for i in sorted(ls, reverse=True):
    #         rv_ls.append(i)
    #     print(rv_ls)

    # reverse_list([1,2,3,4,5])
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    # def capitalize_list_items(ls):
    #     caps_ls = []
    #     for item in ls:
    #         caps_ls.append(item.upper())
    #     return caps_ls
    # print(capitalize_list_items(["ibrahim", "hussain", "hassan"]))
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
    # def add_item(ls, item):
    #     ls.append(item)
    #     return ls
    # print(add_item(["tomato", "potato", "carrot"], "salad"))
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def remove_item(ls, item):
#     ls.remove(item)
#     return ls
# print(remove_item([1,2,3,4,5], 1))
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
    # def sum_of_numbers(num):
    #     sum = 0
    #     for n in range(num+1):
    #         sum += n
    #     return sum
    # print(sum_of_numbers(100))
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    # def sum_of_odds(num):
    #     sum = 0
    #     for n in range(num+1):
    #         if n % 2 != 0:
    #             sum += n
    #     return sum
    # print(sum_of_odds(100))
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
    # def sum_of_evens(num):
    #     sum = 0
    #     for n in range(num+1):
    #         if n % 2 == 0:
    #             sum += n
    #     return sum
    # print(sum_of_evens(100))
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # def evens_and_odds(n):
    #     even = 0
    #     odd = 0
    #     for i in range(n+1):
    #         if i % 2 == 0:
    #             even += 1
    #         elif i % 2 != 0:
    #             odd += 1
    #     return f"The number of odds are {odd}.\nThe number of evens are {even}."
    # print(evens_and_odds(100))
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    # def factorial(n):
    #     factor = 1
    #     for i in range(1, n+1):
    #         factor *= i
    #     return factor
    # print(factorial(5))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
    # def is_empty(arg):
    #     if arg:
    #         print("Not empty")
    #     else:
    #         print("Its empty")  
    # is_empty('')
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
nums = [2,4,6,8,7,8,9,9,8,9]
# print(nums)
    # def calculate_mean(ls):
    #     sum = 0
    #     for i in ls:
    #         sum += i
    #     mean = sum / len(ls)
    #     return mean
    # print(calculate_mean(nums))

    # def calculate_median(ls):
    #     sorted_ls = sorted(ls)
    #     count_ls = len(ls)
    #     position = 0
    #     if count_ls % 2 != 0:
    #         position = round(count_ls // 2)
    #         return sorted_ls[position]
    #     if count_ls % 2 == 0:
    #         position = int(count_ls / 2)
    #         print(position)
    #         add_two_mid = sorted_ls[position - 1] + sorted_ls[position]
    #         divide_result = add_two_mid / 2
    #         return divide_result
            
    # print(calculate_median(nums))

# def calculate_mode(ls):
#     dict = {}
#     for i in ls:
#         dict[i] = ls.count(i)
#     res = dict.items()

#     f_count = []
#     for x in res:
#         f_count.append(x[1])
#     sorted_f_count = sorted(f_count, reverse=True)
#     top_num = sorted_f_count[0]
#     modes = []
#     for n in res:
#         if n[1] == top_num:
#             modes.append(n[0])
#     print(modes)
# calculate_mode(nums)

    # def calulate_range(ls):
    #     sorted_ls = sorted(ls)
    #     least = sorted_ls[0]
    #     greatest = sorted_ls[-1]
    #     range = greatest - least
    #     print(range)
    # calulate_range(nums)

    # def calculate_variance(ls):
    #     total = 0
    #     count = len(ls)
    #     for i in ls:
    #         total += i
        
    #     mean = total / count
    #     subtracted_from_mean = []
    #     for n in ls:
    #         subtracted_from_mean.append(n - mean)
    #     squared_result = []
    #     for j in subtracted_from_mean:
    #         squared_result.append(j**2)
    #     sum_squared = 0
    #     for k in squared_result:
    #         sum_squared += k

    #     return sum_squared / (count - 1)
    # print(calculate_variance(nums))

    # def calculate_std(ls):
    #     count = len(ls)
    #     total = 0
    #     for n in ls:
    #         total += n

    #     mean = total / count
    #     print(mean)

    #     subtracted_from_mean = []
    #     for i in ls:
    #         subtracted_from_mean.append((i - mean)**2)

    #     sum_of_squares = 0
    #     for k in subtracted_from_mean:
    #         sum_of_squares += k
    #     divide_by_n1 = sum_of_squares / (count - 1)
    #     return divide_by_n1 ** 0.5
    # print(calculate_std(nums))
# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
    # def greet(name = "Guest"):
    #     return f"Hello, {name}!"
    # print(greet())
    # print(greet("Ibrahim"))
# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
    # def show_args(name="Jhon Doe", age=33, city="New York"):
    #     return f"name: {name}, age: {age}, city: {city}"
    # print(show_args())
    # print(show_args("Ibrahim", 23, "Mogadisu"))
# Write a function called is_prime, which checks if a number is prime.
    # def is_prime(n):
    #     if n < 2:
    #         return "not a prime"

    #     if (str(n) != str(2) and str(n) != str(5)) and str(n).endswith(("0","2","4","6","8","5")):
    #         return "not a prime"

        
    #     sqrt = n ** 0.5
    #     for i in range(3, int(sqrt)+1, 2):
    #         if n % i == 0:
    #             return "not a prime!"
    #     return "prime!"
    # print(is_prime(2)) #prime
    # print(is_prime(3)) #prime
    # print(is_prime(5)) #prime
    # print(is_prime(7)) #prime
    # print(is_prime(17)) #prime
    # print(is_prime(4)) #not prime
    # print(is_prime(10)) #not prime
    # print(is_prime(25)) #not prime
    # print(is_prime(86)) #not prime
# Write a functions which checks if all items are unique in the list.
    # def are_unique(ls):
    #     for item in ls:
    #         if ls.count(item) == 1:
    #             return "items in the list are unique"
    #         else:
    #             return "not unique"
    # fruits = ["orange", "apple", "banana"]
    # numbers = [1,2,3,4,5,6,7,8,9,10]
    # print(are_unique(fruits))
    # print(are_unique(numbers))

# Write a function which checks if all the items of the list are of the same data type.
    # def check_type(ls):
    #     if len(ls) == 0:
    #         return "no data in list"

    #     if len(ls) == 1:
    #         return f"one item its type {type(ls[0])}"
        
    #     baseline = type(ls[0])

    #     for item in ls[1:]:
    #         if type(item) == baseline:
    #             # return "items matches the data type"
    #             continue
    #         else:
    #             return "items are not the same data type"
    #     return "items matches the data type"

    # fruits = ["orange", "banana", "apple", "cherry"]
    # # check_type(fruits)
    # print(check_type(["hh","uu","ss","jj"]))
# Write a function which check if provided variable is a valid python variable
    # def check_valid_var_name(var_name):
    #     if var_name.isidentifier():
    #         return "valid"  
    #     else:
    #         return "not valid"
    # print(check_valid_var_name("3hello"))
from countries_data import cd
#Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
    # def most_spoken_languages(ls):
    #     langs = []
    #     for i in ls:
    #         for x in i["languages"]:
    #             langs.append(x)
    #     lang_and_num = {}
    #     for c in langs:
    #         lang_and_num[c] = langs.count(c)
    #     res = sorted(lang_and_num.items(), key=lambda item: item[1], reverse=True)[:10]
    #     for x in res:
    #         print(x)
    # most_spoken_languages(cd)

# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(ls):
    countries_and_population = {}
    for countries in ls:
        countries_and_population[countries["name"]] = countries["population"]

    res = sorted(countries_and_population.items(), key=lambda item: item[1], reverse=True)[:10]
    print(res)
most_populated_countries(cd)