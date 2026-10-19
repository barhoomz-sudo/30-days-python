import re

# txt = "my name is Ibrahim Hussain and I love to code with Python"
# re.match() -> returns an object only if the string starts with the pattern
# match = re.match('my name is Ibrahim Hussain', txt, re.I)
# # print(match)
# span = match.span()
# start, end = span
# substring = txt[start:end]
# print(substring)

# re.search -> returns an object if the string contians the pattern (looks throughout the entire string)
# s = re.search("and", txt, re.I)
# # print(s)
# span = s.span()
# start, end = span
# substring = txt[start:end]
# print(substring)

# re.findall() -> returns all matches as a list
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# f = re.findall('language', txt, re.I)
# print(f)
# you can also do -> 'Python|python' this or this
# without_i = re.findall('[Pp]ython', txt)
# print(without_i)

# re.sub() -> replace a pattern in a string
# replace = re.sub('python|Python', 'C', txt)
# print(replace)

# re.split() -> splits text...
# sp = re.split('\n', txt)
# print(sp)

# regex_pattern = r'[Aa]pple'
# txt = "Iphone's logo is Apple. an apple someone took a bite of it."
# find = re.findall(regex_pattern, txt)
# print(find)

# '+' -> means one or more times of whatever comes before it 
# reg_pattern = r'\d+'
# txt = "today is 19/10/2026"
# m = re.findall(reg_pattern, txt)
# print(m)

# '.' -> means any character except new line '\n'
# regex_pattern = r'[a].'
# txt = "any abbreviation will be sufficient"
# d = re.findall(regex_pattern, txt)
# print(d)

# '*' -> means it can occur zero or many times
# regex_patter = r'a.*'
# txt = "you are a toy!"
# pattern = re.findall(regex_patter, txt)
# print(pattern)

# '?' -> means the pattern may appear once or wont occur
# txt = "some people say email others say Email some folks say E-mail or e-mail"
# regex_pattern = r'[Ee]-?mail'
# r = re.findall(regex_pattern, txt)
# print(r)

# '{} -> numbers the pattern should have'
# txt = "in October 19, 2026-2027 i was doing the day number 18 of regex in python 30 day mastery repo"
# regex_pattern = r'\d{4}'
# pattern = re.findall(regex_pattern, txt)
# print(pattern)

# '^' -> means start from here
# txt = "lorem ipsum trafshs 0976423"
# regex_pattern = r'^lorem'
# p = re.findall(regex_pattern, txt)
# print(p)
# regex_pattern = r'[^A-Za-z_]+'
# np = re.findall(regex_pattern, txt)
# print(np)