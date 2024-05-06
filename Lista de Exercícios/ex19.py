votos = []
numero_votos = []
opcoes = ['Windows Server', 'Unix', 'Linux', 'NetWare', 'MacOS', 'Outro']
numVoto = 1

while True:
    print(f"Voto {numVoto}:")
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto > 6 or voto < 1:
            print("[Voto inválido]")
            print(f"Voto {numVoto}:")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    numVoto += 1

sistema = ("Sistema Operacional")
espaco1 = "      "
espaco2 = "   "
print_votos = "Votos"
print("\n" * 2)
print(f"Sistema Operacional       Votos           %")
print("-" * 50)

for i in range(len(opcoes)):
    numero_votos.append(votos.count(i + 1))
    print(f"{opcoes[i]} {" " * (19 - len(opcoes[i]) + len(print_votos) + 3)} {votos.count(i + 1)} {" " * 6} {round(100 * votos.count(i + 1) / len(votos), 2)} %")

indice_ganhador = numero_votos.index(max(numero_votos))
print(f"O sistema mais votado foi o {opcoes[indice_ganhador]} com {numero_votos[indice_ganhador]} votos.")
print(f"Equivalente a {round(100 * numero_votos[indice_ganhador] / len(votos), 2)}% dos votos.")