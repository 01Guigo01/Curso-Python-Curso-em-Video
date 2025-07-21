"""
DESAFIO 017

Faça um programa que leia o comprimentyo do cateto oposto e do cateto adjacente de um triângulo retâncgulo, calcule e
mostre o comprimento da hipotenusa

"""

from math import hypot

print("=" * 50)

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Exibir o resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

print("=" * 50)
