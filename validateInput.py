#!/usr/bin/env python3

""" No primeiro loop while, perguntamos a idade ao usuário e armazenamos
sua entrada em age. Se age for um valor válido (decimal), sairemos desse
primeiro loop while e prosseguiremos para o segundo, que pede uma senha.
Caso contrário, informamos o usuário que ele deve fornecer um número e
perguntamos sua idade novamente.

No segundo loop while, devemos pedir uma senha, armazenar o dado de
entrada do usuário em password e sair do loop se a entrada for
alfanumérica. Se não for, não ficaremos satisfeitos; sendo assim,
dizemos ao usuário que a senha deve ser alfanumérica e, novamente,
pedimos que uma senha seja fornecida.

Se chamarmos isdecimal() e isalnum() em variáveis, poderemos testar se
os valores armazenados nessas variáveis são decimais ou não, ou se são
alfanuméricos ou não.

Eis alguns métodos de string is X comuns:

- isalpha() retornará True se a string for constituída somente de letras
e não estiver vazia.
- isalnum() retornará True se a string for constituída somente de letras
e números e não estiver vazia.
- isdecimal() retornará True se a string for constituída somente de
caracteres numéricos e não estiver vazia.
- isspace() retornará True se a string for constituída somente de
espaços, tabulações e quebras de linha e não estiver vazia.
- istitle() retornará True se a string for constituída somente de
palavras que comecem com uma letra maiúscula seguida somente de letras
minúsculas. """

while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for you age.")

while True:
    print("Select a new password (letters and numbers only): ")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")
