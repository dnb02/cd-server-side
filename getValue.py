import requests
import json
import os

api = os.environ.get('CRYPTO_API')

Headers={
	'Accept': 'application/json'
}

parameters = {
	'CMC_PRO_API_KEY': api,
	'id' : '1,1839,4687,1831,2010,1975,4943,74,1027,2,6636,3890,5426,512,2416,825,3408,7083,3717,52'
}

list_id = [1,1839,4687,1831,2010,1975,4943,74,1027,2,6636,3890,5426,512,2416,825,3408,7083,3717,52]
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
response = requests.get(url,params=parameters)
recievedValue = response.json()
dumpValue = {}
for i in list_id:
	dumpValue[str(i)] = str(recievedValue['data'][str(i)]['quote']['USD']['price'])
with open('dump.json','w') as out:
	json.dump(dumpValue,out,indent=4)
