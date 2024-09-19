import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

o = response.json()

usd = o["bpi"]["USD"]["rate_float"]
price = usd * float(sys.argv[1])
print(f'${price:,.4f}')