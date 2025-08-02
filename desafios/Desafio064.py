"""

Desafio064

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)

"""

import time
import emoji

print("=" * 50)
print("✨ SOMADOR E CONTADOR MÁGICO ✨".center(50))
print("Descubra a soma e a quantidade de números que você digitar!".center(50))
print("=" * 50)

print("\n🔢 Digite números inteiros. Para encerrar, digite \033[1;31m999\033[m.")
time.sleep(1.5)

total_sum = 0
count = 0
number = int(input("➡️ Digite um número: "))

while number != 999:
    total_sum += number
    count += 1
    number = int(input("➡️ Digite um número: "))

print("\n" + "=" * 50)
print("🎉 ANÁLISE FINALIZADA! 🎉".center(50))
print("=" * 50)

print(f"Você digitou um total de \033[1;33m{count}\033[m números (excluindo o 999).")
print(f"A soma de todos esses números é: \033[1;32m{total_sum}\033[m.")
print(emoji.emojize(":partying_face: :money_bag:"))

print("\n" + "=" * 50)
print("OBRIGADO POR USAR NOSSA FERRAMENTA!".center(50))
print("=" * 50)
print(emoji.emojize(":partying_face: :money_bag:"))
print("=" * 50)