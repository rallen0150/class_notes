l = ["5", "robbie", None, 3, 4]

string_list = str(l)

print(string_list)

import json

json_list = json.dumps(l)
print(json_list)

print(json.dumps({"robbie": 'codes'}))
