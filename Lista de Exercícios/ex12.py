alturas = []
idades = []
inferior = []

for i in range(30):
    print(f"Aluno {i+1}")
    altura = float(input("Digite a sua altura: "))
    alturas.append(altura)
    idade = int(input("Digite a sua idade: "))
    if idade > 13:
        idades.append(idade)

media = sum(alturas) / len(alturas)

for i in range(len(idades)):
    if idade[i] < media:
        inferior.append(idades[i])

print(f"Alunos com mais de 13 anos possuem altura inferior à média: {len(inferior)})")