"""

Desafio 056 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.

- Qual é o nome do homem mais velho.

- Quantas mulheres têm menos de 20 anos.

"""
import time
import emoji

print("=" * 50)
print("✨ ANALISADOR DE GRUPO FAMILIAR ✨".center(50))
print("Descubra os detalhes do seu grupo!".center(50))
print("=" * 50)

sum_ages = 0
age_oldest_man = 0
name_oldest_man = ""
number_of_women_less_20 = 0

print("\n🤯 Vamos analisar as informações de 5 pessoas. Prepare-se!")
time.sleep(1.5)

for c in range(1, 6):
    print(f"\n--- CADASTRO DA \033[1;36m{c}ª\033[m PESSOA ---")
    name = str(input("📝 Digite seu nome: ")).strip().upper()
    age = int(input("🎂 Digite sua idade: "))
    gender = str(input("🚻 Digite seu sexo (M/F): ")).strip().upper()

    sum_ages += age

    if gender == "M" and age > age_oldest_man:
        age_oldest_man = age
        name_oldest_man = name

    if gender == "F" and age < 20:
        number_of_women_less_20 += 1

average_age = sum_ages / 5

print("\n" + "=" * 50)
print("🏆 RESULTADOS DA ANÁLISE DO GRUPO 🏆".center(50))
print("=" * 50)

print(f"📊 A média de idade do grupo é de: \033[1;33m{average_age:.0f}\033[m anos.")

if name_oldest_man:
    print(
        f"👴 O homem mais velho se chama \033[1;32m{name_oldest_man.title()}\033[m e tem \033[1;32m{age_oldest_man}\033[m anos.")
else:
    print("😔 Não foi registrado nenhum homem no grupo para esta análise.")

print(f"👧 Nesse grupo, há \033[1;31m{number_of_women_less_20}\033[m mulheres com menos de 20 anos.")

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA COM SUCESSO!".center(50))
print("=" * 50)
