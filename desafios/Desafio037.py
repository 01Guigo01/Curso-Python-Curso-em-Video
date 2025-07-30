"""

DESESAFIO 037

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal


"""
from time import sleep

print("=" * 50)
print("CONVERSOR DE BASES NUMÉRICAS".center(50))
print("=" * 50)

# 1. Leitura do número inteiro (sem tratamento de erro)
numero_inteiro = int(input("Digite um número inteiro qualquer: "))

# 2. Escolha da base de conversão (sem tratamento de erro)
print("\nEscolha a base de conversão:")
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")

opcao = int(input("Sua opção: "))

print("\nProcessando sua solicitação...")
sleep(1.5) # Um breve atraso para simular processamento

# 3. Realiza a conversão com base na opção escolhida
print("-" * 50)
print(f"Número original: {numero_inteiro}")
print("-" * 50)

if opcao == 1:
    # A função bin() retorna "0b" no início, então usamos fatiamento [2:] para remover.
    print(f"Convertido para BINÁRIO: {bin(numero_inteiro)[2:]}")
elif opcao == 2:
    # A função oct() retorna "0o" no início, então usamos fatiamento [2:] para remover.
    print(f"Convertido para OCTAL: {oct(numero_inteiro)[2:]}")
elif opcao == 3:
    # A função hex() retorna "0x" no início, então usamos fatiamento [2:] para remover.
    # Usamos .upper() para deixar as letras do hexadecimal em maiúsculo (opcional, mas comum).
    print(f"Convertido para HEXADECIMAL: {hex(numero_inteiro)[2:].upper()}")
else: # Se nenhuma das opções acima for escolhida, significa que é uma opção inválida.
    print("OPÇÃO INVÁLIDA! Por favor, escolha 1, 2 ou 3.")

print("=" * 50)
print("FIM DO PROGRAMA".center(50))
print("=" * 50)
