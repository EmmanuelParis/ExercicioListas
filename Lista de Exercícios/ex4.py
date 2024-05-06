vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

palavra = input('Digite uma palavra: ')

for caractere in palavra:
    if caractere in vogais:
        contador += 1

print(f"Existem {len(palavra) - contador} consoantes")