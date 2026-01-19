def calcular_preco_com_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)   
    preco_final = preco - desconto                   
    return round(preco_final, 2)                    

preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto (%): "))

preco_final = calcular_preco_com_desconto(preco, percentual)

print(f"Preço final com desconto: R$ {preco_final:.2f}")
