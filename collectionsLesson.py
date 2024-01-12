# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "pear", "orange"]

# print(fruits[::-1])
#
# for fruit in fruits:
#     print(fruit)

# show attributes and methods available for this collection
# print(dir(fruits))
# print(help(fruits))

print(len(fruits))
print ("apple" in fruits)

fruits.append("banana")
fruits.remove("apple")
fruits.insert(2,"apple")
fruits.sort()
fruits.reverse()
print(fruits)
print(fruits.index("apple"))
fruits.clear()
fruits.append("egg")
fruits.append("egg")
print(fruits.count("egg"))
print(fruits)
print(fruits.count("apple"))

# SET

fruitsAsSet = {"apple", "pear", "orange", "banana"}
print(fruitsAsSet)
fruitsAsSet.add("pineapple")
print(fruitsAsSet)
fruitsAsSet.remove("apple")
print(fruitsAsSet)
fruitsAsSet.pop()
print(fruitsAsSet)

# TOUPLE