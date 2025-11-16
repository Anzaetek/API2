
import numpy as np
import json
import requests

# only needed for getenvcached ~
import utils

# load a big matrix
#   local prefix: optimization/qubo/
path = "examples_matrices/finance/01/r0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-0.2-0.4-0.4-0.1-5-10.0-10.0-10.0-10.0-200x200.config"
with open(path, "r") as f:
    data = json.loads(f.read())
for k in data:
    print("object in archive: ", k)
matrix = data['data:']['matrix']
with np.printoptions(threshold=np.inf):
    print("matrix = ", repr(np.array(matrix))) # json.dumps(matrix, indent=4)

# get environment
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

config = {
    "backend":"JuliaQUBOBackend",
    "nshots":1
}

url = "https://api2.anzaetek.com:443/execute"
# url = "http://localhost:5000/execute"

def qubo_query(config, matrix):
    q = { 
        "__class__":"QUBOSolverProblem", 
        "query": {
                "Qubo":{"W":matrix},
                "Config": config,
                "Info":{"user":user1,"token":token1}
            }
        }
    query = { 'user': user1, 'token': token1, 'query': json.dumps(q) }
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    return rv['Results']['bestBinaryVector']

v = qubo_query(config, matrix)
print("suggested solution vector: ", v)
