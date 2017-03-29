import requests

choice = input("Would you like to look at a (s)pecific item/pokémon or a (l)ist?:\n>").lower()

if choice == 's':
    endpoint = input("What do you want to search for? (pokemon), (type), or (ability)?:\n>").lower()
    number = input("What number do you want to see?:\n>")
    url = "http://pokeapi.co/api/v2/{}/{}/".format(endpoint, number)

    json_result = requests.get(url).json()
    result_list = json_result.keys()

    print(result_list)

    category = input("\nWhat info about the item or Pokémon would you like to see?:\n>").lower()

    print(json_result[category])

elif choice == 'l':
    endpoint = input("What do you want to search for? (pokemon), (type), or (ability)?:\n>").lower()
    url = "http://pokeapi.co/api/v2/{}/".format(endpoint)
    while url:
        result = requests.get(url).json()
        for pokemon in result["results"]:
            print(pokemon['name'])
        if input("---Press Enter to keep going or type n to stop  "):
            break
        url = result["next"]

else:
    print("INVALID OPTION!!!")
