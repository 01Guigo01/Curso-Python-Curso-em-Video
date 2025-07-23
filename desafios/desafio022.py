"""
DESESAFIO 022

Crie um programa quqe leia o nome completo de uma pessoa e mostre:

1 - O nome com todas as letras maíúsculos

2 - O nome com todas as letras minúsculas

3 - Quantas letras ao todo (sem considerar espaços)

4 - Quantas letras tem o primeiro nome

"""
from os.path import split

print("=" * 50)

print("VERIFICADOR DE NOME".center(50))

name = str(input("Digite seu nome completo: ")).strip()

name_upper = name.upper()
name_lower = name.lower()
amount_name_not_space = len(name.replace(" ", ""))
amount_first_name = len(name.split()[0])

print(f"Seu nome completo em letras maiúscula fica: {name_upper}"
      f"\nSeu nome completo em letras minúsculas fica: {name_lower}"
      f"\nSeu nome completo tem ao todo {amount_name_not_space} caracteres"
      f"\nSeu primeiro nome tem {amount_first_name} caracteres")

print("=" * 50)