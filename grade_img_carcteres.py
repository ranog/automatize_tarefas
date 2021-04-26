#!/usr/bin/env python3

""" Podemos pensar em grid[x][y] como sendo o caractere nas coordenadas
x e y de uma “imagem” desenhada com caracteres textuais. A origem (0, 0)
estará no canto superior esquerdo, as coordenadas x aumentam para a
direita e as coordenadas y aumentam para baixo. """

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0

while x < len(grid[0]):
    for y in grid:
        print(y[x], end='')
    x += 1
    print()
