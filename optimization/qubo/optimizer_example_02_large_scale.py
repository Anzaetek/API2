import requests
import json
# GET THE CONFIG
import utils

#   local prefix: optimization/qubo/
path = "examples_matrices/finance/01/r11-12-13-14-15-16-17-18-19-20-21-0.3-0.5-0.5-0.2-5-100.0-100.0-100.0-100.0-112x112.config"
with open(path, "r") as f:
    data = json.loads(f.read())
for k in data:
    print("object in archive: ", k)
info = data['data:']
print(info.keys())
# program
program = info['program'].replace(">1.0", ">@1").replace("==1.0", "==@1").replace("<1.0", "<@1").replace("\n", "").replace("\r", "")
print("program = " , program)
# vars
print(info['vars'])
# weights
print(info['weights'])

user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

config = {"configSelect":"JuliaConfig"}
target = program # "label('l', minimize(list(x1,x2), (x1 - 0.1)**2)) & label('v', x2 == 1.0) & label('v2', x1 > 0.2)"
symbols = info['vars'] # ["x1","x2"]
weights = info['weights'] # {"l":1.0,"v":100.0,"v2":1000.0}

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
