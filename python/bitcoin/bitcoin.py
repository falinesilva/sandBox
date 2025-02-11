import json
import requests
import sys

# Ask the user for the number of Bitcoins they want to convert

try:
    n = float(sys.argv[1])
    print (n)

except IndexError:
    print("Missing command-line argument")
    sys.exit
except ValueError:
    print("Command-line argument is not a number")
    sys.exit
except requests.RequestException:
    sys.exit

# Request the current Bitcoin value in USD

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# Outputs the current cost of Bitcoins in USD to four decimal places

o = response.json()
usd = float(o["bpi"]["USD"]["rate"].replace(',', ''))
result = (usd * n)
print(f"${result:,.4f}")