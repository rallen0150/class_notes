# Inventory Tracker RPG

# Player
# Inventory
# Items

player = {"inventory": {"red potion": {"quantity": 20}}}

{
    "red potion": {
        "quantity": 1
    }
}
player_name = input("Welcome Traveler! What is your name?\n>")
player["name"] = player_name
print(player)

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>").lower()

    if choice == 'a':
        item_name = input("What is the item name?\n>")
        item_quantity = int(input("How many?\n>"))
        player["inventory"][item_name] = {"quantity": item_quantity}
        print("Adding item to inventory")

    elif choice == 'i':
        print("Looking in inventory")
        for item in player["inventory"].keys():
            quantity = player["inventory"][item]["quantity"]
            print("{} - {}".format(item, quantity))
