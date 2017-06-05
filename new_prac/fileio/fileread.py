# PRINT THE TEXT LINE BY LINE
with open("test.txt", 'r') as open_file:
    contents = open_file.read()
    print(contents)
################################################################################

# ADDING TO AN EXISTING FILE
def write_to_text(file_name):
    with open(file_name, "w") as open_file:
        open_file.write("Robbie is the best!\n")
        open_file.write("He is awesome!\n")
    info = open(file_name)
    print(info.read())
write_to_text('write.txt')

################################################################################

def add_to_array(file_name):
    new_array = []
    with open(file_name, "r") as open_file:
        for line in open_file:
            new_array.append(line)
        print(new_array)

def number_of_lines(file_name):
    num_of_lines = 0
    with open(file_name, "r") as x:
        for line in x:
            num_of_lines = num_of_lines + 1
        return num_of_lines

add_to_array("test.txt")
print("\n")
print(number_of_lines('test.txt'))
print(number_of_lines("write.txt"))
print("\n")

################################################################################

def write_list_to_file(file_name, list):
    with open(file_name, "w") as myfile:
        for c in list:
            myfile.write(c)
            myfile.write("\n")
    colors = open(file_name)
    return(colors.read())

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Purple', 'Blue', 'Silver', 'Gold']
print(write_list_to_file("color.txt", color))

################################################################################
# TO COPY A FILE
from shutil import copyfile
copyfile("color.txt", "abc.txt")
