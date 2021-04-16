#!/usr/bin/env python3

def spam():
    global eggs # declarada como variável global.
    eggs = 'spam'


eggs = 'global'
spam()

print(eggs)
