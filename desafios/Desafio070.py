"""

Desafio070

Crie um programa que leia o nome e [reço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No
final, mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de R$1000.00

C) Qual é o nome do produto mais barato

"""

import time
import emoji

print("=" * 50)
print("✨ ANÁLISE DE PRODUTOS DO MERCADO ✨".center(50))
print("Cadastre seus produtos e veja as estatísticas!".center(50))
print("=" * 50)

total_spent = 0
more_than_1000_count = 0
product_count = 0
lowest_price = 0
cheapest_product_name = ''
keep_going = 'S'

while keep_going == 'S':
    print("\n--- CADASTRO DO PRODUTO ---")
    product_name = str(input("📝 Digite o nome do produto: ")).strip().upper()
    product_price = float(input("💰 Digite o preço do produto: R$"))

    total_spent += product_price
    product_count += 1

    if product_price > 1000:
        more_than_1000_count += 1

    if product_count == 1 or product_price < lowest_price:
        lowest_price = product_price
        cheapest_product_name = product_name

    keep_going_valid = False
    while not keep_going_valid:
        print("\n" + "=" * 50)
        keep_going = str(input("Quer continuar a cadastrar? [S/N]: ")).strip().upper()[0]
        print("=" * 50)
        if keep_going in 'SN':
            keep_going_valid = True
        else:
            print("❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            time.sleep(1)

print("\n" + "=" * 50)
print("📊 RESULTADO FINAL DA ANÁLISE 📊".center(50))
print("=" * 50)

print(f"💰 O total gasto na compra foi de: \033[1;32mR${total_spent:.2f}\033[m")
print(f"📈 Produtos que custam mais de R$1000,00: \033[1;33m{more_than_1000_count}\033[m")
print(
    f"📦 O produto mais barato foi \033[1;36m{cheapest_product_name.title()}\033[m, custando \033[1;36mR${lowest_price:.2f}\033[m.")
print(emoji.emojize(":partying_face: :money_bag:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)







