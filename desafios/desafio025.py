"""

DESESAFIO 025

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""

import time

print("=" * 50)
print("✨ VERIFICADOR DE NOME: SILVA NA LISTA? ✨".center(50))
print("=" * 50)

name_ciy = str(input("✍️ Digite seu nome completo: ")).strip().upper()

print(f"\nAnalisando o nome: '\033[1;36m{name_ciy.title()}\033[m' para ver se tem 'Silva'...")
time.sleep(2)

find_silva = name_ciy.find("SILVA")

print("\n" + "=" * 50)
print("🔍 RESULTADO DA VERIFICAÇÃO 🔍".center(50))
print("=" * 50)

if find_silva == -1:
    print(f"😔 Que pena! O seu nome '\033[1;31m{name_ciy.title()}\033[m' \033[1;31mNÃO\033[m possui 'Silva'.")
else:
    print(f"🎉 Parabéns! O seu nome '\033[1;32m{name_ciy.title()}\033[m' \033[1;32mPOSSUI\033[m 'Silva'!")

print("=" * 50)
print("VERIFICAÇÃO CONCLUÍDA!".center(50))
print("=" * 50)
