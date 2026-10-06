# Create an empty tuple
tpl = tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Alexander", "Jhon")
sisters = ("Lara", "Hana", "Yara")
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
# How many siblings do you have?
print(siblings)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.insert(0, "Gabriel")
family_members.insert(1, "Mona")
print(family_members)

# Unpack siblings and parents from family_members
father, mother, *siblings = family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "apple", "orange")
vegetables = ("cucumber", "tomato", "potato")
animal = ("rabbit", "cow", "camel")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(food_stuff_lt)
n = length // 2
print(food_stuff_lt[n:n+1])
# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)