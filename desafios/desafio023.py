"""
DESESAFIO 023

Faça um programa que  leia um núemro de 0 a 9999 e mostre na tela cada um dos dígito separados

Ex:
Digite um númeoro: 1834

unidade:
dezena:3
centena: 8
milhar: 1

"""

print("=" * 50)

print("VERIFICADOR DE NÚMEROS".center(50))

num_str = str(input("Digite um número (de 0 a 9999): ")).zfill(4)

print(f"\nunidade: {num_str[3]}")
print(f"\ndezena: {num_str[2]}")
print(f"\ncentena: {num_str[1]}")
print(f"\nmilhar: {num_str[0]}")


print("=" * 50)