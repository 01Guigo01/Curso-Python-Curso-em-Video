"""

DESAFIO 012

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto.

"""

import time

print("=" * 50)
print("✨ LOJAS LOUCAS ✨".center(50))
print("🎁 Seu Cupom de Desconto 🎁".center(50))
print("=" * 50)

product_value = float(input("💲 Digite o valor do produto: R$"))
discount_percentage = int(input("✂️ Digite a porcentagem de desconto (ex: 10 para 10%): "))

print(f"\nAplicando desconto de \033[1;36m{discount_percentage}%\033[m ao valor de \033[1;36mR${product_value:.2f}\033[m...")
time.sleep(2)

# Realiza os cálculos
discount_amount = product_value * (discount_percentage / 100)
final_price = product_value - discount_amount

print("\n" + "=" * 50)
print("🎉 RESUMO DA SUA COMPRA 🎉".center(50))
print("=" * 50)

# Apresenta os resultados com cores e destaque
print(f"Preço original do produto: \033[1;34mR${product_value:,.2f}\033[m")
print(f"Desconto aplicado: \033[1;33m{discount_percentage}%\033[m")
print("-" * 50) # Linha divisória

print(f"Você economizou: \033[1;32mR${discount_amount:,.2f}\033[m! ✨")
print(f"VALOR FINAL A PAGAR: \033[1;32mR${final_price:,.2f}\033[m")
print("=" * 50)
print("🥳 Obrigado e volte sempre às Lojas Loucas! 🥳".center(50))
print("=" * 50)
