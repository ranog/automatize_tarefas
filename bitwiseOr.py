"""
Podemos combinar as variáveis re.IGNORECASE, re.DOTALL e re.VERBOSE
utilizando o caractere pipe (|) que, nesse contexto, é conhecido como o
operador ou bit a bit (bitwise or).

Portanto, se quiser uma expressão regular que ignore as diferenças entre
letras maiúsculas e minúsculas e inclua quebras de linha para que
correspondam ao caractere ponto, sua chamada a re.compile() deverá ser feita
da seguinte forma:
"""

import re

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

print(someRegexValue)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

print(someRegexValue)
