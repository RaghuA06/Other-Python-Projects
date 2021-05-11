import requests

# API KEY = 7a5883b5a6559dd16b1a897c78521462

address = 'http://data.fixer.io/api/latest?access_key='

api_key = '7a5883b5a6559dd16b1a897c78521462'

url =  address + api_key

data = requests.get(url).json()

print(data)
