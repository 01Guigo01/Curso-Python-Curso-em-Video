""""
DESAFIO 007

Desenvolva um programa que leia as notas de um aluno nos 4 bimestres e mostre sua média

"""
print("=" * 50)
print(" CALCULADORA DE MÉDIA ESCOLAR ".center(50, "="))
print("=" * 50)


grade_1 = float(input("Digite a nota do 1º Bimestre: "))
grade_2 = float(input("Digite a nota do 2º Bimestre: "))
grade_3 = float(input("Digite a nota do 3º Bimestre: "))
grade_4 = float(input("Digite a nota do 4º Bimestre: "))

final_average = (grade_1 + grade_2 + grade_3 + grade_4) / 4

print("\n" + "-" * 50)
print(" BOLETIM FINAL DO ALUNO ".center(50))
print("-" * 50)

print(f"A média final foi: {final_average:.1f}")

print("=" * 50)