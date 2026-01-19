def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

conta = 150.00
porcentagem = 10

valor_gorjeta = calcular_gorjeta(conta, porcentagem)
print(f"Gorjeta: R$ {valor_gorjeta:.2f}")