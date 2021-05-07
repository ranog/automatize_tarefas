#!/usr/bin/env python3

""" bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início
de cada linha de texto do clipboard. """

import pyperclip

text = pyperclip.paste()

# Separa as linhas e acrescenta asteriscos.
lines = text.split('\n')

# Percorre todos os índices da lista "lines" em um loop.
for i in range(len(lines)):
    # Acrescenta um asterisco em cada string da lista "lines".
    lines[i] = '* ' + lines[i]

# Passamos "lines" para o método join() a fim de obter uma única string
# resultante da junção das strings da lista. 
text = '\n'.join(lines)

pyperclip.copy(text)
