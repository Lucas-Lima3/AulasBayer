def retornar_verificacao_numero(x):
    if x > 0:
        return('POSITIVO')
    elif x < 0:
        return('NEGATIVO')
    else:
        return('NEUTRO')

print(retornar_verificacao_numero(-10))
