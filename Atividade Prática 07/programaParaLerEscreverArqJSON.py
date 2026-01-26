import json

dados = {
    "nome": "Bleach",
    "ano": 2004,
    "país": "Japão",
    "protagonista": "Kurosaki Ichigo"

}

nome_arquivo = input("Informe o nome do arquivo JSON (ex: dados.json): ")

try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Dados salvos com sucesso no arquivo JSON!")

except Exception as erro:
    print("Falha ao salvar o arquivo.")
    print("Erro:", erro)

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("\nDados lidos do arquivo JSON:")
    print("Nome:", dados_lidos["nome"])
    print("Ano:", dados_lidos["ano"])
    print("País de Origem:", dados_lidos["país"])
    print("Protagonista:", dados_lidos["protagonista"])

except FileNotFoundError:
    print("Falha ao ler o arquivo: arquivo não encontrado.")
except Exception as erro:
    print("Falha ao ler o arquivo.")
    print("Erro:", erro)
