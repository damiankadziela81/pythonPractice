number = "123456789"

# for x in range(1,10,2):
#     x = x * 2
#     print(x)
#     if x > 9:
#         print(f"{str(x)[0]} + {str(x)[1]}")
#         sumAsInt = int(str(x)[0]) + int(str(x)[1])
#         sumAsString = str(x)[0] + str(x)[1]
#         print(f"Sum as int= {sumAsInt}")
#         print(f"Sum as string= {sumAsString}")

# odd
for x in number[::2]:
    print(x)


# even
for x in number[1::2]:
    print(x)


