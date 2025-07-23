"""
DESESAFIO 024

Crie um programa que leia o nome de uma cidade e diga se ela começa ou nãO COM O NOME "SANTO"

"""

print("=" * 50)

print("VERIFICADOR DE NOME CIDADE".center(50))

name_ciy = str(input("Digte o nome da sua cidade: ")).strip().upper()
find_santo = name_ciy.startswith("SANTO")

print(f"A cidade '{name_ciy}' {'COMEÇA' if find_santo else 'NÃO começa'} com 'Santo'.")

print("=" * 50)