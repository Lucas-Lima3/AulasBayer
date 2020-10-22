"""
Função com *args
"""

def receber_dados(*args):
    print(type(args))
    print(args)

receber_dados('Lucas', 'Suzano', 20, True)

"""
Função com **kwargs
"""

def retornar_dicionar(**kwargs):
    for c, v in kwargs.items():
        print(f'{c} - {v}')

retornar_dicionar(nome='Lucas', altura=1.81)
