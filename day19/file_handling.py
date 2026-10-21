import os
import json
import csv
import xml.etree.cElementTree as et

# file = open("ex.txt")
# # print(file.read(9))
# # print(file.readline()) # one line only
# print(file.readlines())
# file.close()

# lines = file.read().splitlines()
# print(lines)
# file.close()

# with open("ex.txt") as f:
#     lines = f.read().splitlines()
#     print(lines)

# with open("ex.txt", "a") as file:
#     file.write("this third is added using append mode")

# with open("new.txt", "w") as f:
#     f.write("new file created with write mode")

# if os.path.exists("new.txt"):
#     os.remove("new.txt")
# else:
#     print('file doesnt exsit')

# json to dictionary
# person_json = '''{
#     "name": "Ibrahim",
#     "age": "24",
#     "country": "Somalia"
# }'''
# print(person_json)
# print(type(person_json))
# person_dictionary = json.loads(person_json)
# print(person_dictionary)
# print(type(person_dictionary))


per_dict = {
    'name': "Ibrahim",
    'age': 24,
    'skills': [
        'Python',
        'HTML',
        'CSS'
    ]
}

# dictionary to json
# per_json = json.dumps(per_dict, indent=4)
# print(per_json)

# # saving as JSON file
# with open("json_example.json", "w", encoding='UTF-8') as j:
#     json.dump(per_json, j, ensure_ascii=False, indent=4)

# csv
# with open("csv_file.csv") as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f"column names are: {", ".join(row)}")
#             line_count += 1
#         else:
#             print(f"{row[0]} is a passionate future ML. he lives in {row[1]}, {row[2]}")
#             line_count += 1
#     print(f"number of lines: {line_count}")


# working with xml
# tree = et.parse("xml_ex.xml")
# root = tree.getroot()
# print("Root tag:",root.tag)
# print("attribute:",root.attrib)
# for ch in root:
#     print("field:",ch.tag)

