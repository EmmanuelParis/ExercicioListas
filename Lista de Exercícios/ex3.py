notas = list()

for nota in range(4):
    nota = int(input('Digite uma nota: '))
    notas.append(nota)
    
print(f"Notas: {notas}\nMédia: {sum(notas) / len(notas)}")