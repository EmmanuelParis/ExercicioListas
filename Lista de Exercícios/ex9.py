a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = []

for numero in a:
    quadrados.append(numero * numero)
    
print(f"Soma dos quadrados: {sum(quadrados)}")