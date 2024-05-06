aprovados = []
numAluno = 1

for aluno in range(10):
    notas = []
    print(f"Aluno {numAluno}")
    for nota in range(4):
        nota = float(input(f"Digite a nota {nota+1}: "))
        notas.append(nota)
        while nota > 10 or nota < 0:
            print("[Nota inválida]")
            nota = notas.append(float(input(f"Digite a nota {nota+1}: ")))
    media = sum(notas) / len(notas)
    if media >= 7:
        aprovados.append(media)
    numAluno += 1
    
print(f"Número de alunos com média 7 ou maior: {len(aprovados)}")