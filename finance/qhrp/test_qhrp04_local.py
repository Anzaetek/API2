import utils
import json
import requests

# Get configuration
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

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
    #print(rv)
    return rv

def q0(lst, t):
    return {
        "use_covar": [],
        "from_date_yyyy_m_d": "2022-1-1",
        "to_date_yyyy_m_d": "2023-1-1",
        "ticker_list": lst,
        "constraint_weight": 50, 
        "mode": "replay", # record, record_and_compute, replay
        "tag": t 
    }

lsts = [
    ["ADBE","EQIX","EXPE"],
    ["BAC","KO","ABBV","C"],
    ["ABBV", "C", "ADBE", "EQIX", "EXPE"],
    ["BAC", "COST", "ABBV", "C", "ADBE", "EQIX", "EXPE"],
    ["BAC", "COST", "ABBV", "C", "ADBE", "EQIX", "EXPE", "ABBV"],
    ["MCHP", "UAL", "CFG", "AMT", "ALGN", "CLX", "FSLR", "OTIS", "MSFT"],
    ["K", "CPB", "DHI", "MRNA", "JPM", "COP", "TMUS", "GRMN", "ROL", "META"],
    ["WAT", "TDY", "PG", "J", "JCI", "EL", "APH", "APD", "ROST", "VZ", "PANW", "HCA", "PFG", "DGX"]
]

c = 0
for l in lsts: 
    print("tickers = ", l)
    t = "qhrp04" + str(c)
    try:
        res = qhrp_query(q0(l, t))
        print(res["allocation"], res["perm"])
    except:
        pass
    c+=1
