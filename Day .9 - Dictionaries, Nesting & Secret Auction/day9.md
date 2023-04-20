**SYNTAX**
dictionary = { "key" : value, "key2" : value2}
print(dictionary["key"])

# add new items
dictionary["key3"] = value

# empty dict
dictionary = {}

# edit item
dictionary["key"] = new value

# loop thru
for thing in dictionary:
    print(thing)            **PRINTS KEYS**

# print key and values
for thing in dictionary:
    print(thing)
    print(dictionary[thing])  

