#!/usr/bin/env python3

""" Exibição de tabela
Crie uma função chamada printTable() que receba uma lista de listas de
strings e a exiba em uma tabela bem organizada, com cada coluna
justificada à direita. Suponha que todas as listas internas contenham o
mesmo número de strings. Por exemplo, o valor poderá ter o seguinte
aspecto:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

Sua função printTable() exibirá o seguinte:
    apples Alice dogs
    oranges Bob cats
    cherries Carol moose
    banana David goose

Dica: seu código inicialmente deverá localizar a string mais longa em
cada uma das listas internas para que a coluna toda tenha largura
suficiente para que todas as strings possam ser inseridas. Você pode
armazenar a largura máxima de cada coluna como uma lista de inteiros. A
função printTable() pode começar com colWidths = [0] * len(tableData),
que criará uma lista contendo o mesmo número de valores 0 que o número
de listas internas em tableData. Dessa maneira, colWidths[0] poderá
armazenar a largura da string mais longa de tableData[0], colWidths[1]
poderá armazenar a largura da string mais longa de tableData[1] e assim
por diante. Você poderá então identificar o maior valor na lista
colWidths e descobrir a largura na forma de um inteiro a ser passada
para o método de string rjust(). """


def printTable(tableData):
    """ Exiba em uma tabela bem organizada, com cada coluna justificada
    à direita. """

    # Criará uma lista contendo o mesmo número de valores 0 que o número
    # de listas internas em tableData.
    colWidths = [0] * len(tableData)

    # O laço while a seguir, armazena em colWidths[0] a largura da string
    # mais longa de tableData[0], em colWidths[1] a largura da string
    # mais longa de tableData[1] e assim por diante... 
    i = 0
    while i < len(tableData):
        st_length = []
        for st in tableData[i]:
            st_length.append(len(st))

        st_length.sort()
        colWidths[i] = st_length[-1]
        i += 1

    # Organiza a lista colWidths[] e atribui a maior largura na forma de
    # um inteiro na variavel width que é passada para o métoro de string
    # rjust().
    colWidths.sort()
    width = colWidths[-1]

    # O laço a seguir é responsável por exibir a tabela de forma
    # organizada, com cada coluna justificada à direita.
    j = 0
    while j < len(tableData):
        for item in tableData[j]:
            print(item.rjust(width), end=' ')

        print()
        j += 1


tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David', 'John'],
        ['dogs', 'cats', 'moose', 'goose'],
        ['England', 'Finland', 'France', 'Germany', 'Afghanistan']]

printTable(tableData)
