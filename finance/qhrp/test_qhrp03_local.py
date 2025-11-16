import numpy as np
import datetime
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

def q0(lst, fromdate, todate):
    return {
        "use_covar": [],
        "from_date_yyyy_m_d": fromdate, #"2022-1-1",
        "to_date_yyyy_m_d": todate, #"2023-1-1",
        "ticker_list": lst,
        "constraint_weight": 50
    }

start_date = datetime.date(2023, 2, 1)
end_date = datetime.date(2023, 3, 1)
delta = datetime.timedelta(days=1)

lst = ["ADBE","EQIX","EXPE"]

while (start_date <= end_date):
    if np.is_busday(start_date):
        #print(start_date)
        fmt = start_date.strftime("%Y-%m-%d")
        #print(fmt)
        m1y = start_date - datetime.timedelta(days=365*2)
        fmt2 = m1y.strftime("%Y-%m-%d")
        print(fmt2, fmt)
        alloc = qhrp_query(q0(lst, fmt2, fmt))["allocation"]
        print(alloc)

    start_date += delta
