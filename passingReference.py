#!/usr/bin/env python3

def eggs(someParameter):
    """ Modifica a lista in place. """
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)

print(spam)
