""" 
    Correspondendo a quebras de linha com o caractere ponto.

    O ponto-asterisco corresponderá a qualquer caractere, exceto uma
    quebra de linha.

    Ao passar re.DOTALL como segundo argumento de re.compile(), podemos
    fazer o caractere ponto corresponder a todos os caracteres,
    incluindo o caractere de quebra de linha.

    A regex noNewlineRegex, criada sem que re.DOTALL tenha sido passado
    para a chamada a re.compile(), corresponderá a qualquer caractere
    até o primeiro caractere de quebra de linha, enquanto newlineRegex,
    que teve re.DOTALL passado para re.compile(), corresponderá a todos
    os caracteres.

    É por isso que a chamada a newlineRegex.search() corresponde à
    string completa, incluindo seus caracteres de quebra de linha.

------------------------------------------------------------------------

Revisão dos símbolos de regex

• ? corresponde a zero ou uma ocorrência do grupo anterior.
• * corresponde a zero ou mais ocorrências do grupo anterior.
• + corresponde a uma ou mais ocorrências do grupo anterior.
• {n} corresponde a exatamente n ocorrências do grupo anterior.
• {n,} corresponde a n ou mais ocorrências do grupo anterior.
• {,m} corresponde a zero até m ocorrências do grupo anterior.
• {n,m} corresponde a no mínimo n e no máximo m ocorrências do grupo
anterior.
• {n,m}? ou *? ou +? faz uma correspondência nongreedy do grupo anterior.
• ^spam quer dizer que a string deve começar com spam.
• spam$ quer dizer que a string dever terminar com spam.
• . corresponde a qualquer caractere, exceto os caracteres de quebra de linha.
• \d, \w e \s correspondem a um dígito, um caractere de palavra ou um
caractere de espaço, respectivamente.
• \D, \W e \S correspondem a qualquer caractere, exceto um dígito, um
caractere de palavra ou um caractere de espaço, respectivamente.
• [abc] corresponde a qualquer caractere que estiver entre os colchetes (por
exemplo, a, b ou c).
• [^abc] corresponde a qualquer caractere que não esteja entre os colchetes. """

import re

noNewLineRegex = re.compile(r'.*')
nog = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

print(nog)

newLineRegex = re.compile(r'.*', re.DOTALL)
nog1 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

print(nog1)
