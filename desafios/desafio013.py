"""

DESAFIO 013

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

"""

import time

print("=" * 50)
print("✨ LOJAS LOUCAS: SETOR DE RH ✨".center(50))
print("📈 Seu Aumento de Salário 📈".center(50))
print("=" * 50)

salary = float(input("💲 Digite o seu salário atual: R$"))
actual_increase = int(input("🎯 Digite a porcentagem de aumento desejada (ex: 10 para 10%): "))

print(f"\nProcessando seu pedido de aumento de \033[1;36m{actual_increase}%\033[m sobre \033[1;36mR${salary:.2f}\033[m...")
time.sleep(2)

increase_value = salary * (actual_increase / 100)
new_salary = salary + increase_value

print("\n" + "=" * 50)
print("💰 DETALHES DO SEU NOVO SALÁRIO 💰".center(50))
print("=" * 50)

print(f"Salário original: \033[1;34mR${salary:,.2f}\033[m")
print(f"Aumento solicitado: \033[1;33m{actual_increase}%\033[m")
print("-" * 50)

print(f"🎉 Você teve um aumento de: \033[1;32mR${increase_value:,.2f}\033[m!")
print(f"✅ SEU NOVO SALÁRIO É: \033[1;32mR${new_salary:,.2f}\033[m")

print("=" * 50)
print("🥳 Continue prestando um bom serviço! Sua dedicação vale ouro! 🥳".center(50))
print("=" * 50)
