"""
DESAFIO 016

Crie um programa que leia um número Real qualquer pelo teclado e mostre na  tela a sua porção inteira

"""

from math import trunc

print("=" * 50)

num = float(input("Digite um número: "))

print(f"O número digitado foi {num}"
      f"\nSua porção inteira é {trunc(num)}")

print("=" * 50)
