


import requests

API_URL = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(API_URL)

users = response.json()
for u in users:
	print(u)

#print("Status code", response.status_code)

#user = input("Digite o seu e-mail: ")
#pass = input("Digite uma senha: ")

data = {'name': input("Digite seu nome: "),
		'email': input("Digite seu email: "),
		'password':input("Digite seu password: ")}

r = requests.post(url = API_URL, json = data)

if r.status_code == 200:
	user_id = r.json()['id']
	print(user_id)
else:
	print("erro ao cadastrar")