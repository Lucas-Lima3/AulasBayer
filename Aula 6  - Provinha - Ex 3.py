"""
Exercicio 3
"""

numeros = []

quantidade_numeros = int(input('Digite a quantidade de numeros que quer que entre: '))
for i in range(quantidade_numeros):
    numeros.append(int(input(f'Digite o numero {i+1}: ')))

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

print(f'Teve {len(pares)} pares ')