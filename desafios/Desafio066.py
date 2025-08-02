"""

Desafio066

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

(Desconsiderando o flag).

"""

import time
import emoji

print("=" * 50)
print("✨ SOMADOR E CONTADOR MÁGICO ✨".center(50))
print("Descubra a soma e a quantidade dos seus números!".center(50))
print("=" * 50)

total_sum = 0
count = 0
keep_going = 'S'

while keep_going == 'S':
    number = int(input("🔢 Digite um número: "))

    total_sum += number
    count += 1

    keep_going_valid = False
    while not keep_going_valid:
        print("\n" + "=" * 50)
        keep_going = str(input("Quer digitar outro número? [S/N]: ")).strip().upper()[0]
        print("=" * 50)

        if keep_going in "SN":
            keep_going_valid = True
        else:
            print("\n❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            time.sleep(1)

print("\n" + "=" * 50)
print("🎉 ANÁLISE FINALIZADA! 🎉".center(50))
print("=" * 50)

print(f"Você digitou um total de \033[1;33m{count}\033[m números.")
print(f"A soma de todos esses números é: \033[1;32m{total_sum}\033[m.")
print(emoji.emojize(":partying_face: :money_bag:"))
