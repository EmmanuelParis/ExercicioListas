idades = []
alturas = []
numPessoa = 1

for i in range(5):
    print(f"Pessoa {numPessoa}: ")
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    altura = float(input("Digite a altura: "))
    alturas.append(altura)
    numPessoa += 1

idades.reverse()
alturas.reverse()

print(f"Idades: {idades} \n Alturas: {alturas}")