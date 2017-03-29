import requests

endpoint = input("What do you want to search for? (pokemon), (type), or (ability)?:\n>")
number = input("What number do you want to see?:\n>")
url = "http://pokeapi.co/api/v2/{}/{}/".format(endpoint, number)

json_result = requests.get(url).json()
result_list = json_result.keys()

print(result_list)

category = input("\nWhat info about the item or Pokémon would you like to see?:\n>")

print(json_result[category])
