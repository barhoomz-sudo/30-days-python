import random
import string
import math

# Write a function which generates a six digit/character random_user_id.
    # def random_user_id():
    #     letters_and_digits = string.ascii_letters + string.digits
    #     length = len(letters_and_digits)
        
    #     user_id = ''
    #     for _ in range(6):
    #         random_number = math.floor(random.random() * length)
    #         user_id += letters_and_digits[random_number]

    #     return user_id
    # print(random_user_id())

 # Modify the previous task. Declare a function named user_id_gen_by_user. 
 # It doesn’t take any parameters but it takes two inputs using input(). 
 # One of the inputs is the number of characters 
 # and the second input is the number of IDs which are supposed to be generated.

    # def user_id_gen_by_user():
    #     number_of_characters = int(input("Number of characters: "))
    #     number_of_ids = int(input("Number of IDs: "))
    #     letters_and_digits = string.ascii_letters + string.digits
    #     length = len(letters_and_digits)

    #     user_id = ''
    #     for _ in range(number_of_ids):
    #         for _ in range(number_of_characters):
    #             random_number = math.floor(random.random() * length)
    #             user_id += letters_and_digits[random_number]
    #         user_id += '\n'
    #     return user_id.removesuffix("\n")
    # print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
    # def rgb_color_gen():
    #     red = math.floor(random.random() * 256)
    #     green = math.floor(random.random() * 256)
    #     blue = math.floor(random.random() * 256)

    #     return f"rgb({red},{green},{blue})"
    # print(rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number 
# of hexadecimal colors in an array (six hexadecimal numbers written 
# after #. Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f. 
# Check the task 6 for output examples).
    # def list_of_hexa_colors():
    #     number_of_hexas = int(input("Number of Hexa color's: "))
    #     digits_and_letters = string.digits + string.ascii_letters[:6]

    #     hexa_color = '#'
    #     for _ in range(number_of_hexas):
    #         for _ in range(6):
    #             random_number = math.floor(random.random() * len(digits_and_letters))
    #             hexa_color += digits_and_letters[random_number]
    #         hexa_color += ' #'
    #     hexa_colors = hexa_color.split(" ")
    #     hexa_colors.pop()
    #     return hexa_colors
    # print(list_of_hexa_colors())

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
    # def list_of_rgb_colors():
    #     number_of_colors = int(input("Number of RGB color's: "))

    #     colors = []
    #     for _ in range(number_of_colors):
    #         red = math.floor(random.random() * 256)
    #         green = math.floor(random.random() * 256)
    #         blue = math.floor(random.random() * 256)
    #         rgb = f"rgb({red},{green},{blue})"
    #         colors.append(rgb)

    #     return colors
    # print(list_of_rgb_colors())

# Write a function generate_colors which can generate any number of hexa or rgb colors.
# def generate_colors(color, num):
#     if color == "rgb":
#         colors = []
#         for _ in range(num):
#             red = math.floor(random.random() * 256)
#             green = math.floor(random.random() * 256)
#             blue = math.floor(random.random() * 256)
#             rgb = f"rgb({red},{green},{blue})"
#             colors.append(rgb)

#         return colors
#     if color == "hexa":
#         digits_and_letters = string.digits + string.ascii_letters[:6]
#         hexa_color = '#'
#         for _ in range(num):
#             for _ in range(6):
#                 random_number = math.floor(random.random() * len(digits_and_letters))
#                 hexa_color += digits_and_letters[random_number]
#             hexa_color += ' #'
#         hexa_colors = hexa_color.split(" ")
#         hexa_colors.pop()
#         return hexa_colors
# print(generate_colors("rgb", 3))
# print(generate_colors("hexa", 4))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
    # def shuffle_list(ls):
    #     random.shuffle(ls)
    #     return ls
    # print(shuffle_list([1,2,3,4,5,6]))

# Write a function which returns an array of seven random numbers in a range of 0-9.
# All the numbers must be unique.
    # def random_numbers_list():
    #     ls = []
    #     length = 7
    #     while length > 0:
    #         random_nums = random.randint(0,9)
    #         if random_nums not in ls:
    #             ls.append(random_nums)
    #             length -= 1
    #         else:
    #             continue

    #     return ls
    # print(random_numbers_list())