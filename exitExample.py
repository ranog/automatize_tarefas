#!/usr/bin/env python3

import sys

while True:
    print("Type exit to exit.")
    reponse = input()

    if reponse == 'exit':
        sys.exit()

    print("You typed " + reponse + "." )
