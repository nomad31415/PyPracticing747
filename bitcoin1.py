import requests

def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency}"
    response = requests.get(api_url)
    data = response.json()
    rate = data[from_currency][to_currency]
    return rate


# Example: Convert USD to Bitcoin
from_currency = "bitcoin"  # For CoinGecko, cryptocurrency IDs are used instead of symbols
to_currency = "usd"
rate = get_exchange_rate(from_currency, to_currency)
print(f"1 Bitcoin = {rate} USD")



