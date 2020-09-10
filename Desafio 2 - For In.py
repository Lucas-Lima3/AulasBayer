frase = input('Digite uma frase: ')
letra_desejada = input('Digite a letra que quer contar: ')
contador = 0

for letra in frase:
    if letra_desejada == letra:
        contador += 1
print(contador)
