"""

Desafio061

Refaça o Desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.

"""

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA DE PROGRESSÃO ARITMÉTICA ✨".center(50))
print("Descubra os 10 primeiros termos da sua PA!".center(50))
print("=" * 50)

first_term = int(input("🔢 Digite o PRIMEIRO termo da PA: "))
reason = int(input("➕ Digite a RAZÃO da PA: "))

print(f"\nCalculando os 10 primeiros termos da PA com primeiro termo \033[1;36m{first_term}\033[m e razão \033[1;36m{reason}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("📝 OS 10 PRIMEIROS TERMOS DA PA SÃO: 📝".center(50))
print("=" * 50)

current_term = first_term
count = 1

while count <= 10:
    print(f"👉 {count}º termo: \033[1;32m{current_term}\033[m")
    current_term += reason
    count += 1
    time.sleep(0.3)

print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
print(emoji.emojize(":partying_face: :money_bag:"))
print("=" * 50)