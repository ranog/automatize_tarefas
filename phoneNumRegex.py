#!/usr/bin/env python3

""" Revisão da correspondência com expressão regular

Embora haja diversos passos para usar expressões regulares em Python,
cada passo é bem simples:
    1. Importe o módulo de regex usando import re;
    2. Crie um objeto Regex usando a função re.compile(). (Lembre-se de
    usar uma string pura);
    3. Passe a string que você quer pesquisar ao método search() do
    objeto Regex. Isso fará um objeto Match ser retornado;
    4. Chame o método group() do objeto Match para retornar uma string
    com o texto correspondente.

NOTA: Apesar de incentivá-lo a digitar o código de exemplo no shell
interativo, você também deve usar ferramentas de teste de expressões
regulares baseadas em web, que poderão mostrar exatamente como uma regex
faz a correspondência de uma porção de texto especificada. Recomendo
usar a ferramenta de teste em http://regexpal.com/ . """

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print("Phone number found: " + mo.group())
