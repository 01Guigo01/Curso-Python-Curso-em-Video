"""
DESAFIO 005

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

"""


# Get a number from the user
num = int(input("Digite um número: "))

# Display the analysis of the number
print("=" * 50)
print(f"Analisando o número {num}...".center(50))
print("-" * 50)
print(f"Seu antecessor é o número {num - 1}.")
print(f"Seu sucessor é o número {num + 1}.")
print("=" * 50)