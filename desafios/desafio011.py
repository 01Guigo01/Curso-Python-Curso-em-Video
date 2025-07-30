""""

DESAFIO 011

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessário para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m².

"""

import time

print("=" * 50)
print("✨ CALCULADORA DE TINTA PARA PAREDES ✨".center(50))
print("=" * 50)

width = float(input("📐 Digite a LARGURA da parede em metros (m): "))
height = float(input("📏 Digite a ALTURA da parede em metros (m): "))

print(f"\nCalculando as dimensões da parede de \033[1;36m{width:.2f}m x {height:.2f}m\033[m...")
time.sleep(2)


area = width * height
liter_ink = area / 2

print("\n" + "=" * 50)
print("🖌️ RESULTADOS DO ORÇAMENTO DE TINTA 🖌️".center(50)) # Título dos resultados
print("=" * 50)

print(f"Sua parede tem as dimensões de \033[1;34m{width:.2f}m x {height:.2f}m\033[m.")
print(f"A área total a ser pintada é de: \033[1;32m{area:.2f}m²\033[m.")
print("-" * 50)

print(f"Para pintar essa parede, você precisará de:")
print(f"🎨 \033[1;33m{liter_ink:.2f} litros de tinta\033[m!") # Litros de tinta em amarelo
print("\nLembre-se: 1 litro de tinta cobre aproximadamente 2m².")

print("=" * 50)
print("ORÇAMENTO CONCLUÍDO!".center(50))
print("=" * 50)
