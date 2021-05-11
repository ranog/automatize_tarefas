#!/usr/bin/env python3

""" Método findall()
Além do método search(), os objetos Regex também têm um método
findall(). Enquanto search() retorna um objeto Match do primeiro texto
correspondente na string pesquisada, o método findall() retorna as
strings de todas as correspondências na string pesquisada.

Para resumir o que o método findall() retorna, lembre-se do seguinte:

1. Quando chamado em uma regex sem grupos, por exemplo, \d\d\d-\d\d\d-
\d\d\d\d, o método findall() retorna uma lista de strings
correspondentes, como ['415-555-9999', '212-555-0000'].

2. Quando chamado em uma regex que tenha grupos, por exemplo, (\d\d\d)-
(\d\d\d)-(\d\d\d\d), o método findall() retorna uma lista de tuplas
contendo strings (uma string para cada grupo), como em
[('415', '555', '1122'), ('212', '555', '0000')]. """

import re

print("""- String para pesquisa:
Cell: 415-555-9999 Work: 212-555-0000

Método search(): """)

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print("OBS: Retorna somente o objeto Match.")

print("\nMétodo findall() (SEM grupos na regex): ")
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
print("OBS: findall() retorna uma lista de strings.")

print("\nMétodo findall() (COM grupos na regex): ")
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
print("OBS: findall() retorna uma lista de tuplas.")
