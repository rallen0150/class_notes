# Inventory Tracker RPG

# Player
# Inventory
# Items

player = {}
player_name = input("Welcome Traveler! What is your name?\n>")
player["name"] = player_name
print(player)

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>").lower()

    if choice == 'a':
        print("Adding item to inventory")
    elif choice == 'i':
        print("Looking in inventory")
