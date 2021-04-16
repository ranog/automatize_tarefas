#!/usr/bin/env python3


def spam():
    print(eggs) # ERRO!
    eggs = 'spam local'


eggs = 'global'
spam()
