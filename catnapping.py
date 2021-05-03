#!/usr/bin/env python

print("""Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob.""")

""" Observe que o caractere único de aspas simples em Eve's não precisa
ser escapado. Escapar aspas simples e duplas é opcional em strings
multinhas. """

print("""

A chamada a print() a seguir exibirá um texto idêntico, porém
não utiliza uma string de múltiplas linhas: """)

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat \
burglary, and extortion.\n\nSincerely,\nBob.')
