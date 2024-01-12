# dictionary =  a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington DC", "Poland": "Warsaw", "Germany": "Berlin"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

capitals.update({"Japan": "Tokyo"})
capitals.update({"Poland": "Krakow"})
capitals.pop("Germany")
capitals.popitem()
keys = capitals.keys()
values = capitals.values()
items = capitals.items()

print(keys)
for key in keys:
    print(key)

print(values)

print(items)

print("---------------------------------")
for k,v in capitals.items():
    print(f"{k}: {v}")

capitals.clear()
print(capitals)
print(keys)