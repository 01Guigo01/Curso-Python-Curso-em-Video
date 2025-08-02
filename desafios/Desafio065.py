"""

Desafio065

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.

"""

import time
import emoji

print("=" * 50)
print("✨ ANALISADOR DE NÚMEROS ✨".center(50))
print("Descubra a média, o maior e o menor valor de uma sequência!".center(50))
print("=" * 50)

total_sum = 0
count = 0
highest_number = 0
lowest_number = 0
keep_going = 'S'

print("\n🤯 Vamos começar a analisar seus números!")
time.sleep(1.5)

while keep_going == 'S':
    number = int(input("🔢 Digite um número inteiro: "))
    total_sum += number
    count += 1

    if count == 1:
        highest_number = number
        lowest_number = number
    else:
        if number > highest_number:
            highest_number = number
        if number < lowest_number:
            lowest_number = number

    print("\n" + "=" * 50)
    keep_going = str(input("Quer continuar a digitar? [S/N]: ")).strip().upper()[0]
    print("=" * 50)

print("\n🎉 ANÁLISE CONCLUÍDA! 🎉".center(50))
print("-" * 50)

if count > 0:
    average = total_sum / count
    print(f"Você digitou \033[1;33m{count}\033[m números.")
    print(f"A média entre eles é: \033[1;36m{average:.2f}\033[m.")
    print(f"O maior valor digitado foi: \033[1;32m{highest_number}\033[m.")
    print(f"O menor valor digitado foi: \033[1;31m{lowest_number}\033[m.")
else:
    print("❌ Nenhum número foi digitado. Nenhuma análise a ser feita.")

print("-" * 50)
print("OBRIGADO POR USAR NOSSA FERRAMENTA!".center(50))
print("=" * 50)
print(emoji.emojize(":partying_face: :money_bag:"))
print("=" * 50)