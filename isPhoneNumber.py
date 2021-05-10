#!/usr/bin/env python3

# isPhoneNumber.py - Encontrando padrões de texto sem usar expressões
# regulares (pg 189-190).

def isPhoneNumber(text):
    """ Verifica se uma string corresponde ao padrão telefônico
    415-555-4242. """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print("415-555-4242 is a phone number: ")
print(isPhoneNumber('415-555-4242'))
print("Moshi moshi is a phone number: ")
print(isPhoneNumber('Moshi moshi'))
