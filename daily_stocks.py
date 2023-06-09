import requests
import os
import json

res = requests.post(
  url="https://api.tickertape.in/screener/query",
  headers={
      "Host": "api.tickertape.in",
      "Connection": "keep-alive",
      "Content-Length": "472",
      "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
      "Accept": "application/json, text/plain, */*",
      "sec-ch-ua-platform": "\"macOS\"",
      "accept-version": "7.11.0",
      "sec-ch-ua-mobile": "?0",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
      "Content-Type": "application/json;charset=UTF-8",
      "Origin": "https://www.tickertape.in",
      "Sec-Fetch-Site": "same-site",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
  },
  data=json.dumps({
"match": {},
"sortBy": "pr1d",
"sortOrder": -1,
"project": [
  "subindustry",
  "mrktCapf",
  "lastPrice",
  "pr1d",
  "pr1w",
  "4wpct",
  "26wpct",
  "52wpct"
],
"offset": 0,
"count": 10,
"sids": [
  "ACC",
  "ADEL",
  "ADNA",
  "APSE",
  "ADAG",
  "ADAI",
  "ABUJ",
  "APLH",
  "ASPN",
  "AVEU",
  "AXBK",
  "BPCL",
  "BAJA",
  "BJFN",
  "BJFS",
  "BJAT",
  "BANH",
  "BOB",
  "BRGR",
  "BAJE",
  "BRTI",
  "BION",
  "BOSH",
  "BRIT",
  "CHLA",
  "CIPL",
  "COAL",
  "COLG",
  "DABU",
  "DIVI",
  "DLF",
  "REDY",
  "EICH",
  "NYK",
  "GAIL",
  "GLAN",
  "GOCP",
  "GRAS",
  "HDFC",
  "HVEL",
  "HCLT",
  "HDFA",
  "HDBK",
  "HDFL",
  "HROM",
  "HLL",
  "HIAE",
  "HALC",
  "IOC",
  "INIR",
  "ICBK",
  "ICIL",
  "ICIR",
  "BHRI",
  "INBK",
  "INED",
  "INFY",
  "INGL",
  "ITC",
  "JSTL",
  "KTKM",
  "LART",
  "LIC",
  "LRTI",
  "MAHM",
  "MRCO",
  "MRTI",
  "MBFL",
  "MUTT",
  "NEST",
  "NTPC",
  "ONGC",
  "PAY",
  "PROC",
  "PIIL",
  "PIDI",
  "PGRD",
  "RELI",
  "MOSS",
  "SBIC",
  "SBIL",
  "SHCM",
  "SIEM",
  "SRFL",
  "SBI",
  "SUN",
  "TACN",
  "TAMO",
  "TTPW",
  "TISC",
  "TCS",
  "TEML",
  "TITN",
  "TORP",
  "ULTC",
  "UNSP",
  "UPLL",
  "VDAN",
  "WIPR",
  "ZOM"
]
})
).json()

li = []
text = '''*_NIFTY100 Top 10 Stocks Today_*\n\n'''
for i in res["data"]["results"]:
    li.append(i["stock"]["info"]["ticker"])
    text = text + f'''[{i["stock"]["info"]["ticker"]}] *{i["stock"]["info"]["name"]}*
_{i["stock"]["info"]["sector"]} / {i['stock']['advancedRatios']['subindustry']}_
```LTP/1D: {i['stock']['advancedRatios']["lastPrice"]}INR``` - ```{round(float(i['stock']['advancedRatios']["pr1d"]), 2)}%```
```1W/1M/6M/1Y: {round(float(i['stock']['advancedRatios']["pr1w"]), 2)}% / {round(float(i['stock']['advancedRatios']["4wpct"]), 2)}% / {round(float(i['stock']['advancedRatios']["26wpct"]), 2)}% / {round(float(i['stock']['advancedRatios']["52wpct"]), 2)}%```
-------------------------\n'''
    
headers = {"content-type": "text/plain"}


# print(text)

requests.post(f"{os.environ['IP']}/stonks", data=str(text), headers=headers)
