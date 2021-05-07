#!/usr/bin/env python3

""" bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início
de cada linha de texto do clipboard. """

import pyperclip

text = pyperclip.paste()

# TODO: Separa as linhas e acrescenta asteriscos.

pyperclip.copy(text)
