#!/usr/bin/env python3


def spam():
    global eggs
    eggs = 'spam' # essa é a variável global.


def bacon():
    eggs = 'bacon' # essa é uma variável local.


def ham():
    print(eggs) # essa é a variável global.


eggs = 42 # esse é a variável global.
spam()
print(eggs)
