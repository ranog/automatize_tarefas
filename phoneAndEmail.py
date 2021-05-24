#! python3
# phoneAndEmail.py – Encontra números de telefone e endereços de email
# no clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # código de área
        (\s|-|\.)?          # separador
        (\d{3})             # primeiros 3 dígitos
        (\s|-|\.)?          # separador
        (\d{4})             # últimos 4 dígitos
        (\s*(exp|x|exp.)\s*(\d{2,5}))?  # extensão
        )'''.re.VERBOSE)

# Cria a regex para email.
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # nome do usuário
        @                   # símbolo @
        [a-zA-Z0-9.-]+      # nome do domínio
        (\.[a-zA-Z]{2,4})   # ponto seguido de outros caracteres
        )''', re.VERBOSE)

# TODO: Encontra correspondências no texto do clipboard.
# TODO: Copia os resultados para o clipboard.
