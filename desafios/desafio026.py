"""

DESESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:

1 - Quantas vezes aparece a letra "A".

2 - Em que posição ela aparece a primeira vez.

3 - Em que posição ela aparece a ultima vez.

"""

import time

print("=" * 50)
print("✨ EXPLORADOR DE FRASES: LETRA 'A' ✨".center(50))
print("Descubra os segredos da letra 'A' na sua frase!".center(50))
print("=" * 50)

phrase = str(input("✍️ Digite uma frase qualquer: ")).strip()

print(f"\nAnalisando a frase: '\033[1;36m{phrase}\033[m'...")
time.sleep(2)

phrase_upper = phrase.upper()
count_a = phrase_upper.count('A')
first_position_a = phrase_upper.find('A')
last_position_a = phrase_upper.rfind('A')

print("\n" + "=" * 50)
print("🔍 RESULTADOS DA ANÁLISE 🔍".center(50))
print("=" * 50)

print(f"A frase digitada foi: '\033[1;34m{phrase}\033[m'")
print(f"A letra '\033[1;33mA\033[m' aparece \033[1;32m{count_a}\033[m vezes na frase.")

if count_a > 0:
    print(f"A primeira letra '\033[1;33mA\033[m' apareceu na posição: \033[1;35m{first_position_a}\033[m.")
    print(f"A última letra '\033[1;33mA\033[m' apareceu na posição: \033[1;35m{last_position_a}\033[m.")
else:
    print("😔 Ops! A letra '\033[1;33mA\033[m' \033[1;31mNÃO\033[m foi encontrada em sua frase.")

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
