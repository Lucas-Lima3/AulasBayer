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



"""
Groger Bank
    Criar funções para os seguintes comportamentos:
        Cadastro: Só é possível cadastrar maiores ou igual a 18 anos
        Depósito: Sitema não aceita depositos negativos
        Saque: Valor não pode ser maior que o saldo
               Não pode ser negativo 
               Não pode ser maior que 900
        Emprestimo: Valor não pode ser maior que 10vezes o salario
                    Se aceito: Saldo ganha um aumento e sucesso
                    Se não: Recusado
"""

print('EXERCÍCIO 3')

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Voce não pode se cadastrar.')
else:
    salario = float(input('Digite seu salário: '))
    operacao = input('Selecione Operação: [D] para Depósito, [S] para Saque, [E] para empréstimo: ')
    if operacao == 'D':
        valor_deposito = float(input('Digite valor a ser depositado: '))
        if valor_deposito < 0:
            print('Não pode depositar valor negativo.')
        else:
            print('Operação bem-sucedida.')
    if operacao == 'S':
        valor_saque = float(input('Digite valor a ser sacado: '))
        if valor_saque > salario or valor_saque < 0 or valor_saque > 900:
            print('Não pode sacar esse tipo de valor.')
        else:
            print('Operação bem-sucedida.')
    if operacao == 'E':
        valor_emprestimo = float(input('Digite valor que quer emprestimo: '))
        if valor_emprestimo > 10*salario:
            print('Valor é muito alto')
        else:
            print('Operação bem-sucedida.')

print()

