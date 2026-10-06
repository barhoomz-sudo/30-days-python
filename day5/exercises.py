# Declare an empty list
li = []
# Declare a list with more than 5 items
items = [1,2,3,4,5]
# Find the length of your list
print(len(items))
# Get the first item, the middle item and the last item of the list
print(items[0])
print(items[-1])
# mid_index = round(len(items) / 2)
# print(items[mid_index])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ibrahim Hussain", 23, 174, "Single", "Mogadishu, Yaaqshid"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
# Print the list after modifying one of the companies
it_companies[-2] = "Ali express"
print(it_companies)
# Add an IT company to it_companies
it_companies.append("Samsung")
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(4, "eBay")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))
# Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[:3])
# Slice out the last 3 companies from the list
print(it_companies[-3:])
# Slice out the middle IT company or companies from the list
print(it_companies[4:5])
# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.pop(3)
print(it_companies)
it_companies.pop(4)
print(it_companies)
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
print(min(sorted(ages)))
print(max(sorted(ages)))
# Add the min age and the max age again to the list
ages.append(min(sorted(ages)))
ages.append(max(sorted(ages)))
print(ages)
# Find the median age (one middle item or two middle items divided by two)
length = len(ages)
n = length // 2 # if its even then two middle items
first_middle_item = ages[n-1]
second_middle_item = ages[n]
print(first_middle_item)
print(second_middle_item)
# Find the average age (sum of all items divided by their number )
avg_age = sum(ages) // 2
print(avg_age)
# Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages) - avg_age))
print(abs(max(ages) - avg_age))
# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
countries_length = len(countries)
print(countries_length)
no = countries_length // 2
print(no)
print(countries[no])
# Divide the countries list into two equal lists 
# if it is even if not one more country for the first half.
first_half = countries[:98]
print(len(first_half))
second_half = countries[98:]
print(len(second_half))
# Unpack the first three countries and the rest as scandic countries.
ch, rs, us, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(ch)
print(rs)
print(us)
print(scandic_countries)