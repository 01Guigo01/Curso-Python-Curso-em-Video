""""

DESAFIO 010

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar.

"""

import time

print("=" * 50)
print("✨ CONVERSOR DE REAIS PARA MOEDAS ESTRANGEIRAS ✨".center(50))
print("=" * 50)

money = float(input("💰 Digite o valor em Reais (R$) para converter: "))

print(f"\nCalculando as conversões para \033[1;36mR${money:.2f}\033[m...")
time.sleep(2)

dolar_taxa = 5.55
euro_taxa = 6.45

dolar = money / dolar_taxa
euro = money / euro_taxa

print("\n" + "=" * 50)
print("💱 RESULTADOS DA CONVERSÃO 💱".center(50)) # Título da tabela
print("=" * 50)

print(f"Com \033[1;36mR${money:.2f}\033[m Reais, você pode ter:")
print("-" * 50)

print(f"💵 Dólares Americanos (USD): \033[1;32m${dolar:.2f}\033[m (Taxa: R${dolar_taxa:.2f}/USD)") # Dólar em verde
print(f"🇪🇺 Euros (EUR): \033[1;34m€{euro:.2f}\033[m (Taxa: R${euro_taxa:.2f}/EUR)") # Euro em azul

print("=" * 50)
print("CONVERSÕES CONCLUÍDAS!".center(50))
print("=" * 50)
