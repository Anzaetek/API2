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
        "mode": "record", # record, record_and_compute, replay
        "tag": t 
    }

good_names = ["TPR","EMR","CTAS","HSIC","KIM","PLD","IEX","BAC","CBOE","EXR","NCLH","CVS","DRI","DTE","AVY","AXON","EW","EA","NWSA","BBWI","CAG",
              "GILD","FCX","GPC","UNP","CDW","SBUX","MNST","CMCSA","KEY","ISRG","CTVA","AKAM","EMN","WMT","EG","K","CPB","DHI","JPM","COP","TMUS",
              "GRMN","ROL","META","FI","TEL","IVZ","KLAC","AVB","ELV","MSCI","ZBRA","BKNG","FRT","DVN","SLB","TMO","PRU","CAH","MAR","CCI","TER",
              "TXN","ENPH","F","COST","MAS","NEM","ORCL","TDG","TSLA","WBA","WEC","UHS","TFX","VTRS","WST","BALL","CB","FOX","HUM","GOOG","ZBH",
              "WY","LMT","COR","MOS","PNW","VRSN","WMB","DOW","FOXA","CAT","GEN","LULU","IRM","MTD","CHRW","GIS","KO","MCO","SNA","EXPE","EVRG","OKE",
              "NVR","EQT","KEYS","PFE","DXCM","AMAT","LNT","AMCR","XOM","EQIX","CI","CMA","VLO","CMG","FAST","BEN","LYV","WAT","TDY","PG","J","JCI","SMCI",
              "EL","APH","APD","ROST","VZ","PANW","HCA","PFG","DGX","CRL","RMD","VICI","AWK","CINF","GOOGL","SYK","HAL","PPG","ECL","JBL","WRB","CMS","ILMN",
              "MS","BA","ATO","EIX","ULTA","ED","UNH","ALB","DPZ","PHM","USB","AJG","MHK","BIIB","BSX","SHW","EOG","VRTX","HII","AFL","EBAY","NDAQ","SWK","MKC",
              "FIS","TAP","EXC","GNRC","TT","MAA","NOW","RHI","MPWR","AES","L","REGN","SRE","CCL","O","BMY","HPQ","YUM","IR","WTW","MOH","BX","RL","URI","D","NTRS",
              "AVGO","HSY","ADP","CL","XEL","RF","HIG","CPRT","FE","HON","SCHW","PARA","FITB","GM","AMP","TSCO","DLTR","LYB","KHC","CSX","BK","PPL","NUE","XRAY","COO",
              "CRM","BBY","ROP","DLR","TYL","GD","AXP","JBHT","DUK","LH","LVS","NFLX","WFC","ETSY","NKE","MGM","CSGP","ES","MMC","C","DAY","CNP","NDSN","LRCX","SPGI",
              "STLD","BLDR","CSCO","IBM","ARE","RVTY","CF","TSN","EQR","AMGN","DHR","STE","AOS","PYPL","LEN","PEP","RCL","ANET","PH","ETR","REG","VFC","GWW","DG","HLT",
              "KDP","GLW","APTV","CTLT","HRL","PODD","SO","ADSK","KMI","PAYC","ALL","PWR","SBAC","MRO","AZO","JNJ","MSI","PGR","QRVO","HES","MA","HWM","MET","FICO","PXD",
              "VTR","LIN","AEP","KMX","ON","T","MDT","MTB","WM","STT","EFX","MCK","WDC","CVX","MO","WYNN","HPE","MDLZ","VMC","FDX","HBAN","CMI","IP","IT","LOW","BAX","DOC",
              "PSX","OXY","RSG","ABBV","FANG","BKR","MTCH","FTV","SPG","AIZ","PKG","POOL","MRK","TFC","DE","KMB","TTWO","DOV","BIO","INTC","APA","IDXX","EXPD","MMM","CTSH",
              "PEG","NOC","A","DIS","WBD","TJX","JNPR","LUV","BLK","HAS","AMZN","HOLX","SYY","TGT","HUBB","UBER","ICE","FMC","AEE","CZR","ORLY","PNR","DVA","PTC","HD",
              "NSC","TECH","EPAM","MLM","NWS","ADBE","ADI","ABT","DECK","JKHY","AIG","ESS","MCHP","UAL","CFG","AMT","ALGN","CLX","FSLR","MSFT","MRNA","ROK","V","ZTS",
              "IQV","KR","WAB","ITW","TRGP","IFF","COF","ANSS","AON","DAL","GE","RJF","TXT","CNC","UDR","ACGL","PAYX","XYL","CHTR","LDOS","INTU","CE","LW","BG","VRSK",
              "ETN","SWKS","NRG","AAPL","ACN","GPN","STX","INCY","TRV","PNC","CTRA","SYF","WELL","CBRE","SNPS","LLY","LHX","CME","ALLE","FTNT","QCOM","NXPI","FDS","NEE",
              "PCAR","BRO","MKTX","CPAY","GL","SJM","HST","WRK","TROW","BR","PSA","BDX","LKQ","AME","FFIV","MU","NTAP","TRMB","BXP","MCD","AAL","AMD","OMC","DFS","NVDA",
              "PM","RTX","UPS","ADM","PCG","STZ","BWA","GS","MPC","IPG","ODFL","INVH","CDNS","CPT","DD","CHD","NI"]

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

for c in range(3,100): 
    l = good_names[c:c+c]
    print("tickers = ", l)
    t = "qhrp05" + str(c)
    try:
        res = qhrp_query(q0(l, t))
        print(res["allocation"], res["perm"])
    except:
        pass
