import requests
import json
# GET THE CONFIG
import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

path = "examples/parametrizedvols/uocall_03.json"
with open(path, "r") as f:
    els = json.loads(f.read())

url = "https://api2.anzaetek.com:443/execute"
#url = "http://localhost:5000/execute"
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
    print(rv)
    rj = json.loads(rv['Results']['analytics'])
    print(rj)
    return rj

rv = query16(els)
print(repr(rv))
# OK
