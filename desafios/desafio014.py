"""

DESAFIO 014

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

"""

import time

print("=" * 50)
print("✨ CONVERSOR DE TEMPERATURAS ✨".center(50))
print("=" * 50)

cel = float(input("🌡️ Digite a temperatura em Celsius (ºC): "))

print(f"\nConvertendo {cel:.1f}ºC para Fahrenheit...")
time.sleep(2)

fah = (cel * 9/5) + 32

print("\n" + "=" * 50)
print("❄️ RESULTADO DA CONVERSÃO 🔥".center(50))
print("=" * 50)

print(f"A temperatura de \033[1;36m{cel:.1f}ºC\033[m (Celsius) corresponde a:")
print(f"🌡️ \033[1;32m{fah:.1f}ºF\033[m (Fahrenheit)!")

print("=" * 50)
print("CONVERSÃO CONCLUÍDA!".center(50))
print("=" * 50)
