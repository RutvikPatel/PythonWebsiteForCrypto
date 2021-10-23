import requests


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': '10', 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'c7d607b1-aeb6-4507-afa2-7b8249afff77'}

    json = requests.get(url, params=parameters, headers=headers).json()

    coins = json['data']
    top_crypto_prices = []

    for x in coins:
        top_crypto_prices.append((x['symbol'], x['quote']['USD']['price']))

    return top_crypto_prices
