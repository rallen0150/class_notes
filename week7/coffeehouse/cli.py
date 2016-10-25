import requests


# print(json_result)
count = 0
while True:
    json_result = requests.get("http://localhost:8000/specials/").json()
    for special in json_result:
        count += 1
        print(count)
        print(special["name"])
        print(special["price"])
        print(special["description"])
        print("*" * 80)
