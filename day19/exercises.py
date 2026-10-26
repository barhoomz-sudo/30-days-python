import json
import re


# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# Read obama_speech.txt file and count number of lines and words
    # with open("./obama_speech.txt") as f:
        # number_of_lines = f.read().splitlines()
        # print(number_of_lines)
        # words = f.read()
        # lst_words = words.split()
        # print(len(lst_words))
        # print(lst_words)
    
# Read michelle_obama_speech.txt file and count number of lines and words
    # with open("./michelle_obama_speech.txt") as f:
    #     # number_of_lines = f.read().splitlines()
    #     # print(len(number_of_lines))
    #     words = f.read()
    #     lst_words = words.split()
    #     print(len(lst_words))
    #     print(lst_words)
# Read donald_speech.txt file and count number of lines and words
    # with open("./donald_speech.txt") as f:
    #     number_of_lines = f.read().splitlines()
    #     print(len(number_of_lines))
    #     words = f.read()
    #     lst_words = words.split()
    #     print(len(lst_words))
    #     print(lst_words)
# Read melina_trump_speech.txt file and count number of lines and words
    # with open("./melina_trump_speech.txt") as f:
    #     number_of_lines = f.read().splitlines()
    #     print(len(number_of_lines))
    #     words = f.read()
    #     lst_words = words.split()
    #     print(len(lst_words))

# Read the countries_data.json data file in data directory, 
# create a function that finds the ten most spoken languages
    # def top_ten(file, n):
    #     with open(file) as f:
    #         countries = f.read()
    #         json_countries = json.loads(countries)

    #         langs = []
    #         for country in json_countries:
    #             for languages in country["languages"]:
    #                 langs.append(languages)

    #         langs_and_count = {}
    #         for language in langs:
    #             langs_and_count[language] = langs.count(language)
    #         sorted_languages = sorted(langs_and_count.items(), key=lambda item: item[1], reverse=True)
    #     return sorted_languages[:n]
    # print(top_ten("countries_data.json",3))
    # print(top_ten("countries_data.json",10))

# Read the countries_data.json data file in data directory, 
# create a function that creates a list of the ten most populated countries
    # def most_populated_countries(file, n):
    #     with open(file) as f:
    #         countries = f.read()
    #         parsed_countries = json.loads(countries)

    #         name_and_population = {}
    #         for country in parsed_countries:
    #             name_and_population[country["name"]] = country["population"]
    #         sorted_population = sorted(name_and_population.items(), key=lambda item: item[1], reverse=True)
    #     return sorted_population[:n]

    # print(most_populated_countries("countries_data.json", 3))
    # print(most_populated_countries("countries_data.json", 10))

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
    # with open("email_exchanges_big.txt") as f:
    #     r = f.read()
    #     matches = re.findall(r'\w+@\w+\.\w+', r) # many wierd email are in the file, so followed this standard username@subdomain.maindomain
    #     print(matches)
# Find the most common words in the English language. 
# Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, 
# indicating the number of words. Your function will return an array of tuples in descending order. 
    # d = "hello world my name is ibrahim and i am a software developer using python and i love solving problems"
    # def find_most_common_words(s, n):
    #     joined_string = s.split(" ")

    #     words_dictionary = {}
    #     for word in joined_string:
    #         words_dictionary[word] = joined_string.count(word)
    #     decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words(d,3))

# Use the function, find_most_frequent_words to find:
# The ten most frequent words used in Obama's speech
    # def find_most_common_words(s, n):
    #     with open(s) as f:
    #         res = f.read()
    #         splitted_speech = res.split(" ")
    #         words_dictionary = {}
    #         for word in splitted_speech:
    #             words_dictionary[word] = res.count(word)
    #         decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words("obama_speech.txt",3))
# The ten most frequent words used in Michelle's speech
    # def find_most_common_words(s, n):
    #     with open(s) as f:
    #         res = f.read()
    #         splitted_speech = res.split(" ")
    #         words_dictionary = {}
    #         for word in splitted_speech:
    #             words_dictionary[word] = res.count(word)
    #         decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words("michelle_obama_speech.txt",3))
