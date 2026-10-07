st = set()

fruits = {"banana", "apple", "orange", "cherry"}
print(fruits)
fruits.add("lemon")
print(fruits)
fruits.update(["pineapple", "cantaloupe", "strawberrey"])
print(fruits)
# k = fruits.pop()
# print(k)
fruits.remove("cantaloupe")
print(fruits)
fruits.discard("blue berrey")

n1 = {1,2,3,4,5}
n2 = {6,7,8,9,10}
n3 = n1.union(n2) # n1 | n2
print(n3)

items1 = {"glasses", "notebook", "ring", "cup"}
items2 = {"cup", "laptop", "phone"}
matching_items = items1.intersection(items2) # items1 & items2
print(matching_items)
# is all the items in 'items1' are contained inside 'items2'
print(items1.issubset(items2))
print(items1.issuperset(items2))
print(items1.difference(items2))
print(items1.symmetric_difference(items2))
print(items1.isdisjoint(items2))