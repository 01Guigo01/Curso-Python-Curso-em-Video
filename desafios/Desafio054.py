"""

Desafio 054

Crie um programa que leia o anao de nascimento de sete pessoas. No final, mostre quantas pessoas não atingiram a
maioridade e quantas já são maiores

"""

import time
import emoji

print("=" * 50)
print("✨ VERIFICADOR DE MAIORIDADE ✨".center(50))
print("Descubra quem já pode curtir e quem ainda está crescendo!".center(50))
print("=" * 50)

import time
import emoji

print("=" * 50)
print("✨ VERIFICADOR DE MAIORIDADE ✨".center(50))
print("Descubra quem já pode curtir e quem ainda está crescendo!".center(50))
print("=" * 50)

adults = 0
minors = 0
current_year = 2025 # Mantive o ano atual fixo para simplificar o código, como você prefere

print(f"\nEstamos analisando a maioridade com base no ano de \033[1;36m{current_year}\033[m.")
time.sleep(1.5)

for c in range(1, 8):
    birth_year = int(input(f"🔢 Digite o ano de nascimento da {c}ª pessoa: "))
    age = current_year - birth_year

    if age >= 18:
        adults += 1
    else:
        minors += 1

print("\n" + "=" * 50)
print("🔍 RESULTADO DA ANÁLISE 🔍".center(50))
print("=" * 50)

print(f"🎉 No grupo, temos \033[1;32m{adults}\033[m pessoas que já são MAIORES de idade! ✨")
print(f"😔 E temos \033[1;31m{minors}\033[m pessoas que ainda são MENORES de idade. 🙁")

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)