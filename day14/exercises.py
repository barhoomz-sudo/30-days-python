from functools import reduce
from countries import countries as cc
from countries_data import cd
# Exercises: Level 1
# Explain the difference between map, filter, and reduce.
    # map -> iterates through the list applies the function to each item and returns a list
    # filter -> based on the function criteria/condition returns a list contins only what passed
    # reduce -> returns only one result of the iterable
# Explain the difference between higher order function, closure and decorator
    # higher order function -> function that takes another function as a param, or returns it
    # closure -> ability of a nested function to access outers scope
    # decorator -> design pattern in python to apply changes to an existed function without modifying it
# Define a call function before map, filter or reduce, see examples.
    # examples done in high_ord_func.py file
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use for loop to print each country in the countries list.
    # for country in countries:
    #     print(country)
# Use for to print each name in the names list.
    # for name in names:
    #     print(name)
# Use for to print each number in the numbers list.
    # for num in numbers:
    #     print(num)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
    # upper_case_countries = map(lambda country: country.upper(), countries)
    # print(list(upper_case_countries))
# Use map to create a new list by changing each number to its square in the numbers list
    # squared_numbers = map(lambda n: n**2, numbers)
    # print(list(squared_numbers))
# Use map to change each name to uppercase in the names list
    # names_in_caps = map(lambda name: name.upper(), names)
    # print(list(names_in_caps))
# Use filter to filter out countries containing 'land'.
    # filter_countries = filter(lambda country: 'land' in country, countries)
    # print(list(filter_countries))
# Use filter to filter out countries having exactly six characters.
    # countries_six = filter(lambda country: len(country) == 6, countries)
    # print(list(countries_six))
# Use filter to filter out countries containing six letters and more in the country list.
    # countries_six = filter(lambda country: len(country) >= 6, countries)
    # print(list(countries_six))
# Use filter to filter out countries starting with an 'E'
    # starts_with_e = filter(lambda cn: cn.startswith("E"), countries)
    # print(list(starts_with_e))
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    # minus_one_numbers = map(lambda x: x - 1, numbers)
    # print("minus one of each item in numbers",list(minus_one_numbers))
    # odds_only = filter(lambda x: x % 2 != 0, numbers)
    # print("filter out to get odd numbers only",list(odds_only))
    # sum_all = reduce(lambda a, b: a + b, numbers)
    # print("the result of adding odd numbers",sum_all)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
    # items = [1, "random", "car", ['book','shelf'], False]
    # string_items =filter(lambda item: isinstance(item, str), items)
    # print(list(string_items))
# Use reduce to sum all the numbers in the numbers list.
    # add_all = reduce(lambda a, b: a + b, numbers)
    # print(add_all)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    # def handle_cn(acc, cn):
    #     for cn in countries:
    #         if cn == countries[-1]:
    #             "and" + cn
    #     else:
    #         acc + ", " + cn

    # concat_countries = reduce(lambda acc, cn: acc + ", " +"and " + cn + " are north European countries" if cn == countries[-1] else acc + ", " + cn, countries)
    # print(concat_countries)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
    # def categorize_countries(ls, patterns):
    #     common_patterns = filter(lambda c: any(p in c for p in patterns), ls)
    #     return list(common_patterns)
    # print(categorize_countries(cc, ["ia", "island", "land", "stan"]))
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
    # def dt_names(ls):
    #     dt = {}
    #     for i in ls:
    #         first_letter = i[0]
    #         if first_letter in dt:
    #             dt[first_letter] += 1
    #         else:
    #             dt[first_letter] = 1
    #     return dt

    # print(dt_names(cc))
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
    # def get_first_ten(ls):
    #     return ls[0:10]
    # print(get_first_ten(cc))
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
    # def get_last_ten(ls):
    #     return ls[-10:]
    # print(get_last_ten(cc))

# Sort countries by name, by capital, by population
    # name = map(lambda n: n["name"], cd)
    # print(sorted(list(name)))
    # # Sort out the ten most spoken languages by location.
    # capital = map(lambda n: n["capital"], cd)
    # print(sorted(list(capital)))
    # # Sort out the ten most populated countries.
    # population = map(lambda n: n["population"], cd)
    # print(sorted(list(population)))