# The ten most frequent words used in Trump's speech
    # def find_most_common_words(s, n):
    #     with open(s) as f:
    #         res = f.read()
    #         splitted_speech = res.split(" ")
    #         words_dictionary = {}
    #         for word in splitted_speech:
    #             if word != "":
    #                 words_dictionary[word] = res.count(word)
    #         decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words("donald_speech.txt",3))
# The ten most frequent words used in Melina's speech
    # def find_most_common_words(s, n):
    #     with open(s) as f:
    #         res = f.read()
    #         splitted_speech = res.split(" ")
    #         words_dictionary = {}
    #         for word in splitted_speech:
    #             if word != "":
    #                 words_dictionary[word] = res.count(word)
    #         decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words("melina_trump_speech.txt",3))
from stop_words import stop_words as sw
#Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, function to clean the text(clean_text), 
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
# List of stop words are in the data directory
    # def clean_text(file):
    #     with open(file) as f:
    #         txt = f.read()
    #         lower_cased_txt = txt.lower()
    #         ascii_punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    #                      ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    #         extra_punctuation = ['—', '–', '…', '‘', '’', '“', '”', '«', '»', '•', '¿', '¡']

    #         all_punctuation = ascii_punctuation + extra_punctuation
    #         placeholder = []
    #         for char in lower_cased_txt:
    #             if char not in all_punctuation:
    #                 placeholder.append(char)
    #             else:
    #                 placeholder.append(" ")
    #         joined_txt = "".join(placeholder)
    #         splitted_txt = joined_txt.split()

    #         return " ".join(splitted_txt)
        
    # melina_speech_cleaned = clean_text("melina_trump_speech.txt")
    # michelle_speech_cleaned = clean_text("michelle_obama_speech.txt")

    # def remove_support_words(s):
    #     words = s.split()
    #     set_of_stop_words = set(sw)
    #     removed_stop_words = []
    #     for word in words:
    #         if word not in set_of_stop_words:
    #             removed_stop_words.append(word)
    #     return removed_stop_words

    # melina_sppech_stop_words_removed = remove_support_words(melina_speech_cleaned)
    # michelle_sppech_stop_words_removed = remove_support_words(michelle_speech_cleaned)

    # def check_similarity(lst1, lst2):
    #     set1 = set(lst1)
    #     set2 = set(lst2)

    #     result = set1 & set2
    #     union_of_sets = set1 | set2
    #     if len(union_of_sets) == 0:
    #         return "0%"
    #     return len(result) / len(union_of_sets)

    # print(f"Similarity btween the speeches is: {check_similarity(melina_sppech_stop_words_removed, michelle_sppech_stop_words_removed):.0%}")

# Find the 10 most repeated words in the romeo_and_juliet.txt
    # from stop_words import stop_words as sw
    # def find_most_common_words(s, n):
    #     with open(s) as f:
    #         res = f.read()
    #         splitted_speech = res.split(" ")
    #         words_dictionary = {}
    #         for word in splitted_speech:
    #             if word not in [".", ""]:
    #                 words_dictionary[word] = res.count(word)
    #         decending_order_words = sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True)
    #     return decending_order_words[:n]
    # print(find_most_common_words("romeo_and_juliet.txt",3))

import csv
import re
#Read the hacker news csv file and find out:
# Count the number of lines containing python or Python
    # with open("hacker_news.csv") as f:
    #     lines = csv.reader(f, delimiter=',')
    #     counter = 0
    #     for row in lines:
    #         line = ",".join(row)
    #         matches = re.search(r'[Pp]ython', line)
    #         if matches:
    #             counter += 1
    #     print(counter)
# Count the number lines containing JavaScript, javascript or Javascript
    # with open("hacker_news.csv") as f:
    #     lines = csv.reader(f, delimiter=',')
    #     counter = 0
    #     for row in lines:
    #         line = ",".join(row)
    #         matches = re.search(r'[Jj]ava[Ss]cript', line)
    #         if matches:
    #             counter += 1
    #     print(counter)
# Count the number lines containing Java and not JavaScript
with open("hacker_news.csv") as f:
    lines = csv.reader(f, delimiter=',')
    counter = 0
    for row in lines:
        line = ",".join(row)
        matches = re.search(r'Java\b', line)
        if matches:
            counter += 1
    print(counter)