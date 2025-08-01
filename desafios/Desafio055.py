"""

Desafio 054

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""
import time
import emoji

print("=" * 50)
print("✨ BALANÇA MÁGICA: VERIFICADOR DE PESO ✨".center(50))
print("Descubra o maior e o menor peso entre 5 pessoas!".center(50))
print("=" * 50)

first_weight = float(input("⚖️ Digite o peso da 1ª pessoa (em kg): "))
maior_peso = first_weight
menor_peso = first_weight

print("\n🤯 Registrando os pesos... Isso pode levar um instante...")
time.sleep(1.5)

for c in range(2, 6):
    current_weight = float(input(f"⚖️ Digite o peso da {c}ª pessoa (em kg): "))

    print("\n🤯 Registrando os pesos... Isso pode levar um instante...")
    time.sleep(1.5)

    if current_weight > maior_peso:
        maior_peso = current_weight

    if current_weight < menor_peso:
        menor_peso = current_weight

print("\n" + "=" * 50)
print("🏆 RESULTADO FINAL DA PESAGEM 🏆".center(50))
print("=" * 50)

print(f"O MAIOR peso registrado foi: \033[1;32m{maior_peso:.2f}\033[m kg! 🎉")
print(f"O MENOR peso registrado foi: \033[1;31m{menor_peso:.2f}\033[m kg! 📉")
print(emoji.emojize(":partying_face: :weighing_scale:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
