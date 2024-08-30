import json

def menor_valor(dados):
    menor = 0

    for i in dados:
        if i == dados[0] and i.get('valor') != 0:
            menor = i.get('valor')
        elif i.get('valor') < menor and i.get('valor') != 0:
            menor = i.get('valor')

    return menor

def maior_valor(dados):
    maior = 0

    for i in dados:
        if i.get('valor') > maior:
            maior = i.get('valor')

    return maior

def media(dados):
    soma = 0
    dias = 0

    for i in dados:
        if i.get('valor') != 0:
            soma = soma + i.get('valor')
            dias = dias + 1

    return soma / dias

def superior_media(dados):
    dias = 0
    for i in dados:
        if i.get('valor') > media(dados):
            dias = dias + 1

    return dias

with open('dados.json', 'r') as file:
    data = json.load(file)

print(f'O menor valor de faturamento ocorrido em um dia do mês foi R$ {menor_valor(data)}')
print(f'O maior valor de faturamento ocorrido em um dia do mês foi R$ {maior_valor(data)}')
print(f'Em {superior_media(data)} dias do mês, o valor de faturamento diário foi superior à média mensal')
