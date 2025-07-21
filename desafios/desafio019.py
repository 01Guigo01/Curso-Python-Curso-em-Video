"""
DESAFIO 019

Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido

"""

from random import choice

print("=" * 50)

student_1 = str(input("Digite o nome do 1ºaluno: ")).capitalize()
student_2 = str(input("Digite o nome do 2ºaluno: ")).capitalize()
student_3 = str(input("Digite o nome do 3ºaluno: ")).capitalize()
student_4 = str(input("Digite o nome do 4ºaluno: ")).capitalize()

students = [student_1, student_2, student_3, student_4]
chosen = choice(students)

print(f"O aluno escolhido foi: {chosen}")

print("=" * 50)