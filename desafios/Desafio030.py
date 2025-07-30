"""

DESESAFIO 030

Crie um programa que leia um número inteiro e mostre na se ele é par ou é ímpar.

"""

import time

print("=" * 50)
print("✨ PAR OU ÍMPAR: QUAL É O NÚMERO? ✨".center(50))
print("Descubra a natureza do seu número!".center(50))
print("=" * 50)

num = int(input("🔢 Digite um número inteiro qualquer: "))

print(f"\nAnalisando o número: \033[1;36m{num}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("🔍 RESULTADO DA VERIFICAÇÃO 🔍".center(50))
print("=" * 50)

if num % 2 == 0:
    print(f"🎉 O número \033[1;32m{num}\033[m que você digitou é \033[1;32mPAR\033[m! ✨")
else:
    print(f"🤔 O número \033[1;31m{num}\033[m que você digitou é \033[1;31mÍMPAR\033[m. 🧐")

print("=" * 50)
print("VERIFICAÇÃO CONCLUÍDA!".center(50))
print("=" * 50)
