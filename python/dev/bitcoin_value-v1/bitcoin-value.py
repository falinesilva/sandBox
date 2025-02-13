import requests
import sys

def main():
    """
    Converts a given number of Bitcoins to USD using the current exchange rate from CoinGecko.
    """
    
    try:
        n = float(sys.argv[1])
    except IndexError:
        print("Missing command-line argument")
        sys.exit()
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()

    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()

        # Extract the Bitcoin price in USD
        usd = data['bitcoin']['usd']
        
        result = usd * n
        print(f"${result:,.4f}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: Cannot connect to server.\n\nRun 'ping api.coingecko.com")
        sys.exit()

if __name__ == "__main__":
    main()
