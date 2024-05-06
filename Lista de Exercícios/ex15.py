notas = []
maiorQueMedia = []
menorQue7 = []
nota = True
while nota != -1:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)
        
print(f"Valores lidos: {len(notas)}")
print(f"Valores na ordem: {notas}")

print("Valores na ordem inversa à que foram informados, um abaixo do outro: ")
notas.reverse()
for i in range(len(notas)):
    print(notas[i])
    
print(f"Soma dos valores: {sum(notas)}")
media = sum(notas) / len(notas)
print(f"Média dos valores: {media}")

for i in range(len(notas)):
    if notas[i] > media:
        maiorQueMedia.append(notas[i])
        
print(f"Quantidade de valores acima da média: {len(maiorQueMedia)}")
for i in range(len(notas)):
    if notas[i] < 7:
        menorQue7.append(notas[i])
        
print(f"Quantidade de notas abaixo de 7: {len(menorQue7)}")   
print("Fim do programa.")