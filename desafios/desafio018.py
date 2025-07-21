"""
DESAFIO 018

Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

"""

from math import sin, cos, tan, radians

print("=" * 50)

# Solicita ao usuário que digite um ângulo em graus
angle_degrees = float(input("Digite um ângulo qualquer (em graus): "))

# Converte o ângulo de graus para radianos
angle_radians = radians(angle_degrees)

# Calcula o seno, cosseno e tangente do ângulo
sine_value = sin(angle_radians)
cosine_value = cos(angle_radians)
tangent_value = tan(angle_radians)

# Exibe os resultados formatados com duas casas decimais
print(f"Para o ângulo de {angle_degrees}°:")
print(f"O SENO é: {sine_value:.2f}")
print(f"O COSSENO é: {cosine_value:.2f}")
print(f"A TANGENTE é: {tangent_value:.2f}")

print("=" * 50)