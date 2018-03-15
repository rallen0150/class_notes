import csv

def read_write_csv(read_file_name):
    # Opens and reads the file
    with open(read_file_name) as open_file:
        contents = open_file.readlines()

    # Replace the new lines with empty strings and split based on ','
    data = [row.replace("\n", "").split(",") for row in contents]

    # Place holders for correct elements
    same_line = []
    intersecting_line = []

    for value in data:
        if value[0] == value[1]:
            # print(value)
            same_line.append(value)
        elif value[0] == value[1][::-1]:
            # print(value)
            intersecting_line.append(value)

    same = ""
    for element in same_line:
        same += "{},{},".format(element[0], element[1])
    same = same[:-1]

    intersecting = ""
    for element in intersecting_line:
        intersecting += "{},{},".format(element[0], element[1])
    intersecting = intersecting[:-1]

    # Go to the function to write new csv file
    write_to_text('test_output.csv', same, intersecting)

def write_to_text(write_file_name, s1, s2):
    with open(write_file_name, "w") as open_file:
        # writes first line
        open_file.write("1, {}\n".format(s1))
        # writes second line
        open_file.write("2, {}\n".format(s2))
    info = open(write_file_name)


read_write_csv('test_example.csv')
