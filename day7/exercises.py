# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Meta", "YC combinator", "Netflix"])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
# What is the difference between remove and discard
    # remove() will raise an Error => KeyError if not the item not found
    # discard() wouldn't raise any error

# Exercises: Level 2
# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
print(A | B)
print(B | A)
# What is the symmetric difference between A and B
print(A ^ B)
# Delete the sets completely
del A
del B
del it_companies
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    # the age list is bigger
print(len(age))
st = set(age)
print(len(st))
# Explain the difference between the following data types: string, list, tuple and set
    # str => sequence of character, indexed and ordered and mutable
    # list => collection of different elements of different datatypes, ordered and indexed and mutable
    # tuple => collection of different elements of different datatypes, ordered and indexed and immutable
    # set => collection of different elements of different datatypes, unordered and unindexed and only unique values
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
un = 'I am a teacher and I love to inspire and teach people'.split(" ")
print(un)
unique_words = set(un)
print(unique_words)