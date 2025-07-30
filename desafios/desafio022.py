"""

DESESAFIO 022

Crie um programa quqe leia o nome completo de uma pessoa e mostre:

1 - O nome com todas as letras maíúsculos.

2 - O nome com todas as letras minúsculas.

3 - Quantas letras ao todo (sem considerar espaços).

4 - Quantas letras tem o primeiro nome.

"""

import time

print("=" * 50)
print("✨ ANALISADOR DE NOME COMPLETO ✨".center(50))
print("Descubra os segredos do seu nome!".center(50))
print("=" * 50)

name = str(input("✍️ Por favor, digite seu nome completo: ")).strip() # Adicionei emoji e .strip()

print(f"\nAnalisando o nome: '\033[1;36m{name}\033[m'...") # Destaca o nome em ciano
time.sleep(2) # Pausa para simular processamento

name_upper = name.upper()
name_lower = name.lower()
amount_name_not_space = len(name.replace(" ", ""))
amount_first_name = len(name.split()[0])

print("\n" + "=" * 50)
print("🔍 RESULTADOS DA ANÁLISE DO NOME 🔍".center(50))
print("=" * 50)

print(f"Capitalizado (Original): \033[1;34m{name.title()}\033[m") # Adicionado para clareza
print(f"Em letras MAIÚSCULAS: \033[1;32m{name_upper}\033[m")
print(f"Em letras minúsculas: \033[1;31m{name_lower}\033[m")
print("-" * 50) # Separador

print(f"Seu nome (sem espaços) tem: \033[1;33m{amount_name_not_space}\033[m caracteres.")
print(f"Seu PRIMEIRO nome ('\033[1;34m{name.split()[0]}\033[m') tem: \033[1;33m{amount_first_name}\033[m caracteres.")

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
