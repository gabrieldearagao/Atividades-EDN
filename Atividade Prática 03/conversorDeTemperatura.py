temperatura = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").upper()
destino = input("Informe a unidade de destino (C, F ou K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32

elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15

elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9

elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15

elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15

elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32

elif origem == destino:
    resultado = temperatura

else:
    print("Unidade inválida!")
    resultado = None

if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f}°{destino}")
