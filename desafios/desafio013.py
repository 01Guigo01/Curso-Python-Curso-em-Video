"""
DESAFIO 013

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

"""

print("=" * 50)
print("LOJAS LOUCAS SETOR DE RH".center(50))
print("Seu aumento de salário".center(50))
print("=" * 50)


salary = float(input("Digite o seu salário atual: R$"))
actual_increase= int(input("Digite o quanto de aumento você quer: (%): "))


increase_value = salary * (actual_increase / 100)
new_salary = salary + increase_value

print("-" * 50)
print(f"salario original: R$ {salary:,.2f}")
print(f"Aumento aplicado: {actual_increase}%")
print("-" * 50)
print(f"Você teve um aumento de: R$ {increase_value:,.2f}")
print(f"Seu novo salário é: R$ {new_salary:,.2f}")
print("=" * 50)
print("Continue prestando um bom serviço!".center(50))
print("=" * 50)