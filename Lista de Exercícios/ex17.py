numAtleta = True

while True:
    saltos = []
    print(f"Atleta {numAtleta}: ")
    atleta = input("Digite o nome do atleta: ")
    if atleta == '':
        break
    
    else:
        numSalto = 1
        for i in range(5):
            print(f"Salto {numSalto}: ")
            distancia = float(input("Digite a distância do salto: "))
            saltos.append(distancia)
            numSalto += 1
            
        print("Atleta: ", atleta)
        numSalto = 1
        for i in range(5):
            print(f"{numSalto}° Salto : {saltos[i]}m")
            numSalto += 1
            
        print("Resultado Final:")
        print(f"Atleta: {atleta}")
        print(f"Saltos: {saltos}")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        
        media = sum(saltos) / len(saltos)
        print(f"Média dos saltos: {round(media, 2)}")
        numAtleta += 1