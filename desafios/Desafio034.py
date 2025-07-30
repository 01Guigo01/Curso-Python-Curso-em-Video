"""

DESESAFIO 034

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a 2.000,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

"""

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA DE AUMENTO SALARIAL ✨".center(50))
print("Seu futuro financeiro começa aqui!".center(50))
print("=" * 50)

salary = float(input("💰 Digite o seu salário atual: R$"))

print(f"\nAnalisando seu salário de \033[1;36mR${salary:,.2f}\033[m para calcular o aumento...")
time.sleep(2)

print("\n" + "=" * 50)
print("📈 DETALHES DO SEU NOVO SALÁRIO 📈".center(50))
print("=" * 50)

if salary > 2000:
    increase_percentage = 10
    increase_value = salary * (increase_percentage / 100)
    new_salary = salary + increase_value

    print(f"Salário original: \033[1;34mR${salary:,.2f}\033[m")
    print(f"Aumento aplicado: \033[1;33m{increase_percentage}%\033[m")
    print("-" * 50)
    print(f"🎉 Você teve um aumento de: \033[1;32mR${increase_value:,.2f}\033[m!")
    print(f"✅ SEU NOVO SALÁRIO É: \033[1;32mR${new_salary:,.2f}\033[m")
    print(emoji.emojize(":money_bag: :chart_increasing:"))

else:
    increase_percentage = 15
    increase_value = salary * (increase_percentage / 100)
    new_salary = salary + increase_value

    print(f"Salário original: \033[1;34mR${salary:,.2f}\033[m")
    print(f"Aumento aplicado: \033[1;33m{increase_percentage}%\033[m")
    print("-" * 50)
    print(f"🎉 Parabéns! Você teve um aumento de: \033[1;32mR${increase_value:,.2f}\033[m!")
    print(f"✅ SEU NOVO SALÁRIO É: \033[1;32mR${new_salary:,.2f}\033[m")
    print(emoji.emojize(":money_bag: :star-struck:"))

print("=" * 50)
print("🥳 Continue prestando um excelente serviço! Sua dedicação é valorizada! 🥳".center(50))
print("=" * 50)
