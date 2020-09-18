"""
Dicionário com for
    Crie um dicionário e itere com for suas informações.
"""
print('EXERCÍCIO 1')
dadospessoais = {
    'Nome': 'Lucas',
    'Idade': 20,
    'Altura': 1.81,
    'Pai': 'Claudio',
    'Mãe': 'Luciana'
}

for item in dadospessoais:
    print(f'{item} : {dadospessoais[item]}')

print()



"""
Retornar maior valor
    Crie uma função que receba como argumento 3 valores, e retorne qual o maior valor.
"""

print('EXERCÍCIO 2')

numeros = []

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite outro número: '))

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

print(max(int(numero) for numero in numeros))

print()
