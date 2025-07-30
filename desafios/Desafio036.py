"""

DESESAFIO 036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela nãO pode exceder 30% do salário ou entãO o empréstimo será
negado.

"""
from time import sleep

print("=" * 50)

print("CALCULADORA DE EMPRESTIMO".center(50))

value_house = float(input("Digite o valor da casa: R$"))
salary = float(input("Digite seu salário: R$"))
installments = int(input("Em quantas parcelas você vai pagar?: "))

# Convertendo anos para meses para calcular a prestação mensal
# Mantenho o nome da variável 'installments' para o número de anos, como no seu código original
# E calculo os meses para a divisão
total_months = installments * 12
value_installments = value_house / total_months

sleep(2) # Reduzi um pouco o tempo de espera para ser mais ágil
print("ANALISANDO SEUS DADOS".center(50))

# Calculando o limite de 30% do salário
limit_30_percent_salary = salary * (30 / 100)

print("-" * 50)
print(f"Valor da casa: R${value_house:,.2f}")
print(f"Seu salário: R${salary:,.2f}")
print(f"Parcelamento em: {installments} anos ({total_months} meses)")
print(f"Valor da prestação mensal: R${value_installments:,.2f}")
print(f"30% do seu salário (limite): R${limit_30_percent_salary:,.2f}")
print("-" * 50)

# A lógica principal: se a prestação for menor ou igual ao limite, aprova.
# Se for maior, nega.
if value_installments <= limit_30_percent_salary:
    print(f"\n\033[1;32mSeu salário atual é de R${salary:,.2f}, e o valor das parcelas em {installments} anos "
          f"ficou no valor de R${value_installments:,.2f}, por tanto seu empréstimo foi APROVADO!!! 🎉\033[m")
elif value_installments > limit_30_percent_salary: # Esta condição pega o caso de ser maior
    print(f"\n\033[1;31mSeu salário atual é de R${salary:,.2f}, e o valor das parcelas em {installments} anos "
          f"ficou no valor de R${value_installments:,.2f}, por tanto seu empréstimo foi NEGADO!!! ❌\033[m")
    print(f"A prestação excede 30% do seu salário (R${limit_30_percent_salary:,.2f}).")


print("=" * 50)
