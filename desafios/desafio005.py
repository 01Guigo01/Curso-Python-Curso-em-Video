"""

DESAFIO 005

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

"""

print("=" * 50)
print("✨ DESCOBRINDO O ANTECESSOR E SUCESSOR ✨".center(50)) # Título mais convidativo
print("=" * 50)
num = int(input("🔢 Digite um número inteiro qualquer: "))

print(f"\nPreparando para analisar o número: \033[1;36m{num}\033[m...") # Destacando o número em ciano

print("\n" + "-" * 50)
print("🔎 RESULTADOS DA ANÁLISE:".center(50))
print("-" * 50)

print(f"👉 O número que vem ANTES de \033[1;36m{num}\033[m é o \033[1;31m{num - 1}\033[m. (Antecessor)") # Antecessor em vermelho

print(f"👈 O número que vem DEPOIS de \033[1;36m{num}\033[m é o \033[1;32m{num + 1}\033[m. (Sucessor)") # Sucessor em verde

print("-" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
