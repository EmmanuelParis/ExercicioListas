intervalos = [
    [200,299],[300,399],[400,499],
    [500,599],[600,699], [700,799],
    [800,899],[900,999]
    ]
quantidades = [0,0,0,0,0,0,0,0,0]
salarios = []
vendas = 1

while vendas != 0:
    vendas = float(input("Digite o valor das vendas: "))
    if vendas == 0:
        break
    else:
        salario = (vendas * 0.09) + 200
        if salario < 1000:
            for i in range(len(intervalos)):
                if salario > intervalos[i][0] and salario < intervalos[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
for i in range(len(intervalos)):
    print(f"Entre R${intervalos[i][0]} e R${intervalos[i][1]}: {quantidades[i]}")
    
print(f"Salários maiores que R$1000: {quantidades[-1]}")