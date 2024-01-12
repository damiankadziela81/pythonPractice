# name = input("Enter your name:")
# phoneNumber = input("Enter your phone number.")

# result = len(name)
# result = name.find(" ")
# result = name.rfind("s") # last occurrence
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phoneNumber.count("-")
# phoneNumber = phoneNumber.replace("-", "")
#
# print(result)
# print(name)
# print(phoneNumber)

# print(help(str))

# exercise - input validator
name = input("Enter user name: ")

if len(name) > 12:
    print("Your name can't have more than 12 characters")
elif name.__contains__(" "):
    print("Your name can't contain spaces")
elif not name.isalpha():
    print("Your name can't have digits")
else:
    print(f"Welcome {name}")
