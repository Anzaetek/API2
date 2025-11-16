import utils
import json
import requests

# Get configuration
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

##print(user1, token1)

uri = "http://127.0.0.1:5000/execute"

def qhrp_query(q0):
    q = {
        "__class__": "QHRP",
        "user": user1,
        "token": token1,
        "query": q0
    }
    qs = json.dumps(q)
    query = {      
        "user": user1,
        "token": token1,
        "query": qs,        
    } 
    post_response = requests.post(url = uri, json=query)
    rv = post_response.json()
    print(rv)
    return rv

q0 = {
    "use_covar": [[0.12055772584937176, 0.0434040736259131, 0.03657016444844578], 
                                [0.0434040736259131, 0.13147949152864283, 0.03381911680330686], 
                                [0.03657016444844578, 0.03381911680330686, 0.10987923580316178]],
    "from_date_yyyy_m_d": "2022-1-1",
    "to_date_yyyy_m_d": "2023-1-1",
    "ticker_list": [
        "ADBE",
        "EQIX",
        "EXPE"
    ],
    "constraint_weight": 50
}

res = qhrp_query(q0)
print("allocation:", res["allocation"], " perm = ", res["perm"])
