import re
# What is the most frequent word in the following paragraph?
    # paragraph = 'I love teaching. If you do not love teaching what else can you love. ' \
    # 'I love Python if you do not love something which can give you all ' \
    # 'the capabilities to develop an application what else can you love'
    # regex_pattern = r'\w+'
    # pa = re.findall(regex_pattern, paragraph, re.I)
    # words = {}
    # for word in pa:
    #     if word not in words:
    #        words[word] = pa.count(word)
    # sorted_words = sorted(words.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_words[0])

# The position of some particles on the horizontal x-axis are
#  -12, -4, -3 and -1 in the negative direction, 0 at origin,
#  4 and 8 in the positive direction. 
# Extract these numbers from this whole text 
# and find the distance between the two furthest particles.

    # txt = "The position of some particles on the horizontal x-axis are" \
    # " -12, -4, -3 and -1 in the negative direction, 0 at origin,4 and 8 in the positive direction."
    # regex_pattern = r'(-[0-9][0-9]?|[0-9])+'

    # extract = re.findall(regex_pattern, txt)
    # distance = int(extract[-1]) - int(extract[0])
    # print(extract)
    # print(distance)

# Write a pattern which identifies if a string is a valid python variable
    # def vaid_var_name():
    #     var_name = input("Enter variable name: ")
    #     regex_pattern = r'^[^\d|\-][a-zA-Z0-9_]+$' #TODO -> find a way to reject variables doesnt starts with letters or underscore #DONE
    #     if validate := re.search(regex_pattern, var_name):
    #         return True
    #     return False
    # print(vaid_var_name())

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
regex_pattern = r'[%\$@&#;]'
replace = re.sub(regex_pattern, "",sentence)
lst = replace.split()
word_and_count = {}
for word in lst:
    word_and_count[word] = lst.count(word)
# print(word_and_count)
sort_words_count = sorted(word_and_count.items(), key=lambda item: item[1], reverse=True)
print(sort_words_count[:3])

