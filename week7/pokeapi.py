import requests

def get_data(endpoint, lookup="name"):
    url = "http://pokeapi.co/api/v2/{}/".format(endpoint)
    while url:
        result = requests.get(url).json()
        for pokemon in result["results"]:
            print(pokemon[lookup])
        if input("---Press Enter to keep going or type n to stop  "):
            break
        url = result["next"]


while True:
    value = input("What do you want to search for? (pokemon), (type), (ability), (berry),\n(item), (generation), (move) or (location):\n> ")
    get_data(value)
