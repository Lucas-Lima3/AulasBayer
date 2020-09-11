from random import randint

numeros = []

for contador in range(10):
    aleatorio = randint(1,100)
    numeros.append(aleatorio)
    contador += 1

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Lista : {numeros}')
print(f'Pares : {pares}')
print(f'Impares : {impares}')
