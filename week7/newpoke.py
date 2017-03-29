import requests

url = "http://pokeapi.co/api/v2/pokemon/1"

json_result = requests.get(url).json()
result_list = json_result.keys()

print(result_list)

category = input("What info about the Pokémon would you like to see?:\n>")

print(json_result[category])
