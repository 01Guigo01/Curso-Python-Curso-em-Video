"""

DESAFIO 004

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele.

"""

print("=" * 50)
print("✨ DETECTOR DE CARACTERÍSTICAS DE ENTRADA ✨".center(50)) # Título mais expressivo
print("=" * 50)

value = input("✍️ Digite algo para ser analisado: ").strip() # Adicionei um emoji e .strip() para limpeza inicial

print(f"\nPreparando a análise do valor: '\033[1;36m{value}\033[m'...") # Destacando o valor em ciano

print("\n" + "-" * 50)
print("🔎 RESULTADOS DA ANÁLISE:".center(50))
print("-" * 50)

print(f"Tipo primitivo desse valor: \033[1;33m{type(value)}\033[m") # Tipo em amarelo

print(f"Só tem espaços? {'✅' if value.isspace() else '❌'} {value.isspace()}")
print(f"É um número? {'✅' if value.isnumeric() else '❌'} {value.isnumeric()}")
print(f"É alfabético? {'✅' if value.isalpha() else '❌'} {value.isalpha()}")
print(f"É alfanumérico? {'✅' if value.isalnum() else '❌'} {value.isalnum()}")

# Verificações de formatação de texto (case)
print(f"Está totalmente em maiúsculas? {'✅' if value.isupper() else '❌'} {value.isupper()}")
print(f"Está totalmente em minúsculas? {'✅' if value.islower() else '❌'} {value.islower()}")
print(f"Está capitalizada (formato de título)? {'✅' if value.istitle() else '❌'} {value.istitle()}")

print("-" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
