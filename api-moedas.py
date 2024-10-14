import requests

link_api = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

requisicao = requests.get(link_api)

print(requisicao.status_code)
print(requisicao.json())