# Iterate 0 to 10 using for loop, do the same using while loop.
    # for i in range(11):
    #     print(i)

    # n = 0
    # while n < 11:
    #     print(n)
    #     n += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
    # nums = [10,9,8,7,6,5,4,3,2,1,0]
    # for i in nums:
    #     print(i)

    # n = 10
    # while n >= 0:
    #     print(n)
    #     n -= 1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
    # for x in range(7):
    #     for _ in range(1+x):
    #         print("#", end='')
    #     print()

# Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

    # for _ in range(8):
    #     for _ in range(8):
    #         print("# ",end='')
    #     print()

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
    # for x in range(11):
    #     print(f"{x} x {x} = {x*x}")
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
    # pythonic_items = ['Python', 'Numpy','Pandas','Django', 'Flask']
    # for item in pythonic_items:
    #     print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
    # for i in range(101):
    #     if i % 2 == 0:
    #         print(i)
# Use for loop to iterate from 0 to 100 and print only odd numbers
    # for i in range(101):
    #     if i % 2 != 0:
    #         print(i)
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    # sum = 0
    # for i in range(101):
    #     sum += i
    # print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    # even = 0
    # odd = 0
    # for i in range(101):
    #     if i % 2 == 0:
    #         even += i
    #     if i % 2 != 0:
    #         odd += i
    # print(f"The sum of all evens is {even}")
    # print(f"The sum of all odds is {odd}")
# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing 
# the word land.
    # countries = [
    #   'Afghanistan',
    #   'Albania',
    #   'Algeria',
    #   'Andorra',
    #   'Angola',
    #   'Antigua and Barbuda',
    #   'Argentina',
    #   'Armenia',
    #   'Australia',
    #   'Austria',
    #   'Azerbaijan',
    #   'Bahamas',
    #   'Bahrain',
    #   'Bangladesh',
    #   'Barbados',
    #   'Belarus',
    #   'Belgium',
    #   'Belize',
    #   'Benin',
    #   'Bhutan',
    #   'Bolivia',
    #   'Bosnia and Herzegovina',
    #   'Botswana',
    #   'Brazil',
    #   'Brunei',
    #   'Bulgaria',
    #   'Burkina Faso',
    #   'Burundi',
    #   'Cabo Verde',
    #   'Cambodia',
    #   'Cameroon',
    #   'Canada',
    #   'Central African Republic',
    #   'Chad',
    #   'Chile',
    #   'China',
    #   'Colombia',
    #   'Comoros',
    #   'Congo, Democratic Republic of the',
    #   'Congo, Republic of the',
    #   'Costa Rica',
    #   "Côte d'Ivoire",
    #   'Croatia',
    #   'Cuba',
    #   'Cyprus',
    #   'Czech Republic',
    #   'Denmark',
    #   'Djibouti',
    #   'Dominica',
    #   'Dominican Republic',
    #   'East Timor (Timor-Leste)',
    #   'Ecuador',
    #   'Egypt',
    #   'El Salvador',
    #   'Equatorial Guinea',
    #   'Eritrea',
    #   'Estonia',
    #   'Eswatini',
    #   'Ethiopia',
    #   'Fiji',
    #   'Finland',
    #   'France',
    #   'Gabon',
    #   'Gambia',
    #   'Georgia',
    #   'Germany',
    #   'Ghana',
    #   'Greece',
    #   'Grenada',
    #   'Guatemala',
    #   'Guinea',
    #   'Guinea-Bissau',
    #   'Guyana',
    #   'Haiti',
    #   'Honduras',
    #   'Hungary',
    #   'Iceland',
    #   'India',
    #   'Indonesia',
    #   'Iran',
    #   'Iraq',
    #   'Ireland',
    #   'Israel',
    #   'Italy',
    #   'Jamaica',
    #   'Japan',
    #   'Jordan',
    #   'Kazakhstan',
    #   'Kenya',
    #   'Kiribati',
    #   'Korea, North',
    #   'Korea, South',
    #   'Kuwait',
    #   'Kyrgyzstan',
    #   'Laos',
    #   'Latvia',
    #   'Lebanon',
    #   'Lesotho',
    #   'Liberia',
    #   'Libya',
    #   'Liechtenstein',
    #   'Lithuania',
    #   'Luxembourg',
    #   'Madagascar',
    #   'Malawi',
    #   'Malaysia',
    #   'Maldives',
    #   'Mali',
    #   'Malta',
    #   'Marshall Islands',
    #   'Mauritania',
    #   'Mauritius',
    #   'Mexico',
    #   'Micronesia',
    #   'Moldova',
    #   'Monaco',
    #   'Mongolia',
    #   'Montenegro',
    #   'Morocco',
    #   'Mozambique',
    #   'Myanmar',
    #   'Namibia',
    #   'Nauru',
    #   'Nepal',
    #   'Netherlands',
    #   'New Zealand',
    #   'Nicaragua',
    #   'Niger',
    #   'Nigeria',
    #   'North Macedonia',
    #   'Norway',
    #   'Oman',
    #   'Pakistan',
    #   'Palau',
    #   'Palestine',
    #   'Panama',
    #   'Papua New Guinea',
    #   'Paraguay',
    #   'Peru',
    #   'Philippines',
    #   'Poland',
    #   'Portugal',
    #   'Qatar',
    #   'Romania',
    #   'Russia',
    #   'Rwanda',
    #   'Saint Kitts and Nevis',
    #   'Saint Lucia',
    #   'Saint Vincent and the Grenadines',
    #   'Samoa',
    #   'San Marino',
    #   'Sao Tome and Principe',
    #   'Saudi Arabia',
    #   'Senegal',
    #   'Serbia',
    #   'Seychelles',
    #   'Sierra Leone',
    #   'Singapore',
    #   'Slovakia',
    #   'Slovenia',
    #   'Solomon Islands',
    #   'Somalia',
    #   'South Africa',
    #   'South Sudan',
    #   'Spain',
    #   'Sri Lanka',
    #   'Sudan',
    #   'Suriname',
    #   'Sweden',
    #   'Switzerland',
    #   'Syria',
    #   'Tajikistan',
    #   'Tanzania',
    #   'Thailand',
    #   'Togo',
    #   'Tonga',
    #   'Trinidad and Tobago',
    #   'Tunisia',
    #   'Turkey',
    #   'Turkmenistan',
    #   'Tuvalu',
    #   'Uganda',
    #   'Ukraine',
    #   'United Arab Emirates',
    #   'United Kingdom',
    #   'United States',
    #   'Uruguay',
    #   'Uzbekistan',
    #   'Vanuatu',
    #   'Vatican City',
    #   'Venezuela',
    #   'Vietnam',
    #   'Yemen',
    #   'Zambia',
    #   'Zimbabwe'
    # ];
    # for country in countries:
    #     if 'land' in country:
    #         print(country)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    # fruits = ['banana', 'orange', 'mango', 'lemon']
    # for fruit in sorted(fruits, reverse=True):
    #     print(fruit)
# Go to the data folder and use the countries_data.py file.
# from countries_data import cd
# What are the total number of languages in the data
    # total_langs = 0
    # for c in countries_data:
    #     for x in c["languages"]:
    #         total_langs += 1
        # print(f"{x}")
    # print(total_langs)
# Find the ten most spoken languages from the data
    # langs = []
    # for i in cd:
    #     for x in i["languages"]:
    #         langs.append(x)
    # lang_and_num = {}
    # for c in langs:
    #     lang_and_num[c] = langs.count(c)
    # res = sorted(lang_and_num.items(), key=lambda item: item[1], reverse=True)[:10]
    # for x in res:
    #     print(x)
# Find the 10 most populated countries in the world
    # countries_and_population = {}
    # for countries in cd:
    #     countries_and_population[countries["name"]] = countries["population"]

    # res = sorted(countries_and_population.items(), key=lambda item: item[1], reverse=True)[:10]
    # print(res)

