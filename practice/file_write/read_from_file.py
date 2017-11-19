select_file = input("Which file do you want to read from (don't need .txt extension)?\n>")

with open("{}.txt".format(select_file), 'r') as open_file:
    lines = open_file.readline()
    while lines:
        print(lines)
        lines = open_file.readline()
    open_file.close()
