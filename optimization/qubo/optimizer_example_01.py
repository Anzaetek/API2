import requests
import json
# GET THE CONFIG
import utils

user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

config = {"configSelect":"gekkoConfig"}
target = "label('l', minimize(list(x1,x2), (x1 - 0.1)**2)) & label('v', x2 == 1.0) & label('v2', x1 > 0.2)"
symbols = ["x1","x2"]
weights = {"l":1.0,"v":100.0,"v2":1000.0}

url = "https://api2.anzaetek.com:443/execute"

def query_optimizer(config, target, symbols, weights):
    q = { 
        "__class__":"SolverProblem", 
        "query":{ "Description":{"Terms":[],"ForceNBits":[],"Parameters":{},"Initialization":{}},
                "DescriptionString":target,
                "DescriptionSymbolList":symbols,
                "DescriptionParameters":weights,
                "Config":config,
                "Info":{"user":user1,"token":token1}}}
    query = {'user': user1, 
            'token': token1, 
            'query': json.dumps(q)}
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    return { k: rv['Results'][k] for k in symbols }

v = query_optimizer(config, target, symbols, weights)
print(v)

config = {"configSelect":"JuliaConfig"}
target = "label('l', minimize(list(x1,x2), (x1 - 0.1)**2)) & label('v', x2 == 1.0) & label('v2', x1 > 0.2)"
symbols = ["x1","x2"]
weights = {"l":1.0,"v":100.0,"v2":1000.0}

v = query_optimizer(config, target, symbols, weights)
print(v)
