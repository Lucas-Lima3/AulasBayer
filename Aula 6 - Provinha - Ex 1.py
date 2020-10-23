"""
Exercício 1 :

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar

Código |  Especificação  | Preço
  1    | Cachorro Quente |   4
  2    |    X-Salada     |   4.5
  3    |    X-Bacon      |   5
  4    | Torrada Simples |   2
  5    |   Refrigente    |   1.5

************************************************************
Entrada
    O arquivo de entrada contém dois valores inteiros correspondentes ao código
    e a quantidade de um item conforme tabela acima

Saída
    O arquivo de saída deve conter a mensagem "Total:R$" seguido pelo valor a ser pago
    com 2 casas após o ponto decimal
************************************************************
"""

cardapio = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5
}

def calcular_valor(codigo,quantidade):
    preco_final = (cardapio[codigo] * quantidade)
    return preco_final

print(f'Total: R$ {calcular_valor(3,2):.2f}')
