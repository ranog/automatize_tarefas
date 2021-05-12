#!/usr/bin/env python3

""" Códigos abreviados para classes comuns de caracteres:

\d - Qualquer dígito de 0 a 9.
\D - Qualquer caractere que não seja um dígito de 0 a 9.
\w - Qualquer letra, dígito ou o caractere underscore. (Pense nisso como
    uma correspondência de caracteres de “palavra”.)
\W - Qualquer caractere que não seja uma letra, um dígito ou o caractere
    underscore.
\s - Qualquer espaço, tabulação ou caractere de quebra de linha. (Pense
    nisso como uma correspondência de caracteres de “espaço”.)
\S - Qualquer caractere que não seja um espaço, uma tabulação ou uma
    quebra de linha.

As classes de caracteres são convenientes para reduzir as expressões
regulares. A classe de caracteres [0-5] corresponderá somente aos números de
0 a 5; isso é muito mais conciso do que digitar (0|1|2|3|4|5). """

import re


""" A expressão regular \d+\s\w+ corresponderá a textos que tenham um ou
mais dígitos (\d+) seguidos de um caractere de espaço em branco (\s)
seguido de um ou mais caracteres que sejam letra/dígito/underscore
(\w+). O método findall() retorna todas as strings que correspondam ao
padrão da regex em uma lista. """

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,\
        7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
