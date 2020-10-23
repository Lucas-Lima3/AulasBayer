funcionarios = [
    {
        'nome': 'Bruno',
        'vendas': 0,
        'equipe': ['Ana','Diandra','Nico']
    },

    {
        'nome': 'Ana',
        'vendas': 300,
        'equipe': ['Bia', 'Camila']
    },

    {
        'nome': 'Diandra',
        'vendas': 450,
        'equipe': ['Maga', 'Fábio']
    },

    {
        'nome': 'Nico',
        'vendas': 500,
        'equipe': ['Lucas', 'Vini']
    },

    {
        'nome': 'Bia',
        'vendas': 100,
        'equipe': []
    },

    {
        'nome': 'Camila',
        'vendas': 350,
        'equipe': []
    },

    {
        'nome': 'Maga',
        'vendas': 200,
        'equipe': []
    },

    {
        'nome': 'Fabio',
        'vendas': 210,
        'equipe': []
    },

    {
        'nome': 'Lucas',
        'vendas': 150,
        'equipe': []
    },

    {
        'nome': 'Vini',
        'vendas': 100,
        'equipe': []
    },
]

def retornar_salario(funcionarios ,funcionario):
    for func in funcionarios:
        if func['nome'] == funcionario:
            dados_funcionarios = func

    time = dados_funcionarios['equipe']
    if len(time) == 0:
        salario_mortal = dados_funcionarios['vendas'] * 0.95
        return salario_mortal

    for func in funcionarios:
        contador = 0
        while contador < len(time):
            if func['nome'] == time[contador]:
                salario_lider = dados_funcionarios['vendas'] + (func['vendas'] * 0.05)
            contador += 1
        return salario_lider

print(retornar_salario(funcionarios ,'Bruno'))
