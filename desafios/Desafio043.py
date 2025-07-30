"""

Desafio 043 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:

- Abaixo de 18.5: Abaixo do peso

- Entre 18.5 e 25: Peso Ideal

- 25 até 30: Sobrepeso

- 30 até 40: Obesidade

- Acima de 40: Obesidade Morbida

"""

import time

print("=" * 50)
print("✨ CALCULADORA DE IMC ✨".center(50))
print("=" * 50)

weight = float(input("Por favor, digite seu peso em Kg (ex: 70.5): "))
height = float(input("Agora, digite sua altura em metros (ex: 1.75): "))

print("\nCalculando seu Índice de Massa Corporal (IMC)...")
time.sleep(2)

bmi = weight / (height ** 2)

print("-" * 50)
print(f"Peso informado: {weight:.2f} Kg")
print(f"Altura informada: {height:.2f} m")
print(f"Seu IMC calculado é: {bmi:.2f}")
print("-" * 50)


if bmi < 18.5:
    print(f"\n⚠️ Opa! Com um IMC de \033[1;33m{bmi:.2f}\033[m, você está \033[1;33mABAIXO DO PESO\033[m.")
    print("É importante procurar um profissional de saúde para orientação adequada.")
elif 18.5 <= bmi <= 24.9: # Preferência por elif, ajustado para o limite exato do "peso ideal"
    print(f"\n✅ Parabéns! Com um IMC de \033[1;32m{bmi:.2f}\033[m, você está no \033[1;32mPESO IDEAL\033[m!")
    print("Mantenha seus hábitos saudáveis!")
elif 25 <= bmi <= 29.9: # Preferência por elif, ajustado para o limite exato do "sobrepeso"
    print(f"\n🟠 Atenção! Com um IMC de \033[1;31m{bmi:.2f}\033[m, você está com \033[1;31mSOBREPESO\033[m.")
    print("Um pequeno ajuste nos hábitos pode fazer uma grande diferença.")
elif 30 <= bmi <= 39.9: # Preferência por elif, ajustado para o limite exato da "obesidade"
    print(f"\n🔴 Cuidado! Com um IMC de \033[1;31m{bmi:.2f}\033[m, você está com \033[1;31mOBESIDADE\033[m.")
    print("É crucial buscar acompanhamento médico para melhorar sua saúde.")
elif bmi >= 40: # Preferência por elif, pega o caso de obesidade mórbida
    print(f"\n🚨 ALERTA MÁXIMO! Com um IMC de \033[1;35m{bmi:.2f}\033[m, você está com \033[1;35mOBESIDADE MÓRBIDA\033[m.")
    print("Procure ajuda médica URGENTE. Sua saúde é a prioridade número um!")

print("\n" + "=" * 50)
print("ANÁLISE DE IMC CONCLUÍDA!".center(50))
print("=" * 50)
