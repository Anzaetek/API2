# QUBO solver/optimizer example with the Anzaetek API
# Make sure the following is installed to run this example
# pip install requests
import requests
import json
import utils

# get environment
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

qubo = [
    [0.0, -1.0,  4.0],
    [-1.0, 5.0, -9.0],
    [4.0, -9.0, -5.0]
]

config = {
    "backend":"QUBOSimulatorBackend",
    "nshots":2000
}

url = "https://api2.anzaetek.com:443/execute"
# url = "http://localhost:5000/execute"

def quboquery(config, qubo):
    q = { 
        "__class__":"QUBOSolverProblem", 
        "query": {
                "Qubo":{"W":qubo},
                "Config": config,
                "Info":{"user":user1,"token":token1}
            }
        }
    query = { 'user': user1, 'token': token1, 'query': json.dumps(q) }
    post_response = requests.post(url = url, json=query)
    rv = post_response.json()
    #print(rv)
    return rv['Results']['bestBinaryVector']

v = quboquery(config, qubo)
print(config["backend"], v)

config = {
    "backend":"JuliaQUBOBackend",
    "nshots":1
}
 
v = quboquery(config, qubo)
print(config["backend"], v)

config = {
     "backend": "FujitsuDASimulatorBackend",
     "nshots": 1,
     "number_iterations": 1000,   #  = 1000,               # total number of itrations per run
     "number_runs": 16,           #  = 16,                  # number of stochastically independant runs
     "temperature_start": 5000,   # = 5000,               # start temperature for annealing as float value
     "temperature_end": 10,       # = 10,                 # end temperature for annealing as float value 
     "temperature_mode": 0,      # = 0,                         # 0: reduce temperature by factor (1-temperature_decay) every temperature_interval steps
                                                       # 1: reduce temperature by factor (1-temperature_decay*temperature) every temperature_interval steps
                                                       # 2: reduce temperature by factor (1-temperature_decay*temperature^2) every temperature_interval steps
     "temperature_decay": 0.0095, # = 0.0095,             # see temperature_mode 0
     "temperature_interval": 1,   # = 1,                  # see temperature_mode 0
     "offset_increase_rate": 5000.0, # = 5000.0,             # increase of dynamic offset when no bit selected, set to 0.0 to switch off dynamic offset
     #"graphics": True,               # = True                # create data for graphics output 
     "rescale": 100.0
}

v = quboquery(config, qubo)
print(config["backend"], v)

config = {
     "backend": "VQESimulatorBackend",
     "ninit": 1,
     "nshots": 10,     
}

v = quboquery(config, qubo)
print(config["backend"], v)

config = {
     "backend": "OpticQUBOBackend",
     "nshots": 1,
}

v = quboquery(config, qubo)
print(config["backend"], v)