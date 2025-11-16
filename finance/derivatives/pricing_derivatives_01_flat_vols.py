import requests
import json
# GET THE CONFIG
import utils
user1 = utils.getenvcached("QUETZALCOATL_USER1")
token1 = utils.getenvcached("QUETZALCOATL_TOKEN1")

els = { "arguments":[{
    "method":"PriceFLEXMCHLV(npath=65536,npathOld=262144)",
    "trade_string":"BasketCall(maturity=20211113,T=20191113,underlyings=KOSPI2+SAMSUNG,ref1=280,ref2=100,strike=1)",
    "spots":{"KOSPI2":280,"SAMSUNG":100},
    "rates":{"KRW":0.04},
    "repos":{"KOSPI2":0.03,"SAMSUNG":0.01},
    "flatVols":{"KOSPI2":0.20,"SAMSUNG":0.14},
    "fxInterest": {"KRW":0.04},
    "fxYield": {"USDKRW":0.01},
    "fxVols": {"USDKRW":0.20},
    "fxSpots": {"USDKRW":1100.0},
    "ratesMap": {"KOSPI2":"KRW","SAMSUNG":"KRW"},
    "correlations":[[1.0, 0.7],[0.7, 1.0]],
    "correlationKeys":["KOSPI2", "SAMSUNG"]
    }],
    "name": "PriceSimplifiedJob/1"
}

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