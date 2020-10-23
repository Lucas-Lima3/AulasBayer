"""
Ler 4 numeros (N1,N2,N3,N4)
"""
notas = []
peso = [2,3,4,1]

notas.append(float(input('Digite n1: ')))
notas.append(float(input('Digite n2: ')))
notas.append(float(input('Digite n3: ')))
notas.append(float(input('Digite n4: ')))

def calcular_media(notas, peso):

    media = 0
    for item in range(len(notas)):
        media = media + (notas[item] * peso[item])

    media = media/sum(peso)

    return media

media = calcular_media(notas,peso)

print(f'Média: {calcular_media(notas,peso)}')

if media >= 7:
        print('Aluno aprovado.')

elif media < 5:
        print('Aluno Reprovado.')

else:
    print('Aluno em exame.')

    nota_exame = float(input('Digite nota exame: '))

    media_nova = (nota_exame + media) / 2

    print(f'Nota exame: {nota_exame}')

    if media_nova >= 5:
            print('Aluno aprovado')
            print(f'Média Final : {media_nova}')
    else:
            print('Aluno Reprovado')
            print(f'Média Final : {media_nova}')