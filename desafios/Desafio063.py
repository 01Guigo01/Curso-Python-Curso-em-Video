"""

Desafio063

Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de Fibonacci.

"""

import time
import emoji

print("=" * 50)
print("✨ SEQUÊNCIA DE FIBONACCI ✨".center(50))
print("Descubra os N primeiros elementos da magia matemática!".center(50))
print("=" * 50)

number_of_elements = int(input("🔢 Digite quantos elementos da sequência você quer ver: "))

print(f"\nCalculando os \033[1;36m{number_of_elements}\033[m primeiros termos...")
time.sleep(1.5)

print("\n" + "=" * 50)
print("📝 SEQUÊNCIA DE FIBONACCI 📝".center(50))
print("=" * 50)

if number_of_elements <= 0:
    print("❌ Por favor, digite um número inteiro positivo para a sequência.")
elif number_of_elements == 1:
    print(f"👉 \033[1;32m0\033[m -> FIM")
elif number_of_elements == 2:
    print(f"👉 \033[1;32m0\033[m -> \033[1;32m1\033[m -> FIM")
else:
    term1 = 0
    term2 = 1
    count = 3

    print(f"👉 \033[1;32m{term1}\033[m -> \033[1;32m{term2}\033[m -> ", end="")

    while count <= number_of_elements:
        next_term = term1 + term2
        print(f"\033[1;32m{next_term}\033[m -> ", end="")
        term1 = term2
        term2 = next_term
        count += 1
        time.sleep(0.3)

    print("FIM")

print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
