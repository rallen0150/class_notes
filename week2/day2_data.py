import csv

# Help with the comprehension homework
with open("data.csv") as open_file:
    contents = open_file.readlines()

# print(contents[2].split("|")[2])

# clean_data = []

clean_data = [row.replace("\n", "").split("|") for row in contents]
# print(clean_data[11][4])
# print(clean_data)

with open("data.csv") as open_file:
    # contents = csv.reader(open_file)
    contents = csv.DictReader(open_file, delimiter="|")
    print(list(contents)[1]["Water Temp"])
