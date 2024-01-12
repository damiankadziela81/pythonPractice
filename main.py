print("VARIABLES")

age = 21
# ways of printing stuff
print("Age: " + str(age) + " years")
print("Age:", age, "years")
# f string
print(f"Age: {age} years")

# DATA TYPES
# integers
age = 32

# float
gpa = 3.2
print(f"gpa = {gpa}")

# string
name = "damson"
print(f"Your name is {name}")

# boolean - first letter is capital, no quotes
state1 = True
state0 = False
if state1:
    print(f"The state is {state1}")
else:
    print(f"The state is {state0}")

# tricks - mulitple assignment
x, y, z = 1, 2, 3
print(f"{x} {y} {z}")
# setting multiple to the same value
x = y = z = 0
print(f"{x} {y} {z}")

print("TYPE CASTING")

mame = "Damson"
age = 42
gpa = 1.9
student = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

ageAsFloat = float(age)
print(ageAsFloat)
print(type(ageAsFloat))

gpaAsInt = int(gpa)
print(gpaAsInt)
print(type(gpaAsInt))

# impl example
validName = "dams"
invalidName = ""
print(bool(validName))
print(bool(invalidName))

# Implicit typecasting
x = 2
y = 2.0
x = x / y
print(x)

# USER INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age = age + 1
print(f"Hello {name}, you are {age} years old")
