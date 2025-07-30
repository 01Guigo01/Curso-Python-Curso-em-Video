"""

DESESAFIO 024

Crie um programa que leia o nome de uma cidade e diga se ela começa ou nãO COM O NOME "SANTO".

"""

import time

print("=" * 50)
print("✨ CIDADE COM SANTO? VAMOS DESCOBRIR! ✨".center(50))
print("=" * 50)

name_ciy = str(input("🏙️ Digite o nome da sua cidade: ")).strip().upper()

print(f"\nAnalisando se '{name_ciy.title()}' começa com 'Santo'...")
time.sleep(2)

find_santo = name_ciy.startswith("SANTO")

print("\n" + "=" * 50)
print("🔍 RESULTADO DA VERIFICAÇÃO 🔍".center(50))
print("=" * 50)

if find_santo:
    print(f"🎉 A cidade '\033[1;32m{name_ciy.title()}\033[m' \033[1;32mCOMEÇA\033[m com 'Santo'!")
else:
    print(f"😔 A cidade '\033[1;31m{name_ciy.title()}\033[m' \033[1;31mNÃO COMEÇA\033[m com 'Santo'.")

print("=" * 50)
print("VERIFICAÇÃO CONCLUÍDA!".center(50))
print("=" * 50)
