"""
DESESAFIO 025

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

"""

print("=" * 50)

print("VERIFICADOR DE NOME".center(50))

name_ciy = str(input("Digte o seu nome completo: ")).strip().upper()
find_silva = name_ciy.find("SILVA")

if find_silva == -1:
    print("O seu nome não possui Silva")
    print(name_ciy.title())
else:
    print("O seu nome possui Silva")

print("=" * 50)