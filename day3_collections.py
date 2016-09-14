
my_string = "peanut is awesome"
my_string = my_string.split(" ")
print(my_string)

my_list = ["Robbie", 23, ["the dark", "wasps"]]

print(my_list)
my_list.pop()
my_list.append("peanut")
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[2][0])

# Now Dictionary

my_dictionary = {
    "name": "Robbie",
    "age": 23,
    "fears": ["the dark", "wasps"]
}

print(my_dictionary)
print(my_dictionary["name"])
print(my_dictionary["age"])
print(my_dictionary["fears"])

print(my_dictionary.keys())
