senha_valida = False

while True:
    try:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        if not any(caractere.isdigit() for caractere in senha):
            raise ValueError("A senha deve conter pelo menos um número.")

        senha_valida = True

    except ValueError as erro:
        print(f"Senha fraca: {erro}")

    finally:
        if senha_valida:
            print("Senha forte cadastrada com sucesso!")
    if senha_valida:
        break       

