"""

DESAFIO 018

Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""

from math import sin, cos, tan, radians
import time

print("=" * 50)
print("✨ CALCULADORA DE ÂNGULOS TRIGONOMÉTRICOS ✨".center(50))
print("=" * 50)

angle_degrees = float(input("📏 Digite um ângulo qualquer em GRAUS: "))

print(f"\nCalculando seno, cosseno e tangente para \033[1;36m{angle_degrees}°\033[m...")
time.sleep(2)

angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cosine_value = cos(angle_radians)
tangent_value = tan(angle_radians)

print("\n" + "=" * 50)
print("📐 RESULTADOS TRIGONOMÉTRICOS 📐".center(50))
print("=" * 50)

print(f"Para o ângulo de \033[1;34m{angle_degrees}°\033[m:")
print(f"👉 O SENO é: \033[1;32m{sine_value:.2f}\033[m")
print(f"👉 O COSSENO é: \033[1;33m{cosine_value:.2f}\033[m")
print(f"👉 A TANGENTE é: \033[1;31m{tangent_value:.2f}\033[m")

print("=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
