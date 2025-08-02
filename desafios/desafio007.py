""""

DESAFIO 007

Desenvolva um programa que leia as notas de um aluno nos 4 bimestres e mostre sua média.

"""

import time
print("=" * 50)
print("✨ CALCULADORA DE MÉDIA ESCOLAR ✨".center(50))
print("=" * 50)

print("\nPor favor, insira as notas de cada bimestre.")
grade_1 = float(input("📝 Digite a nota do 1º Bimestre: "))
grade_2 = float(input("📝 Digite a nota do 2º Bimestre: "))
grade_3 = float(input("📝 Digite a nota do 3º Bimestre: "))
grade_4 = float(input("📝 Digite a nota do 4º Bimestre: "))

print("\nCalculando a média final do(a) aluno(a)...")
time.sleep(2)

final_average = (grade_1 + grade_2 + grade_3 + grade_4) / 4

print("\n" + "=" * 50)
print("📚 BOLETIM DE DESEMPENHO ANUAL 📚".center(50))
print("=" * 50)

print(f"Notas registradas:")
print(f"  1º Bimestre: \033[1;36m{grade_1:.1f}\033[m")
print(f"  2º Bimestre: \033[1;36m{grade_2:.1f}\033[m")
print(f"  3º Bimestre: \033[1;36m{grade_3:.1f}\033[m")
print(f"  4º Bimestre: \033[1;36m{grade_4:.1f}\033[m")
print("-" * 50)


print(f"✨ A MÉDIA FINAL CALCULADA FOI: \033[1;32m{final_average:.1f}\033[m ✨") # Média em verde
print("-" * 50)

print("\n" + "=" * 50)
print("ANÁLISE DE MÉDIA CONCLUÍDA!".center(50))
print("=" * 50)
