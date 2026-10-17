#Filter only negative and zero in the list using list comprehension
    # numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    # neg_and_zero = [i for i in numbers if i <= 0]
    # print(neg_and_zero)
# Flatten the following list of lists of lists to a one dimensional list :
    # list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # res = [nums for row in list_of_lists for nums in row]
    # print(res)
# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
    # lst = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(10+1)]
    # print(lst)

# Flatten the following list to a new list:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
    # countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    # lst = [[cn.upper(),country[0][0][0:3].upper(),cc.upper()] for country in countries for cn,cc in country]
    # print(lst)
    
# Change the following list to a list of dictionaries:
    # countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    # lst = [{"country":cn,"city":cc.upper()} for country in countries for cn,cc in country]
    # print(lst)

# Change the following list of lists to a list of concatenated strings:
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
    # names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    # lst = [str(first+ " " +last) for name in names for first,last in name]
    # print(lst)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
    # slope_intercept = lambda m, x, y: y - m*x
    # print(slope_intercept(3, 2, 10))