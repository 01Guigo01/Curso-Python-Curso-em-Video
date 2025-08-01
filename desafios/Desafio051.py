"""

Desafio 051

Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa
progressão

"""

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA DE PROGRESSÃO ARITMÉTICA ✨".center(50))
print("Descubra os 10 primeiros termos da sua PA!".center(50))
print("=" * 50)

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA DE PROGRESSÃO ARITMÉTICA ✨".center(50))
print("Descubra os 10 primeiros termos da sua PA!".center(50))
print("=" * 50)

first_term = int(input("🔢 Digite o PRIMEIRO termo da PA: "))
reason = int(input("➕ Digite a RAZÃO da PA: "))

print(f"\nCalculando os 10 primeiros termos da PA com primeiro termo \033[1;36m{first_term}\033[m e razão \033[1;36m{reason}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("📝 OS 10 PRIMEIROS TERMOS DA PA SÃO: 📝".center(50))
print("=" * 50)

for c in range(1, 11):
    term = first_term + (c - 1) * reason
    print(f"👉 \033[1;32m{term}\033[m")
    time.sleep(0.3)

print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
