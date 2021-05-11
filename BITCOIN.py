import requests

address = 'https://api.coindesk.com/v1/bpi/currentprice.json'

bitcoinData = requests.get(address).json()

getTimeUpdated = bitcoinData["time"]["updated"]
getDescription = bitcoinData["disclaimer"]
getBitcoinPriceUSD = bitcoinData["bpi"]["USD"]["rate"]

print('Updated on :' , getTimeUpdated)
print(getDescription)
print(getBitcoinPriceUSD)
