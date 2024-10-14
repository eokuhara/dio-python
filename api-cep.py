import requests
import json

link_api = "https://cep.awesomeapi.com.br/json/08615350"

requisicao = requests.get(link_api)

requisicao = requisicao.json()

print(json.dumps(requisicao, indent=3))

with open("consutal_cep.txt", "w", encoding="utf-8") as file:
    json.dump(requisicao, file, ensure_ascii=False, indent=3)