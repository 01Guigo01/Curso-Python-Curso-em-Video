"""
DESAFIO 004

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele

"""

value = input("Digite algo: ")

print("=" * 50)
print(f"Analisando o valor '{value}'...".center(50))
print("=" * 50)

print(f"O tipo primitivo desse valor é {type(value)}")

# Adicionando uma verificação útil para espaços em branco
print(f"Só tem espaços? {value.isspace()}")

# Verificações de tipo de caractere
print(f"É um número? {value.isnumeric()}")
print(f"É alfabético? {value.isalpha()}")
print(f"É alfanumérico? {value.isalnum()}")  # CORREÇÃO: Usando o método correto

# Verificações de formatação de texto (case)
print(f"Está totalmente em maiúsculas? {value.isupper()}")
print(f"Está totalmente em minúsculas? {value.islower()}") # CORREÇÃO: Texto corrigido
print(f"Está capitalizada (formato de título)? {value.istitle()}")

print("=" * 50)