#!/usr/bin/env python3

# Este é um jogo de adivinhar o número.
import random

# Gera um número aleatório entre 1 e 20.
secretNumber = random.randint(1, 20) 
print("I am thinking of a number between 1 and 20.")

# Peça para o jagodor adivinhar 6 vezes.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    # Verificam se o palpite é menor ou maior que o número secreto.
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too hight.")
    else:
        break # Esta condição corresponde ao palpite correto!

# Verifica se o jogador adivinhou corretamente o número e exibe uma
# mensagem apropriada na tela.
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) +
            " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
