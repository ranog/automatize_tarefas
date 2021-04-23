#!/usr/bin/env python3

""" Observe a expressão usada como índice de messages:

random.randint(0, len(messages) - 1)

Isso gera um número aleatório a ser usado como índice, independentemente
do tamanho de messages, ou seja, você obterá um número aleatório entre 0
e o valor len(messages) - 1. A vantagem dessa abordagem é que você pode
facilmente adicionar e remover strings da lista messages sem alterar
outras linhas de código. Se o seu código for atualizado mais tarde,
haverá menos linhas a serem alteradas e menos chances de introduzir
bugs. """

import random

messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
