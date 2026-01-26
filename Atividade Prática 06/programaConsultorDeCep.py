import requests

cep = input("Informe o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

dados = response.json()

if "erro" not in dados:
    print("Endereço encontrado:")
    print("Logradouro:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])
else:
    print("CEP inválido ou não encontrado.")