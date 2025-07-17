""""
DESAFIO 011

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessário para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m²

"""

width = float(input("Largura da parede (m): "))
height = float(input("Altura da parede (m): "))
area = width * height
liter_ink = area / 2

print("-" * 150)

print(f"Sua parede tem a dimensão de {width}x{height} e sua área é de {area:.2f}m².")
print(f"Para pintar essa parede, você precisará de {liter_ink:.2f}l de tinta.")

print("-" * 150)
