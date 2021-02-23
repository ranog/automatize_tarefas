#!/usr/bin/env python3

"""
    9. Escreva um código que exiba Hello se 1 estiver armazenado em
    spam, Howdy se 2 estiver armazenado em spam e Greetings! se outro
    valor estiver armazenado em spam (pg 92).
"""

spam = input("Please enter a number: ")
spam = int(spam)

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")
