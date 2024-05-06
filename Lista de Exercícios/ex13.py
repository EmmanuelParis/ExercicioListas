temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março','Abril',
    'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print(f"Mês de {meses[i]}:")
    media = float(input("Digite a temperatura média: "))
    temperatura.append(media)
    
anual = sum(temperatura) / 12
for i in range(12):
    if temperatura[i] > anual:
        print(f"Temperatura a cima da média no mês: {meses[i]}")