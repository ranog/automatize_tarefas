#!/usr/bin/env python3

"""
    13. Crie um pequeno programa que mostre os números de 1 a 10 usando
    um loop for. Em seguida, crie um programa equivalente que mostre os 
    números de 1 a 10 usando um loop while.
"""

print("- loop for:")
for num in range(1,11):
    print(num)

print("\n- loop while:")

number = 1
while number <= 10:
    print (number)
    number += 1
