n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

if m >= 6:
    print(f"Aprovado sua média foi {m:.1f}")

else:
    print(f"Reprovado sua média foi {m:.1f}")