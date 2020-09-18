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



"""
Piscina
    Calcule a quantidade de litros de uma piscina:
        Crie um programa que utilize as 3 dimensões de uma piscina para calcular quantos litros de água ela comporta em litros. 
        Imprima apenas o resultado no console. Utilize uma função pare resolver esse exercício.
        Dica: 1m³ = 1000 litros
"""
print('EXERCÍCIO 4')

def quantidade_litros():
    altura = float(input('Qual a altura da piscina em metros: '))
    largura = float(input('Qual a largura da piscina em metros: '))
    comprimento = float(input('Qual o comprimento da piscina em metros: '))

    metros_cubicos = altura * largura * comprimento
    litros = metros_cubicos * 1000

    return litros

print(quantidade_litros())

print()



"""
Salário com Bônus
    Faça um programa que leia :
        - o nome de um vendedor, 
        - o seu salário fixo 
        - e o total de vendas efetuadas por ele no mês (em dinheiro). 
    Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
"""

print('EXERCÍCIO 5')

def salario_com_bonus():
    nome_funcionario = input('Nome: ')
    salario_funcionario = round(float(input('Salario: ')), 2)
    vendas_funcionario = round(float(input('Vendas: ')), 2)

    total_salario = round(salario_funcionario + (vendas_funcionario*1.15), 2)

    return total_salario

print(salario_com_bonus())

print()



"""
Área do Círculo
    A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
    Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
"""

print('EXERCÍCIO 6')


def area_circulo():
    raio = round(float(input('Raio: ')), 2)

    area = round(raio * 3.14159 * 2, 4)

    return area

print(area_circulo())

print()



"""
Fórmula de Bhaskara
    Leia 3 valores floats e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
    mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
"""

print('EXERCÍCIO 7')

def bhaskara():
    a = float(input('digite o valor de a: '))
    b = float(input('digite o valor de b: '))
    c = float(input('digite o valor de c: '))

    delta = (b**2) -4 * a * c

    if delta < 0:
        print('Impossivel calcular')
    else:
        funcao_bhaskara_mais = (- b + (delta ** 0.5)) / (2 * a)
        funcao_bhaskara_menos = (- b - (delta ** 0.5)) / (2 * a)

        return funcao_bhaskara_mais, funcao_bhaskara_menos

print(bhaskara())

print()
