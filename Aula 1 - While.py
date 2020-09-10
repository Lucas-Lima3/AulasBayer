qntd_contatos = int(input('Digite quantos contatos quer add: '))
contatos = []

while len(contatos) != qntd_contatos:
    contatos.append(input('digite um contato: '))
    contador =+ 1

contador = 1
for contato in contatos:
    print(f'Contato {contador}: ',contato)
    contador += 1
