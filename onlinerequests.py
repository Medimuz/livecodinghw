import requests

API = 'h1ewiRI78UxdSwTdPr9AJ67MlJHsPi7GjffFIgfI'

HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API}&currencies=EUR%2CUSD%2CRUB%2CGBP'

response = requests.get(HOST)

CURRENCIES = response.json()['data']