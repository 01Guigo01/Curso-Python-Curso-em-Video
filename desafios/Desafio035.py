"""

DESESAFIO 035

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

"""

import time
import emoji

print("=" * 50)
print("✨ TRIÂNGULO MÁGICO: É POSSÍVEL FORMAR? ✨".center(50))
print("Descubra a geometria das suas retas!".center(50))
print("=" * 50)

r1 = float(input('📏 Digite o comprimento da PRIMEIRA reta: '))
r2 = float(input('📏 Digite o comprimento da SEGUNDA reta: '))
r3 = float(input('📏 Digite o comprimento da TERCEIRA reta: '))

print(f"\nAnalisando se \033[1;36m{r1:.2f}\033[m, \033[1;36m{r2:.2f}\033[m e \033[1;36m{r3:.2f}\033[m podem formar um triângulo...")
time.sleep(2)

print("\n" + "=" * 50)
print("📐 RESULTADO DA ANÁLISE 📐".center(50))
print("=" * 50)

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(f"🎉 Com os comprimentos \033[1;32m{r1:.2f}\033[m, \033[1;32m{r2:.2f}\033[m e \033[1;32m{r3:.2f}\033[m,")
    print("\033[1;32mÉ POSSÍVEL\033[m formar um triângulo! Perfeito! ✨")
    print(emoji.emojize(":triangle_pointing_up: :sparkles:"))
else:
    print(f"😔 Com os comprimentos \033[1;31m{r1:.2f}\033[m, \033[1;31m{r2:.2f}\033[m e \033[1;31m{r3:.2f}\033[m,")
    print("\033[1;31mNÃO É POSSÍVEL\033[m formar um triângulo. As retas não se fecham. 🙁")
    print(emoji.emojize(":red_triangle_pointed_down: :heavy_multiplication_x:"))

print("=" * 50)
print("ANÁLISE GEOMÉTRICA CONCLUÍDA!".center(50))
print("=" * 50)
