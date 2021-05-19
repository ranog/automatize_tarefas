"""
O método sub() dos objetos Regex recebe dois argumentos. O primeiro
argumento é uma string para substituir qualquer correspondência. O
segundo é a string para a expressão regular. O método sub() retorna uma
string com as substituições aplicadas.
"""

import re

namesRegex = re.compile(r'Agent \w+')
nog = namesRegex.sub('CENSORED', 'Agent gave the secret documents to Agent Bob.')

print(nog)


"""
No primeiro argumento de sub(), podemos digitar \1, \2, \3 e assim por
diante para dizer "insira o texto do grupo 1, 2, 3 e assim por diante na
substituição".
"""

namesRegex = re.compile(r'Agent (\w)\w*')
nog = namesRegex.sub(r'\1*****', 'Agent Alice told Agent Carolina that Agent Eve knew Agent Bob was a double agent.')

print(nog)
