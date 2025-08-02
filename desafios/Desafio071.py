"""

Desafio071

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possuí cédulas de R$100, R$50, R$20, R$10, R$5 e R$1.

"""

import time
import emoji

# Definindo as cores para cada cédula
blue = "\033[1;34m"
yellow = "\033[1;33m"
magenta = "\033[1;35m"
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
reset_color = "\033[m"

print("=" * 50)
print("✨ CAIXA ELETRÔNICO MÁGICO ✨".center(50))
print("Seu dinheiro de forma prática e rápida!".center(50))
print("=" * 50)

print("\n💰 Bem-vindo ao caixa mágico!")
amount = int(input("Qual o valor a ser sacado? R$"))
print(f"\nProcessando o saque de \033[1;36mR${amount}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("📝 CÉDULAS ENTREGUES 📝".center(50))
print("=" * 50)

remaining_amount = amount

hundreds_count = remaining_amount // 100
remaining_amount %= 100
if hundreds_count > 0:
    print(f"👉 {blue}{hundreds_count}{reset_color} cédulas de R$100")

fifties_count = remaining_amount // 50
remaining_amount %= 50
if fifties_count > 0:
    print(f"👉 {yellow}{fifties_count}{reset_color} cédulas de R$50")

twenties_count = remaining_amount // 20
remaining_amount %= 20
if twenties_count > 0:
    print(f"👉 {magenta}{twenties_count}{reset_color} cédulas de R$20")

tens_count = remaining_amount // 10
remaining_amount %= 10
if tens_count > 0:
    print(f"👉 {red}{tens_count}{reset_color} cédulas de R$10")

fives_count = remaining_amount // 5
remaining_amount %= 5
if fives_count > 0:
    print(f"👉 {green}{fives_count}{reset_color} cédulas de R$5")

ones_count = remaining_amount // 1
if ones_count > 0:
    print(f"👉 {white}{ones_count}{reset_color} cédulas de R$1")

print("\n" + "=" * 50)
print("SAQUE CONCLUÍDO! 👋".center(50))
print("=" * 50)
