"""
DESAFIO 008

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros,
além de outras unidades de medida.

"""

meters = float(input("Digite uma distância em metros: "))

centimeters = meters * 100      # 1 cm = 0.01 m
millimeters = meters * 1000     # 1 mm = 0.001 m

# --- Apresentação da Tabela de Conversão ---
print("=" * 50)
print(f"A medida de {meters}m corresponde a:".center(50))
print("-" * 50)

# Displaying conversions with appropriate formatting
print(f"{centimeters:.0f} cm (Centímetros)")   # No decimal for exact centimeters
print(f"{millimeters:.0f} mm (Milímetros)")     # No decimal for exact millimeters

print("=" * 50)