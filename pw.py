#!/usr/bin/env python3

""" pw.py - Um programa para repositório de senhas que não é seguro. """

import sys

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
        'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
        'luggage': '12345'}

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]   # O primeiro argumento da linha de comando é o
                        # nome da conta.


