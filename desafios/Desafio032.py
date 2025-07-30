"""

DESESAFIO 032

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

"""

import time
import emoji

print("=" * 50)
print("✨ ANALISADOR DE ANOS BISSEXTO ✨".center(50))
print("Descubra se o ano é especial!".center(50))
print("=" * 50)

# Obtém o ano atual do sistema para uma sugestão, mas não o usa na lógica principal
current_year = time.localtime().tm_year

year = int(input(f"🗓️ Digite um ano para saber se ele é bissexto (ex: {current_year}): "))

print(f"\nVerificando se o ano \033[1;36m{year}\033[m é um ano bissexto...")
time.sleep(2)

print("\n" + "=" * 50)
print("🔍 RESULTADO DA VERIFICAÇÃO 🔍".center(50))
print("=" * 50)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"🎉 O ano \033[1;32m{year}\033[m \033[1;32mÉ BISSEXTO\033[m! Ele tem 366 dias! ✨")
    print(emoji.emojize(":calendar: :sparkles:"))
else:
    print(f"😔 O ano \033[1;31m{year}\033[m \033[1;31mNÃO É BISSEXTO\033[m. Ele tem 365 dias. 🙁")
    print(emoji.emojize(":calendar:"))

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
