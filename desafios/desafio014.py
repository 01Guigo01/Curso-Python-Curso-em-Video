"""
DESAFIO 014

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

"""

print("=" * 50)
print("CONVERSOR DE TEMPERATURAS".center(50))

cel = float(input("Digite a temperatura em Celsius: "))
fah = (cel * 9/5) + 32

print(f"A Temperatura atual é de em {cel}ºC ou"
      f"\n{fah:1f}ºF")

print("=" * 50)