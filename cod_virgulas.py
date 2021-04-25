#!/usr/bin/env python3

def cod_virgulas(spam):
    """ Imprime todos os itens separados por uma vírgula e um espaço,
    com and inserido antes do último item. """

    new_spam = []

    # inserir ',' aos itens da lista original, excluindo os dois últimos.
    for item in spam[:-2]:
        new_spam.append(item + ',')

    # inserir os dois últimos itens da lista original.
    new_spam.append(spam[-2])
    new_spam.append(spam[-1])

    # inserir a string 'and' antes do último item da nova lista.
    new_spam.insert(-1, 'and')

    # imprimir nova lista: nova_lista[0], nova_lista[1], ... nova_lista[n].
    print(*new_spam)


spam = []

try:
    while True:
        item = input("Entre com um item: ")
        print("Ou pressione ENTER para sair.")

        if item == '':
            break
        else:
            spam.append(item)

    cod_virgulas(spam)

except:
    print("Sua sessão foi encerada.")
