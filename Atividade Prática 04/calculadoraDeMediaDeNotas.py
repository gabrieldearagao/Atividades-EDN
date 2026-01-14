soma_notas = 0
quantidade = 0

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            soma_notas += nota
            quantidade += 1
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if quantidade > 0:
    media = soma_notas / quantidade
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")