#!/usr/bin/env python3

myPets = ['Zophie', 'Pooka', 'Fat-tail', 'Merlot', 'Melin']

name = input("Enter a pet name: ")

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
