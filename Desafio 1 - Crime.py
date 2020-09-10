"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice"
e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
print('Digite 1 para Sim e 0 para não')

respostas = []

respostas.append(int(input('Telefonou para a vítima? ')))
respostas.append(int(input('Esteve no local do crime? ')))
respostas.append(int(input('Mora perto da vítima? ')))
respostas.append(int(input('Devia para a vítima? ')))
respostas.append(int(input('Já trabalhou com a vítima? ')))

quantidade_sim = sum(respostas)

if quantidade_sim == 2:
    print('Suspeito')
elif quantidade_sim >=3 and quantidade_sim <=4:
    print('Cumplice')
elif quantidade_sim == 5:
    print('Assasino')
else:
    print('Inocente')