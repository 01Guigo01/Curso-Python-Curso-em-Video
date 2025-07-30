"""

DESESAFIO 041

A confedereçao Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- Até: 9 anos: MIRIM

- Até: 14 anos: INFANTIL

- Até 19 anos: JUNIOR

- Até 24 anos: SÊNIOR

- Acima: MASTER

"""
from datetime import datetime
import time

print("=" * 50)
print("✨ ANALISANDO CATEGORIAS POR IDADE ✨".center(50))
print("=" * 50)

current_year = datetime.now().year


birth_year = int(input("Para começarmos, digite seu ano de nascimento (ex: 2002): "))

current_age = current_year - birth_year

print("\nProcessando seus dados e determinando sua categoria...")
time.sleep(2)

print("\n" + "-" * 50)
print(f"RESUMO DOS DADOS:")
print(f"Ano de Nascimento: {birth_year}")
print(f"Ano Atual: {current_year}")
print(f"Sua Idade Calculada: {current_age} anos")
print("-" * 50)

if current_age <= 9:
    print(f"\n🎉 Você é um jovem entusiasta! Com {current_age} anos, sua categoria é: \033[1;36mMIRIM\033[m!") # Ciano
elif current_age > 9 and current_age <= 14:
    print(f"\n🚀 Que energia! Com {current_age} anos, sua categoria é: \033[1;34mINFANTIL\033[m!") # Azul
elif current_age > 14 and current_age <= 19:
    print(f"\n🌟 Arrasando! Com {current_age} anos, sua categoria é: \033[1;35mJUNIOR\033[m!") # Magenta
elif current_age > 19 and current_age <= 24:
    print(f"\n🏆 Experiência crescendo! Com {current_age} anos, sua categoria é: \033[1;32mSÊNIOR\033[m!") # Verde
else: # Mais de 24 anos
    print(f"\n👑 Mestre da sua categoria! Com {current_age} anos, você está na categoria: \033[1;33mMASTER\033[m!") # Amarelo (adicionei uma categoria MASTER)

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
