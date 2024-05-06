defeitos = ['Necessita da esfera',
            'Necessita de limpeza',
            'Necessita troca do cabo ou conector',
            'Quebrado ou inutilizado'
            ]
numIdentificacao = []
numDefeitos = []
numMouse = 1

while True:
    print(f"Mouse {numMouse}")
    identificacao = int(input("Digite o número de identificação do mouse: "))
    if identificacao == 0:
        break
    else:
        while identificacao in numIdentificacao:
            print("[Número inválido]")
            print(f"Mouse {numMouse}")
            identificacao = int(input("Digite o número de identificação do mouse: "))
        numDefeito = int(input("Digite o número correspondente ao defeito: "))
        while numDefeito > 4 or numDefeito < 1:
            print("[Número inválido]")
            numDefeito = int(input("Digite o número correspondente ao defeito: "))
        numIdentificacao.append(identificacao)
        numDefeitos.append(numDefeito)
    numMouse += 1
    
print(f"Quantidade de mouses: {len(numIdentificacao)}")

for i in range(len(defeitos)):
    print('\n' * 2)
    print(f"Defeito: {defeitos[i]} --- Quantidade: {numDefeitos.count(i + 1)} --- Porcentagem: {round(100 * numDefeitos.count(i + 1) / len(numIdentificacao), 2)}%")
    print('\n' * 2)