"""
DESESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:
1 - Quantas vezes aparece a letra "A"

2 - Em que posição ela aparece a primeira vez

3 - Em que posição ela aparece a ultima vez

"""

print("=" * 50)

phrase = str(input("Digite uma frase: ")).strip()

phrase_upper = phrase.upper()
count_a = phrase_upper.count('A')
first_position_a = phrase_upper.find('A')
last_position_a = phrase_upper.rfind('A')
print(f"A frase digitada foi: '{phrase}'")
print(f"A letra 'A' aparece {count_a} vezes na frase.")

if count_a > 0:
    print(f"A primeira letra 'A' apareceu na posição {first_position_a}.")
    print(f"A última letra 'A' apareceu na posição {last_position_a}.")
else:
    print("A letra 'A' não foi encontrada na frase.")


print("=" * 50)