"""

Desafio 052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

import time
import emoji

print("=" * 50)
print("✨ VERIFICADOR DE NÚMEROS PRIMOS ✨".center(50))
print("Descubra a magia por trás dos números!".center(50))
print("=" * 50)

number = int(input("🔢 Digite um número inteiro para a verificação: "))

print(f"\nAnalisando o número \033[1;36m{number}\033[m para ver se ele é primo...")
time.sleep(2)

divisors = 0
for c in range(1, number + 1):
    if number % c == 0:
        divisors += 1

print("\n" + "=" * 50)
print("🔍 RESULTADO DA ANÁLISE 🔍".center(50))
print("=" * 50)

if divisors == 2:
    print(f"🎉 O número \033[1;32m{number}\033[m é um NÚMERO PRIMO! Ele só é divisível por 1 e por ele mesmo. ✨")
    print(emoji.emojize(":partying_face: :star-struck:"))
else:
    print(f"😔 O número \033[1;31m{number}\033[m \033[1;31mNÃO\033[m é um número primo. Ele tem {divisors} divisores. 🙁")
    print(emoji.emojize(":unamused_face:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
