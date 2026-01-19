def calcular_idade_em_dias(ano_nascimento):
    ano_atual = 2026
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    return idade_em_dias

ano = int(input("Digite o ano de nascimento: "))
dias = calcular_idade_em_dias(ano)
print(f"Sua idade aproximada em dias é: {dias}")
