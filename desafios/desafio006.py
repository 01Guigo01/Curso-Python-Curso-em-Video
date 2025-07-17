"""
DESAFIO 006

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""
import math  # Importa o módulo de matemática para usar a função sqrt()

number = int(input("Digite um número: "))

print("=" * 50)
print(f"Analisando o número {number}".center(50))
print("-" * 50)

double_value = number * 2
triple_value = number * 3
square_root = number ** 0.5

print(f"O dobro de {number} vale {double_value}.")
print(f"O triplo de {number} vale {triple_value}.")
print(f"A raiz quadrada de {number} é igual a {square_root:.2f}.")

print("=" * 50)