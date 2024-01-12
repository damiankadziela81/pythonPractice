# POSITIONAL ARGUMENTS

def sum_custom(a, b):
    print(f"a: {a} + b: {b} = {a+b}")


sum_custom(2, 7)


def multiply(x, y):
    result = x * y
    return result


z = multiply(2, 3)
print(z)

# DEFAULT ARGUMENTS


def net_price(list_price, discount=0.0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500, 0.1, 0))


# KEYWORD ARGUMENTS = arguments prefixed with the names of parameters
# order of the arguments doesn’t matter
# helps with readability

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello", "Mr.", "Dick", "Head")

hello("Hello", first="Dick", title="Mr.", last="Head")


# ARBITRARY ARGUMENTS
# *args       = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))


def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_address(street="123 Fake st.",apt="100",city="Detroit",state="Michigan",zip="12345")


# EXERCISE
print("-------------------------------------------------")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")



