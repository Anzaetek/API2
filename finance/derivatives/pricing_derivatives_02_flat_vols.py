import requests
import json
# GET THE CONFIG
import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

path = "examples/flatvols/vanilla_01.json"
with open(path, "r") as f:
    els = json.loads(f.read())

url = "https://api2.anzaetek.com:443/execute"
def query16(els):
    q = { "__class__":"SibeliusProblem", 
        "query": { "Config":{},
                    "Info":{"user":user1,"token":token1},
                    "SibeliusString": json.dumps(els) }}
    query = {'user': user1, 
            'token': token1, 
            'query': json.dumps(q)}
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    rj = json.loads(rv['Results']['analytics'])
    return rj['scenarios'], rj['values']

rv = query16(els)
print(repr(rv))