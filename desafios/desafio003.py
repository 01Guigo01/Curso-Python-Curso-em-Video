"""

DESAFIO 003

Crie um programa que leia dois números e mostre a soma entre eles.

"""

print("=" * 50)
print("✨ CALCULADORA SIMPLES DE SOMA ✨".center(50))
print("=" * 50)

num_1 = int(input("🔢 Digite o PRIMEIRO valor inteiro: "))
num_2 = int(input("➕ Digite o SEGUNDO valor inteiro: "))


sum_result = num_1 + num_2

print("\n" + "-" * 50)
print(f"Valores informados: {num_1} e {num_2}")
print(f"🎉 A SOMA entre \033[1;36m{num_1}\033[m e \033[1;36m{num_2}\033[m é igual a \033[1;32m{sum_result}\033[m!".center(50))
print("-" * 50)
print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
