import csv

pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Bruno", 30, "Rio de Janeiro"],
    ["Carla", 22, "Belo Horizonte"]
]

nome_arquivo = input("Informe o nome do arquivo (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(pessoas)

    print("Arquivo CSV salvo com sucesso!")

except Exception as erro:
    print("Falha ao salvar o arquivo.")
    print("Erro:", erro)
