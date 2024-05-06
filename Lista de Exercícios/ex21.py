veiculos = ['Fusca', 'Palio', 'UNO', 'Ferrari', 'HB20']
consumo = []

for i in range(5):
    print(f"Veiculo {i + 1}\nNome: {veiculos[i]}")
    kmLitro = float(input("KM por litro: "))
    consumo.append(kmLitro)

print("Relatório final: ")
for i in range(5):
    print(f"{i+1} - {veiculos[i]} = {consumo[i]} - {round(1000 / consumo[i], 2)} litros - R${round(1000 / consumo[i] * 2.25, 2)}")
menorConsumo = consumo.index(max(consumo))
print(f"O menor consumo é o do {veiculos[menorConsumo]}")