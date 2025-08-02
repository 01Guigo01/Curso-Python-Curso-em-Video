"""

DESESAFIO 040 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Cire um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no fianl de acordo com
a média atingida:

-Média abaixo de 5.0:

REPROVADO

-Média entre 5.0 e 6.9:

RECUPERAÇÃO

-Média 7.0 ou superior:

APROVADO

"""
import time

print("=" * 50)
print("✨ VERIFICADOR DE NOTAS ✨".center(50))
print("=" * 50)


grade_1 = float(input("Digite a nota do 1º Bimestre: "))
grade_2 = float(input("Digite a nota do 2º Bimestre: "))
grade_3 = float(input("Digite a nota do 3º Bimestre: "))
grade_4 = float(input("Digite a nota do 4º Bimestre: "))

print("\nCalculando sua média final...")
time.sleep(2)

average = (grade_1 + grade_2 + grade_3 + grade_4) / 4

print("-" * 50)
print(f"Notas registradas:")
print(f"1º Bimestre: {grade_1:.2f}")
print(f"2º Bimestre: {grade_2:.2f}")
print(f"3º Bimestre: {grade_3:.2f}")
print(f"4º Bimestre: {grade_4:.2f}")
print(f"MÉDIA FINAL: {average:.2f}")
print("-" * 50)

if average < 5:
    print(f"\n💔 Sua média foi \033[1;31m{average:.2f}\033[m. Que pena! Você foi \033[1;31mREPROVADO\033[m.")
    print("É importante revisar o conteúdo e se preparar melhor. Não desista dos estudos!")
elif 5 <= average <= 6.9:
    print(f"\n⚠️ Sua média foi \033[1;33m{average:.2f}\033[m. Você está de \033[1;33mRECUPERAÇÃO\033[m!")
    print("Este é o momento de dar um gás extra! Com esforço, você consegue!")
elif average >= 7:
    print(f"\n🎉 Sua média foi \033[1;32m{average:.2f}\033[m. Parabéns! Você foi \033[1;32mAPROVADO\033[m!")
    print("Excelente trabalho! Continue assim e celebre sua conquista!")

print("\n" + "=" * 50)
print("AVALIAÇÃO CONCLUÍDA!".center(50))
print("=" * 50)
