while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2

        elif operacao == "-":
            resultado = num1 - num2

        elif operacao == "*":
            resultado = num1 * num2

        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2

        else:
            raise ValueError("Operação inválida")

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break 

    except ValueError:
        print("Erro: entrada inválida ou operação inválida. Tente novamente.\n")

    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida. Tente novamente.\n")