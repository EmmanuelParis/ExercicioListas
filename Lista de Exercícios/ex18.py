votos = []
votoJogadores = []
numeroJogadores = []
numVoto = 1

while True:
    print(f"Voto {numVoto}:")
    voto = int(input("Digite o número do jogador: "))
    if voto == 0:
        break
    else:
        while voto > 23 or voto < 1:
            print("[Voto inválido.]")
            print(f"Voto {numVoto}:")
            voto = int(input("Digite o número do jogador: "))
        votos.append(voto)
    numVoto += 1
    
print(f"Total de votos: {len(votos)}")
contador = 1

for i in range(23):
    if contador not in votos:
        contador += 1
    else:
        votoJogadores.append(votos.count(contador))
        numeroJogadores.append(contador)
        print(f"Votos para o jogador camisa {contador} = {votos.count(contador)}")
        print(f"Percentual de votos: {round(100 * votos.count(contador) / len(votos), 2)}%")
        contador += 1
        
melhor = votoJogadores.index(max(votoJogadores))
print(f"Mais votado: {numeroJogadores[melhor]} com {votoJogadores[melhor]} votos")
print(f"Ganhou com {round(100 * votoJogadores[melhor] / len(votos), 2)}% dos votos")