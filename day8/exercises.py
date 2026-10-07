# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "rayan"
dog['color'] = "black"
dog['breed'] = "dunno"
dog['legs'] = "wth"
dog['age'] = 7
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': "Ibrahim",
    'last_name': "Hussain",
    'gender': "male",
    'age': 23,
    'country': "Somalia",
    'city': "Mogadishu",
    'martial_status': False,
    'skills': ["Python", "SQL", "Linux"],
    'address': {
        'street': "The multiverse down hill",
        'zipcode': "065787f"
    }
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'][1] = "React" 
student['skills'][2] = "Node" 
print(student['skills'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
del student['martial_status']
print(student)
# Delete one of the dictionaries
del dog