

import requests

CEP = input("Digite o CEP: ")

VIACEP_URI = "http://viacep.com.br/ws/{0}/json/".format (CEP)
response = requests.get(VIACEP_URI)



print("Status code", response.status_code)
print("Texto Plano", response.text)
print("Dicionario Python", response.json())