"""

DESAFIO 019

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.

"""

from random import choice
import time

print("=" * 50)
print("✨ SORTEIO DE ALUNOS ✨".center(50))
print("Quem vai apresentar o trabalho?".center(50))
print("=" * 50)

student_1 = str(input("🧑‍🎓 Digite o nome do 1º aluno: ")).strip().title()
student_2 = str(input("🧑‍🎓 Digite o nome do 2º aluno: ")).strip().title()
student_3 = str(input("🧑‍🎓 Digite o nome do 3º aluno: ")).strip().title()
student_4 = str(input("🧑‍🎓 Digite o nome do 4º aluno: ")).strip().title()

students = [student_1, student_2, student_3, student_4]

print("\nRealizando o sorteio... Suspense no ar!")
time.sleep(2) # Pausa para aumentar a expectativa

print("\n" + "=" * 50)
print("🥁 E O ALUNO ESCOLHIDO FOI... 🥁".center(50))
print("=" * 50)

chosen = choice(students)

# Pequenas pausas para efeito dramático antes de revelar o nome
time.sleep(1)
print("...")
time.sleep(1)

print(f"🎉 PARABÉNS, \033[1;32m{chosen}\033[m! Você foi o(a) sorteado(a)! 🎉") # Nome em destaque verde
print("\n" + "=" * 50)
print("SORTEIO CONCLUÍDO!".center(50))
print("=" * 50)
