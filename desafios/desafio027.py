"""

DESESAFIO 027

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

"""

import time

print("=" * 50)
print("✨ IDENTIFICADOR DE NOMES ✨".center(50))
print("Descubra o início e o fim do seu nome!".center(50))
print("=" * 50)

full_name = str(input("✍️ Digite seu nome completo: ")).strip()

# Validação simples para garantir que o nome não está vazio e tem pelo menos duas partes
if not full_name or len(full_name.split()) < 2:
    print("\n❌ Entrada inválida! Por favor, digite seu nome completo (com pelo menos um sobrenome).")
    print("=" * 50)
    exit()

print(f"\nAnalisando o nome: '\033[1;36m{full_name.title()}\033[m'...")
time.sleep(2)

name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[-1]

print("\n" + "=" * 50)
print("🔍 COMPOSIÇÃO DO SEU NOME 🔍".center(50))
print("=" * 50)

print(f"Seu nome completo é: \033[1;34m{full_name.title()}\033[m")
print(f"Seu PRIMEIRO nome é: \033[1;32m{first_name.title()}\033[m 🎉")
print(f"Seu ÚLTIMO nome é: \033[1;33m{last_name.title()}\033[m")

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
