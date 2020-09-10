qntd_numeros = int(input('Quantos números? '))
contador = 0
numeros = []

while qntd_numeros > contador:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    contador = contador + 1

media = sum(numeros) / len(numeros)

print(f'A média entre os números que voce forneceu é: {media}.')