salarios = []
abonos = []
numFuncionario = 1

while True:
    print(f"Funcionario {numFuncionario}")
    salario = float(input("Digite o salário: "))
    if salario == 0:
        break
    else:
        while salario < 0:
            print("[salario inválido]")
            print(f"Funcionario {numFuncionario}")    
            salario = float(input("Digite o salário: "))
        abono = abonos.append(salario * 0.2)
        salarios.append(salario)
    numFuncionario += 1

minimo = 0
for i in range(len(salarios)):
    if abonos[i] <= 100:
        print(f"Salario = R${salarios[i]} - Abono = R$100.0")
        abonos[i] = 100
        minimo += 1
    print(f"Salario = R${salarios[i]} - Abono = R${abonos[i]}")
    
print(f"Foram processados {len(salarios)} colaboradores.")
print(f"Total gasto com abonos: R${sum(abonos)}")
print(f"Valor minimo pago a {minimo} colaboradores.")
print(f"Maior valor de abono pago: {max(abonos)}")