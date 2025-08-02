"""

Desafio 048

Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.

"""

import time
import emoji

print("=" * 50)
print("✨ EXPLORADOR DE NÚMEROS ÍMPARES ✨".center(50))
print("Somando os múltiplos de 3 no intervalo de 1 a 500!".center(50))
print("=" * 50)

soma_total = 0
contador = 0

something = input("✍️ Digite algo ou aperte ENTER para iniciar a análise: ")

print("\n🤯 Analisando e somando os números... Isso pode levar um instante...")
time.sleep(2)

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma_total += c
        contador += 1

print("\n" + "=" * 50)
print("💰 RESULTADO DA SOMA 💰".center(50))
print("=" * 50)

print(f"✅ A quantidade de números encontrados foi de: \033[1;32m{contador}\033[m")
print(f"🎉 A soma total dos números ímpares e múltiplos de 3 entre 1 e 500 é: \033[1;32m{soma_total}\033[m!")
print(emoji.emojize(":money_with_wings: :sparkles:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
