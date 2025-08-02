"""

DESESAFIO 031

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens até 200Km e R$0,45 para viagens mais longas.

"""

import time

print("=" * 50)
print("✨ CALCULADORA DE VIAGENS INTELIGENTE ✨".center(50))
print("Seu orçamento de viagem na hora!".center(50))
print("=" * 50)

distance = float(input("🛣️ Digite a distância da sua viagem em Km: "))

print(f"\nCalculando o valor da sua viagem de \033[1;36m{distance:.1f} Km\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("💲 DETALHES DO SEU ORÇAMENTO 💲".center(50))
print("=" * 50)

if distance <= 200:
    ticket_value = distance * 0.50
    print(f"Sua viagem é de \033[1;34m{distance:.1f} Km\033[m.")
    print(f"Por ser uma viagem CURTA, o custo por Km é de \033[1;33mR$0.50\033[m.")
    print(f"O VALOR TOTAL da sua passagem será de: \033[1;32mR${ticket_value:.2f}\033[m! 🎉")
else:
    ticket_value = distance * 0.45
    print(f"Sua viagem é de \033[1;34m{distance:.1f} Km\033[m.")
    print(f"Por ser uma viagem LONGA, você GANHOU um desconto!")
    print(f"O custo por Km é de apenas \033[1;33mR$0.45\033[m.")
    print(f"O VALOR TOTAL da sua passagem será de: \033[1;32mR${ticket_value:.2f}\033[m! 🥳")

print("=" * 50)
print("BOA VIAGEM!".center(50))
print("=" * 50)
