import json

# Lê os dados do arquivo JSON
with open("faturamento.json", "r") as f:
    dados = json.load(f)
    
    
# Calcula o maior valor de faturamento de acordo com o arquvio JSON
maiorValor = max(dados.values())

# Calcula o menor valor de faturamento de acordo com o arquivo JSON
menorValor = min(dados.values())

# Calcula a média mensal de faturamento, excluindo dias onde o faturamento foi de R$:0,00 ou seja, dias que não houve faturamento
dias_com_faturamento = [valor for valor in dados.values() if valor > 0]
media = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for valor in dados.values() if valor > media)

# Exibe os resultados
print("Valor de menor faturamento diário:", menorValor)
print("Valor de maior faturamento diário:", maiorValor)
print("Número de dias acima da média mensal:", dias_acima_da_media)
