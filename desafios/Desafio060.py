"""

Desafio060

Faça um programa que leia um número qualquer e mostre seu fatorial.

"""

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA MÁGICA DE FATORIAL ✨".center(50))
print("Descubra o valor total da multiplicação!".center(50))
print("=" * 50)

number = int(input("🔢 Digite um número para calcular o fatorial: "))
print(f"\nCalculando o fatorial de \033[1;36m{number}\033[m...")
time.sleep(1.5)

factorial_result = 1
calculation_string = ""

if number < 0:
    print("\n❌ Não é possível calcular o fatorial de um número negativo.")
elif number == 0:
    print(f"\n✅ O fatorial de 0 é: \033[1;32m1\033[m")
else:
    for c in range(number, 0, -1):
        factorial_result *= c
        if c == number:
            calculation_string += f"{c}"
        else:
            calculation_string += f" x {c}"

    print("-" * 50)
    print(f"O cálculo é: \033[1;34m{calculation_string}\033[m")
    print("-" * 50)
    print(f"🎉 O fatorial de \033[1;36m{number}\033[m é: \033[1;32m{factorial_result}\033[m!")

print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
