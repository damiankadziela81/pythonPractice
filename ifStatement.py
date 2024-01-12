age = int(input("Enter your age: "))

if age >= 100:
    print("Your are toot old")
elif age >= 18:
    print("Your are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You're too young.")