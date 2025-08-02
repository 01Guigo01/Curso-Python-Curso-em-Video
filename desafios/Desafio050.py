"""

Desafio 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apena daqueles que forem pares. Se o valor
digitado for impar desconsidere-o.

"""

import time
import emoji

print("=" * 50)
print("✨ ANALISADOR DE VALORES ✨".center(50))
print("Somando apenas os números pares!".center(50))
print("=" * 50)

soma_pares = 0
numeros_pares = []

print("\n🤯 Prepare-se! Vamos somar os números que você digitar.")
time.sleep(1.5)

for c in range(1, 7):
    num_input = input(f"🔢 Digite o \033[1;36m{c}º\033[m número: ")

    # Validação simples para evitar que o programa trave com letras
    if not num_input.isdigit():
        print("❌ Entrada inválida! Digite apenas números inteiros. O programa será encerrado.")
        exit()

    num = int(num_input)

    if num % 2 == 0:
        soma_pares += num
        numeros_pares.append(num)

print("\n" + "=" * 50)
print("💰 RESULTADO DA SOMA 💰".center(50))
print("=" * 50)

if not numeros_pares:
    print("😔 Nenhum número par foi digitado. A soma total é: \033[1;31m0\033[m.")
else:
    print(f"✔️ Os números pares digitados foram: \033[1;34m{', '.join(map(str, numeros_pares))}\033[m")
    print("-" * 50)
    print(f"🎉 A soma total desses números é: \033[1;32m{soma_pares}\033[m!")
    print(emoji.emojize(":partying_face: :trophy: :star-struck:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
