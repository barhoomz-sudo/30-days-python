me = {
    'first_name': "Ibrahim",
    'last_name': "Hussain",
    'age': 23,
    'country': "Somalia",
    'is_married': False,
    'skills': ["Python", "SQL", "Linux"],
    'address': {
        'street': "The multiverse down hill",
        'zipcode': "065787f"
    }
}

print(len(me))
# print(me)
print(me['first_name'])
print(me['skills'][2])
print(me.get("is_married"))
print('address' in me)
print(me.pop("last_name"))
# print(me)
# print(me.items())
print(me.keys())
print(me.values())