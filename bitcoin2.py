import requests

def get_exchange_rate(from_currency, to_currency):
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}".format(from_currency, to_currency)
    response = requests.get(api_url)
    data = response.json()
    rate = data[from_currency][to_currency]
    return rate



# Example usage:
from_currency = "bitcoin"
to_currency = "usd"
rate = get_exchange_rate(from_currency, to_currency)
print("1 {} = {} {}".format(from_currency.capitalize(), rate, to_currency.upper()))

