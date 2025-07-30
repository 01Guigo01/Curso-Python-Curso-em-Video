"""

DESAFIO 002

Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

"""

name = input("👋 Olá! Por favor, digite seu nome: ").strip()
print("\nPreparando uma calorosa recepção...")

print("=" * 50)
print(f"🎉 Seja muito bem-vindo(a), \033[1;32m{name.title()}\033[m!".center(50)) # Nome em verde e capitalizado
print("=" * 50)

print("\nÉ um prazer ter você aqui!")
print("Espero que aproveite o nosso programa.")

print("\n" + "=" * 50)
print("PRONTO PARA COMEÇAR!".center(50))
print("=" * 50)
