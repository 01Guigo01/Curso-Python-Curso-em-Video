"""

DESAFIO 016

Crie um programa que leia um número Real qualquer pelo teclado e mostre na  tela a sua porção inteira.

"""

from math import trunc
import time

print("=" * 50)
print("✨ EXTRACTOR DE PORÇÃO INTEIRA ✨".center(50))
print("=" * 50)

num = float(input("🔢 Digite um número real (com vírgula, ex: 6.789): "))

print(f"\nAnalisando o número: \033[1;36m{num}\033[m...")
time.sleep(2)

integer_part = trunc(num)

print("\n" + "=" * 50)
print("🔎 RESULTADO DA ANÁLISE 🔎".center(50))
print("=" * 50)

print(f"O número completo digitado foi: \033[1;34m{num}\033[m")
print(f"Sua porção INTEIRA é: \033[1;32m{integer_part}\033[m! 🎉")

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
