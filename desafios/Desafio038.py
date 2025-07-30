"""

DESESAFIO 038

Escreva um progra que leia dois números inteiros e compare-os, mostrando na tela um mensagem:

- O primeiro valor é maior

- O segundo valor é maior

- Não existe valor, maior os são iguais

"""
from time import sleep

print("=" * 50)
print("COMPARADOR DE VALORES".center(50))
print("=" * 50)

# Pede os dois números ao usuário (sem tratamento de erro)
num_1 = int(input("Por favor, digite o PRIMEIRO número inteiro: "))
num_2 = int(input("Agora, digite o SEGUNDO número inteiro: "))

print("\nAnalisando os números...")
sleep(1.5) # Pausa breve para simular processamento

print("-" * 50)
print(f"Você digitou: {num_1} e {num_2}")
print("-" * 50)

# Compara os números e exibe a mensagem apropriada
if num_1 > num_2:
    print(f"\n🎉 O PRIMEIRO valor ({num_1}) é MAIOR que o SEGUNDO valor ({num_2}).")
elif num_1 < num_2:
    print(f"\n🎉 O SEGUNDO valor ({num_2}) é MAIOR que o PRIMEIRO valor ({num_1}).")
elif num_1 == num_2: # Condição explícita para igualdade
    print("\n🤝 Não existe valor maior, AMBOS OS NÚMEROS são IGUAIS.")

print("\n" + "=" * 50)
print("COMPARAÇÃO CONCLUÍDA!".center(50))
print("=" * 50)
