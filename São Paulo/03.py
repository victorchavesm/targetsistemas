import json

with open('03.json', 'r') as file:
    faturamento_diario = json.load(file)

dias_validos = [entrada['faturamento'] for entrada in faturamento_diario if entrada['faturamento'] > 0]

menor_faturamento = min(dias_validos)
maior_faturamento = max(dias_validos)
media_faturamento = sum(dias_validos) / len(dias_validos)
dias_acima_da_media = sum(1 for faturamento in dias_validos if faturamento > media_faturamento)

print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_faturamento}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_faturamento}")
print(f"Número de dias no mês com faturamento diário superior à média mensal: {dias_acima_da_media}")

