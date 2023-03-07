#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

# Define o os valores de faturamento de cada estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o total de faturamento de todos os valores definido acima com a função "sum"
total = sum(faturamento.values())

# Calcula o percentual de faturamento de cada estado
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

# Exibe os resultados percentuais com 2 casas decimais usando "for" para percorrer todas as chaves e valores de "percentuais"
for estado, percentual in percentuais.items():
    print(estado, "-", "{:.2f}%".format(percentual))