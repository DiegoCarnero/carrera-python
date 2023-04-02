import requests
import json

# https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvprop=content&format=json

param = {"action": "query", "prop": "revisions", "titles": "Pet_door", "rvprop": "content", "format":"json"}

r = requests.get("https://en.wikipedia.org/w/api.php", param)

json_obj = r.json()
print(json.dumps(json_obj, indent= 4))
