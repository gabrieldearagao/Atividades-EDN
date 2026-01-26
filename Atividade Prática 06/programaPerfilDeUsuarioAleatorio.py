import  requests

url = "https://randomuser.me/api/"

response = requests.get(url)

dados = response.json()

usuario = dados['results'][0]

nome = f"{usuario['name']['first']} {usuario['name']['last']}"

email = usuario['email']

pais = usuario['location']['country']

print('Perfil de Usuário Gerado com Sucesso:')

print("nome:", nome)
print("Email:", email)
print("País:", pais)