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