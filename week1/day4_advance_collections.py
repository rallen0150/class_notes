#  Tuple

my_tuple = ("robbie", "sarah")
print(my_tuple)
# can't add anything to a tuple
# my_tuple.append("peanut")
# print(my_tuple)

my_string = "cellular phone"
print(my_string + "s")
# print(my_string)
# my_string[2] = "j"

# Set

my_set = {2, 7, 9, "robbie"}
my_people_set = {"robbie", "sarah", "peanut"}
print(help(my_set))
# finds the same item in 2 sets is from intersection
print(my_set.intersection(my_people_set))
