def percentual_rep(total, dados):
    for i in dados:
        porcentagem = (i.get('valor') * 100) / total
        print(f'O estado {i.get('estado')} teve um percentual de representação de {porcentagem}%')

estados = [{'estado': 'SP', 'valor': 67836.43},
           {'estado': 'RJ', 'valor': 36678.66},
           {'estado': 'MG', 'valor': 29229.88},
           {'estado': 'ES', 'valor': 27165.48},
           {'estado': 'Outros', 'valor': 19849.53}
           ]
total = sum(item['valor'] for item in estados)

percentual_rep(total, estados)
