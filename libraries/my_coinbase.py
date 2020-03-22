from coinbase.wallet.client import Client

client = Client('api key', 'api secret', api_version="YYYY-MM-DD")
current_code = 'USD'

price = client.get_spot_price(currency=current_code)

print(f'Bitcoin price {current_code}: {price.amount}')