"""

Desafio 044 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Elabore um programa uqe calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:

- À vista dinheiro/pix: 10% de desconto

- À vista no cartão: 5% de desconto

- Em até 2x no cartão: preço normal

- 3x ou mais no cartão: 20% de juros

"""

import time

print("=" * 50)
print("✨ CALCULADORA DE PAGAMENTOS ✨".center(50))
print("=" * 50)

# Solicita o preço do produto (mantendo suas preferências, sem try-except)
product_price = float(input("Digite o valor normal do produto: R$"))

# Apresenta as opções de pagamento
print("\nEscolha a condição de pagamento:")
print("[ 1 ] À vista Dinheiro/Pix (10% de desconto)")
print("[ 2 ] À vista no Cartão (5% de desconto)")
print("[ 3 ] Em até 2x no Cartão (Preço Normal)")
print("[ 4 ] 3x ou mais no Cartão (20% de juros)")


payment_method = int(input("Sua opção: "))

print("\nProcessando sua escolha de pagamento...")
time.sleep(2)

print("-" * 50)
print(f"Preço original do produto: R${product_price:.2f}")
print("-" * 50)


if payment_method == 1:
    discount_percentage = 10
    discount_amount = product_price * (discount_percentage / 100)
    final_price = product_price - discount_amount
    print(f"\n💰 Você escolheu 'À vista Dinheiro/Pix'.")
    print(f"Desconto de {discount_percentage}% aplicado: R${discount_amount:.2f}")
    print(f"O NOVO PREÇO a pagar é: \033[1;32mR${final_price:.2f}\033[m") # Verde para desconto
    print(f"Você economizou \033[1;32mR${discount_amount:.2f}\033[m neste produto! 🎉")

elif payment_method == 2:
    discount_percentage = 5
    discount_amount = product_price * (discount_percentage / 100)
    final_price = product_price - discount_amount
    print(f"\n💳 Você escolheu 'À vista no Cartão'.")
    print(f"Desconto de {discount_percentage}% aplicado: R${discount_amount:.2f}")
    print(f"O NOVO PREÇO a pagar é: \033[1;32mR${final_price:.2f}\033[m") # Verde para desconto
    print(f"Você economizou \033[1;32mR${discount_amount:.2f}\033[m neste produto! 🌟")

elif payment_method == 3:
    final_price = product_price
    print(f"\n🛒 Você escolheu 'Em até 2x no Cartão'.")
    print(f"O preço permanece o normal.")
    print(f"O VALOR FINAL a pagar é: \033[1;34mR${final_price:.2f}\033[m") # Azul para preço normal
    print("Parcelas: 2x de R$", final_price / 2) # Exemplo de parcelamento

elif payment_method == 4:
    interest_percentage = 20
    interest_amount = product_price * (interest_percentage / 100)
    final_price = product_price + interest_amount
    print(f"\n💸 Você escolheu '3x ou mais no Cartão'.")
    print(f"Juros de {interest_percentage}% aplicados: R${interest_amount:.2f}")
    print(f"O NOVO PREÇO a pagar é: \033[1;31mR${final_price:.2f}\033[m") # Vermelho para juros
    print(f"O valor do produto teve um acréscimo de \033[1;31mR${interest_amount:.2f}\033[m. 😔")
    print("Exemplo: 3x de R$", final_price / 3)

elif payment_method not in [1, 2, 3, 4]:
    print("\n❌ OPÇÃO DE PAGAMENTO INVÁLIDA! Por favor, escolha um número de 1 a 4.")

print("\n" + "=" * 50)
print("CÁLCULO DE PAGAMENTO CONCLUÍDO!".center(50))
print("=" * 50)
