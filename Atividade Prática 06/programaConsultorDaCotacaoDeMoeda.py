import requests
from datetime import datetime

moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

response = requests.get(url)
dados = response.json()

chave = moeda + "BRL"

if chave in dados:
    cotacao = dados[chave]

    valor_atual = cotacao["bid"]
    valor_max = cotacao["high"]
    valor_min = cotacao["low"]

    timestamp = int(cotacao["timestamp"])
    data_hora = datetime.fromtimestamp(timestamp)

    print(f"\nCotação {moeda} para BRL")
    print("Valor atual:", valor_atual)
    print("Máximo do dia:", valor_max)
    print("Mínimo do dia:", valor_min)
    print("Última atualização:", data_hora.strftime("%d/%m/%Y %H:%M:%S"))
else:
    print("Moeda inválida ou não encontrada.")
