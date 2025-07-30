"""

DESAFIO 015

Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

import time

print("=" * 50)
print("🚗 ALUGUEL DE CARROS 💨".center(50))
print("Seu Orçamento Personalizado".center(50))
print("=" * 50)

rented_days = int(input("🗓️ Por quantos dias o carro foi alugado? "))
km_driven = float(input("🛣️ Quantos Km foram rodados com o carro? "))

print(f"\nCalculando seu orçamento para {rented_days} dias e {km_driven:.1f} Km rodados...")
time.sleep(2)

price_per_day = 60.00
price_per_km = 0.15

total_price = (rented_days * price_per_day) + (km_driven * price_per_km)

print("\n" + "=" * 50)
print("💰 DETALHES DO SEU ALUGUEL 💰".center(50))
print("=" * 50)

print(f"✔️ Dias de aluguel: \033[1;36m{rented_days} dias\033[m (R$ {price_per_day:.2f}/dia)")
print(f"✔️ Quilometragem percorrida: \033[1;36m{km_driven:.1f} Km\033[m (R$ {price_per_km:.2f}/Km)")
print("-" * 50)

print(f"O PREÇO TOTAL a pagar pelo aluguel é de: \033[1;32mR$ {total_price:.2f}\033[m! 🎉")

print("=" * 50)
print("AGRADECEMOS A PREFERÊNCIA!".center(50))
print("=" * 50)
