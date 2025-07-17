"""
DESAFIO 012

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto.

"""

print("=" * 50)
print("LOJAS LOUCAS".center(50))
print("Seu Cupom de Desconto".center(50))
print("=" * 50)

product_value = float(input("Digite o valor do produto: R$"))
discount_percentage = int(input("Digite o desconto (%): "))


discount_amount = product_value * (discount_percentage / 100)
final_price = product_value - discount_amount

print("-" * 50)
print(f"Preço original: R$ {product_value:,.2f}")
print(f"Desconto aplicado: {discount_percentage}%")
print("-" * 50)
print(f"Você economizou: R$ {discount_amount:,.2f}")
print(f"Valor a pagar: R$ {final_price:,.2f}")
print("=" * 50)
print("Obrigado e volte sempre!".center(50))
print("=" * 50)