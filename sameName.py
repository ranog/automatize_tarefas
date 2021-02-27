#!/usr/bin/env python3

def spam():
    eggs = 'spam local'
    print(eggs) # exibe 'spam local'


def bacon():
    eggs = 'bacon local'
    print(eggs) # exibe 'bacon local'
    spam()
    print(eggs) # exibe 'bacon local'


eggs = 'global'
bacon()
print(eggs) # exibe 'global'
