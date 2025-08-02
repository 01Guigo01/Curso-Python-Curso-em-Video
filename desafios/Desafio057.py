"""

Desafio057

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'ou 'F'. Caso esteja errado, peça a ditação
novamente até ter um valor correto.

"""
import time
import emoji

print("=" * 50)
print("✨ VALIDADOR DE SEXO ✨".center(50))
print("Vamos registrar seu sexo de forma segura.".center(50))
print("=" * 50)

sexo = str(input('🚻 Informe o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print("\n❌ Dados inválidos! Por favor, tente novamente.")
    time.sleep(1)
    sexo = str(input("🚻 Por favor, informe o seu sexo: ")).strip().upper()[0]

print("\n" + "=" * 50)
print("🎉 CADASTRO CONCLUÍDO! 🎉".center(50))
print("=" * 50)
print(f"O seu sexo '\033[1;32m{sexo}\033[m' foi registrado com sucesso. Obrigado!")
print(emoji.emojize(":white_heavy_check_mark: :partying_face:"))
print("=" * 50)
print("REGISTRO CONCLUÍDO!".center(50))
print("=" * 50)
