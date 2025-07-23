"""
DESESAFIO 027

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

"""

print("=" * 50)

full_name = str(input("Digite seu nome completo: ")).strip()
name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[-1]

print(f"Seu nome completo é: {full_name.title()}") #
print(f"Seu primeiro nome é: {first_name.title()}")
print(f"Seu último nome é: {last_name.title()}")

print("=" * 50)