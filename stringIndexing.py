credit_number = "1234-5678-9012-3456"

# first 4 digits
print(credit_number[0:4])
# or
print(credit_number[:4])
# 2nd 4 digits
print(credit_number[5:9])
# everything past 5 index
print(credit_number[5:])
# last index
print(credit_number[-1])
# pre-last etc
print(credit_number[-2])
# steps - every 2nd character
print(credit_number[::2])
# every 2nd from each fours
print(credit_number[1::5])
# reverse
print(credit_number[::-1])

email = input("Enter your email: ")
index = email.index("@")
username = email[:index]
domain = email[index + 1:]
print(f"usename: {username}" )
print(f"domain: {domain}" )




