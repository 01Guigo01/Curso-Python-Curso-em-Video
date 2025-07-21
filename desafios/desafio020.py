"""
DESAFIO 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos aluno. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada

"""

from random import shuffle

print("=" * 50)

student_1 = str(input("Digite o nome do 1ºaluno: ")).capitalize()
student_2 = str(input("Digite o nome do 2ºaluno: ")).capitalize()
student_3 = str(input("Digite o nome do 3ºaluno: ")).capitalize()
student_4 = str(input("Digite o nome do 4ºaluno: ")).capitalize()

students = [student_1, student_2, student_3, student_4]

shuffle(students)

print(f"O aluno escolhido foi: {students}")

print("=" * 50)