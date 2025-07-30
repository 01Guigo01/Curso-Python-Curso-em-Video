"""

DESAFIO 017

Faça um programa que leia o comprimentyo do cateto oposto e do cateto adjacente de um triângulo retâncgulo, calcule e
mostre o comprimento da hipotenusa.

"""

from math import hypot
import time

print("=" * 50)
print("✨ CALCULADORA DE HIPOTENUSA PITAGÓRICA ✨".center(50))
print("=" * 50)

cateto_oposto = float(input("📐 Digite o comprimento do CATETO OPOSTO: "))
cateto_adjacente = float(input("📏 Digite o comprimento do CATETO ADJACENTE: "))

print(f"\nCalculando a hipotenusa para catetos de \033[1;36m{cateto_oposto:.2f}\033[m e \033[1;36m{cateto_adjacente:.2f}\033[m...")
time.sleep(2)

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("\n" + "=" * 50)
print("🔺 RESULTADO DO CÁLCULO 🔺".center(50))
print("=" * 50)

print(f"O cateto oposto é: \033[1;34m{cateto_oposto:.2f}\033[m")
print(f"O cateto adjacente é: \033[1;34m{cateto_adjacente:.2f}\033[m")
print("-" * 50)

print(f"A HIPOTENUSA calculada é: \033[1;32m{hipotenusa:.2f}\033[m! 🎉")

print("=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
