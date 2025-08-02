"""

DESESAFIO 033

Faça um programaque leia três números e mostre qual é o maior e qual é o menor.

"""

import time

print("=" * 50)
print("✨ ANALISADOR DE NÚMEROS: MAIOR E MENOR ✨".center(50))
print("Descubra os extremos dos seus números!".center(50))
print("=" * 50)

num1 = int(input('🔢 Digite o PRIMEIRO número inteiro: '))
num2 = int(input('🔢 Digite o SEGUNDO número inteiro: '))
num3 = int(input('🔢 Digite o TERCEIRO número inteiro: '))

print(f"\nAnalisando os números: \033[1;36m{num1}\033[m, \033[1;36m{num2}\033[m e \033[1;36m{num3}\033[m...")
time.sleep(2)

# Lógica para encontrar o maior número
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Lógica para encontrar o menor número
smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print("\n" + "=" * 50)
print("🏆 RESULTADOS DA ANÁLISE 🏆".center(50))
print("=" * 50)

print(f"O MAIOR número digitado foi: \033[1;32m{largest}\033[m! 🎉") # Maior em verde
print(f"O MENOR número digitado foi: \033[1;31m{smallest}\033[m. 📉") # Menor em vermelho

print("=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
