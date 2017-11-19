filename = input("Name of file: ")

with open(filename+".txt", 'w') as open_file:
    text = input("What do you want to say in this file?\n")
    open_file.write(text)
    open_file.close()
