import requests
import sys

try:
    coins = float(sys.argv[1])
    print (coins)

except IndexError:
    print("Missing command-line argument")
    sys.exit
except ValueError:
    print("Command-line argument is not a number")
    sys.exit
except requests.RequestException:
    sys.exit