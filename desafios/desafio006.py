"""

DESAFIO 006

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""

import math
import time
print("=" * 50)
print("✨ ANALISADOR DE PROPRIEDADES NUMÉRICAS ✨".center(50)) # Título mais descritivo e com emoji
print("=" * 50)

number = int(input("🔢 Digite um número inteiro para análise: "))

print(f"\nPreparando para analisar o número: \033[1;36m{number}\033[m...") # Destacando o número em ciano
time.sleep(2) # Uma pequena pausa para simular o processamento

double_value = number * 2
triple_value = number * 3
square_root = math.sqrt(number)

print("\n" + "-" * 50)
print("🔎 RESULTADOS DA ANÁLISE:".center(50))
print("-" * 50)

print(f"➕ O DOBRO de \033[1;36m{number}\033[m é: \033[1;32m{double_value}\033[m") # Dobro em verde

print(f"✖️ O TRIPLO de \033[1;36m{number}\033[m é: \033[1;34m{triple_value}\033[m") # Triplo em azul

print(f"🌱 A RAIZ QUADRADA de \033[1;36m{number}\033[m é: \033[1;33m{square_root:.2f}\033[m") # Raiz em amarelo e formatada

print("-" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
