"""
João e Maria fizeram uma prova na escola.
Crie um algoritmo que corrija as provas comparando com o gabarito
Imprima a nota de cada aluno considerando o peso de cada nota



Pergunta | Joao | Maria | Gabarito | Peso
1        |  C   |   C   |    A     |  3
2        |  A   |   D   |    A     |  3
3        |  D   |   D   |    B     |  3
4        |  B   |   D   |    A     |  3
5        |  D   |   D   |    A     |  3
"""

#FAZER DO JEITO MAIS FACIL POSSIVEL !!!!!!

alunos = [
    {
        'nome': 'João',
        'respostas': ['C', 'A', 'D', 'B', 'D']
    },
    {
       'nome': 'Maria',
        'respostas': ['C', 'D', 'D', 'D', 'D']
    }
]

gabarito = ['A', 'A', 'B', 'A', 'A']

peso = [3, 2, 1, 1, 3]

#FAZER DO JEITO MAIS FACIL POSSIVEL !!!!!!

def retornar_nota_prova(lista_alunos, gabarito, peso, posicao_aluno):
    aluno = lista_alunos[posicao_aluno]
    lista_respostas = aluno['respostas']
    nome_aluno = aluno['nome']
    contador_gabarito = 0
    contador_peso = 0
    nota_aluno = 0
    for resposta in lista_respostas:
        if resposta == gabarito[contador_gabarito]:
            nota_aluno = nota_aluno + peso[contador_peso]
        contador_gabarito = contador_gabarito + 1
        contador_peso = contador_peso + 1
    print(f'A nota do(a) aluno(a) {nome_aluno} foi {nota_aluno}')

print(retornar_nota_prova(alunos, gabarito, peso, 0))
print(retornar_nota_prova(alunos, gabarito, peso, 1))


#Não sei porque aparece o NONE


"""
Jeito Groger
"""

gabarito = ['A', 'A', 'B', 'A', 'A']

peso = [3, 2, 1, 1, 3]

alunos = {
    'joao': ('C', 'D', 'A', 'B', 'D'),
    'maria': ('A', 'B', 'A', 'A', 'D')
}

for nome in alunos:
    aluno_respostas = alunos[nome]

    ponto = 0
    for item in range(len(gabarito)):
        if gabarito[item] == aluno_respostas:
            ponto += peso[item]

    print(nome, ponto)
