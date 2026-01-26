import csv

nome_arquivo = input("Informe o nome do arquivo CSV: ")

try:
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        print("\nConteúdo do arquivo CSV:\n")

        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as erro:
    print("Ocorreu um erro ao ler o arquivo.")
    print("Erro:", erro)
