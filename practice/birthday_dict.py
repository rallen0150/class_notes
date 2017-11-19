birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Barack Obama': '08/04/1961',
    'Rowan Atkinson': '01/6/1955',
    'Derek Jeter': '06/26/1974',
    'Frank Martin': '03/26/1966'
    }

# How to add another key & value to dictionary
birthdays['Fake Me'] = '01/19/1990'

print("Welcome. We know the birtdays of: ")
for name in birthdays:
    print(name)

option = 'b'
while option != "q":
    option = input("Do you want to (a)dd another birthday or (s)earch for a birthday or (l)ist of names or (q)uit?: ").lower()
    if option == 'a':
        name = input("Input a name: ").title()
        bday = input("Enter a birthday with the format m/d/y: ")
        birthdays[name] = bday
    elif option == "s":
        search = input("Whose birthday do you want to look up?\n>").title()
        print("{}'s birthday is on {}".format(search, birthdays[search]))
    elif option == 'l':
        print("\nWe know the birtdays of: ")
        for name in birthdays:
            print(name)
    elif option == 'q':
        print("Thank you for adding and viewing birthdays!\nGoodbye!")
    else:
        print('Invalid Option!\nPlease type a correct option')
