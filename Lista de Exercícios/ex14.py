sim = 0

perguntas = ["Telefonou para a vitima? [s/n]: ",
             "Esteve no local do crime? [s/n]: ",
             "Mora perto da vitima? [s/n]: ",
             "Devia para a vitima? [s/n]: ",
             "Já trabalhou com a vítima? [s/n]: "
             ]

for i in range(len(perguntas)):
    resposta = input(perguntas[i]).lower()
    if resposta == 's':
        sim += 1
        
if sim == 2:
    print("Você é suspeitO!")
elif sim > 2 and sim <= 4:
    print("Você é um cúmplice!")
elif sim == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente!")