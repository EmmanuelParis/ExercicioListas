import random
numeros = []
par = []
impar = []


for i in range(20):
    numAleatorio = numeros.append(random.randrange(0, 1000))

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números: {numeros} \n\nÍmpar: {impar} \n\nPar: {par}")