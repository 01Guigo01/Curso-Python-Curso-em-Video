"""

DESAFIO 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos aluno. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.

"""

from random import shuffle
import time

print("=" * 50)
print("✨ SORTEIO DA ORDEM DE APRESENTAÇÃO ✨".center(50))
print("Quem será o próximo a apresentar?".center(50))
print("=" * 50)

student_1 = str(input("🧑‍🎓 Digite o nome do 1º aluno: ")).strip().title()
student_2 = str(input("🧑‍🎓 Digite o nome do 2º aluno: ")).strip().title()
student_3 = str(input("🧑‍🎓 Digite o nome do 3º aluno: ")).strip().title()
student_4 = str(input("🧑‍🎓 Digite o nome do 4º aluno: ")).strip().title()

students = [student_1, student_2, student_3, student_4]

print("\nEmbaralhando a ordem dos alunos... Preparar, apontar, VAI!")
time.sleep(2) # Pausa para suspense

shuffle(students)

print("\n" + "=" * 50)
print("📋 ORDEM DE APRESENTAÇÃO DEFINIDA! 📋".center(50))
print("=" * 50)

# Exibe a lista embaralhada
print("A sequência de apresentação será:")
for i, student in enumerate(students):
    print(f"   {i+1}º - \033[1;32m{student}\033[m") # Alunos em destaque verde
    time.sleep(0.5) # Pequena pausa entre cada nome para um efeito de revelação

print("\n" + "=" * 50)
print("SORTEIO CONCLUÍDO!".center(50))
print("Boa sorte a todos!".center(50))
print("=" * 50)
