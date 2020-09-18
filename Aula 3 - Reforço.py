"""
importar biblioteca
"""
from random import randint

print(randint(10,100))

import numpy

print(numpy.sqrt(49))

"""
Listas
"""
valores = [1, 2.3, 105, 3]
nomes_cidades = ['Suzano', 'Itaqua', 'Poa', 'Mogi']

for nome in nomes_cidades:
    print(nome)

valores.sort()
print(valores)

"""
Dicionario
"""

cidade = {
    'nome': 'Suzano',
    'qtd_habitantes': '300000',
    'Referencia': 'Saldanha'
}

for chave, valor in cidade.items():
    print(chave, valor)

"""
Função
"""
def retornar_soma_numeros(a,b,c):
    return a + b + c
