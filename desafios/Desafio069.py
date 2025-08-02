"""

Desafio069

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o progrma deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessaos tem mais de 18 anos.

B) Quantos homens foram cadastradas.

C) Quantas mulheres tem menos de 20 anos.

"""

import time
import emoji

print("=" * 50)
print("✨ ANALISADOR DE GRUPO FAMILIAR ✨".center(50))
print("Cadastre pessoas e veja as estatísticas!".center(50))
print("=" * 50)

adult_count = 0
men_count = 0
women_under_20_count = 0
keep_going = 'S'
person_number = 0

while keep_going == 'S':
    person_number += 1
    print(f"\n--- CADASTRO DA \033[1;36m{person_number}ª\033[m PESSOA ---")

    age = int(input("🎂 Idade: "))

    gender_valid = False
    while not gender_valid:
        gender = str(input("🚻 Sexo [M/F]: ")).strip().upper()[0]
        if gender in 'MF':
            gender_valid = True
        else:
            print("❌ Entrada inválida! Digite 'M' para Masculino ou 'F' para Feminino.")
            time.sleep(1)

    if age > 18:
        adult_count += 1

    if gender == 'M':
        men_count += 1

    if gender == 'F' and age < 20:
        women_under_20_count += 1

    keep_going_valid = False
    while not keep_going_valid:
        print("\n" + "=" * 50)
        keep_going = str(input("Quer continuar a cadastrar? [S/N]: ")).strip().upper()[0]
        print("=" * 50)
        if keep_going in 'SN':
            keep_going_valid = True
        else:
            print("❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            time.sleep(1)

print("\n" + "=" * 50)
print("📊 RESULTADO FINAL DA ANÁLISE 📊".center(50))
print("=" * 50)

print(f"Pessoas com mais de 18 anos: \033[1;32m{adult_count}\033[m ✨")
print(f"Homens cadastrados: \033[1;36m{men_count}\033[m 👨")
print(f"Mulheres com menos de 20 anos: \033[1;31m{women_under_20_count}\033[m 👩‍🦱")

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
