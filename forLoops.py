# for x in range(1,11):
#     print(x)
#
# for x in reversed(range(1,11)):
#     print(x)
#
# for x in range(1,11,2):
#     print(x)
#
# numberString = "1234567890"
# for x in numberString:
#     print(x)
#
# for x in range(1, 21):
#     if x == 13:
#         # continue
#         break
#     else:
#         print(x)

# nested
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

# print(x) == print(x, end="\n")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

