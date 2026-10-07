# n = 8
# n = int(input("What's n? "))
# if n % 2 == 0 and n != 0:
#     print("Even")
# elif not n % 2 == 0:
#     print("Odd")
# else:
#     print("zero")

# print("positive") if n > 0 else print("negative")

a = 4

if a > 0:
    if a % 2 == 0:
        print("positive + even")
    else:
        print("positive")
elif a == 0:
    print("zero")
else:
    print("negative")