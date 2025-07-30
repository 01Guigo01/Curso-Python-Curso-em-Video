"""

DESESAFIO 023

Faça um programa que  leia um núemro de 0 a 9999 e mostre na tela cada um dos dígito separados.

Ex:
Digite um númeoro: 1834

unidade:
dezena:3
centena: 8
milhar: 1

"""

import time

print("=" * 50)
print("✨ EXPLORADOR DE ORDENS NUMÉRICAS ✨".center(50))
print("Descubra a estrutura dos seus números!".center(50))
print("=" * 50)

num_raw = input("🔢 Digite um número inteiro (de 0 a 9999): ").strip()

if not num_raw.isdigit() or int(num_raw) < 0 or int(num_raw) > 9999:
    print("\n❌ Entrada inválida! Por favor, digite um número inteiro entre 0 e 9999.")
    print("=" * 50)
    exit()

num_str = num_raw.zfill(4)

print(f"\nAnalisando o número \033[1;36m{num_raw}\033[m (representado como \033[1;36m{num_str}\033[m)...")
time.sleep(2)

print("\n" + "=" * 50)
print("🔍 COMPOSIÇÃO DO NÚMERO 🔍".center(50))
print("=" * 50)

print(f"👉 Unidade:   \033[1;32m{num_str[3]}\033[m")
print(f"👉 Dezena:    \033[1;33m{num_str[2]}\033[m")
print(f"👉 Centena:   \033[1;34m{num_str[1]}\033[m")
print(f"👉 Milhar:    \033[1;31m{num_str[0]}\033[m")

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
