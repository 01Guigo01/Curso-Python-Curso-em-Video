"""

DESESAFIO 039 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI


Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.

- Se é a hora de se alistar.

- Se já passou o tempo de alistamento.

"""

from time import sleep
from datetime import datetime

VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
ROXO = '\033[35m'
CIANO = '\033[36m'
RESET = '\033[0m'

print(f"{CIANO}{'=' * 50}{RESET}")
print(f"{AZUL}{'SISTEMA DE ALISTAMENTO MILITAR'.center(50)}{RESET}")
print(f"{CIANO}{'=' * 50}{RESET}")

sleep(1)

print(f"\n{AMARELO}Seja bem-vindo(a) ao seu verificador de alistamento!{RESET}")
print(f"Vamos descobrir sua situação perante o Serviço Militar.")
sleep(2)

current_year = datetime.now().year
print(f"\n{VERDE}O ano atual é: {current_year}{RESET}")
birth_year = int(input("Digite seu ano de nascimento (ex: 2002): "))

current_age = current_year - birth_year
year_enlistment = birth_year + 18

print(f"\n{ROXO}Analisando seus dados, aguarde um momento...{RESET}")
sleep(3)

print(f"\n{CIANO}--- RESULTADO DA ANÁLISE ---\n{RESET}")
print(f"Seu ano de nascimento: {birth_year}")
print(f"Sua idade atual: {current_age} anos")
print(f"Ano previsto para seu alistamento: {year_enlistment}\n")

if current_age < 18:
    anos_faltantes = year_enlistment - current_year
    print(f"{VERDE}>>> Ótima notícia! Você ainda vai se alistar ao serviço militar!{RESET}")
    print(f"Você tem {current_age} anos e deverá se alistar em {year_enlistment}.")
    print(f"Faltam **{anos_faltantes} ano(s)** para o seu alistamento. Prepare-se!")

elif current_age == 18:
    print(f"{AMARELO}>>> ATENÇÃO! É HORA DE SE ALISTAR!{RESET}")
    print(f"Você completou {current_age} anos este ano e deve se apresentar para o serviço militar imediatamente.")
    print(f"Não perca o prazo! Consulte o site oficial para mais informações.")

else:
    anos_atrasados = current_year - year_enlistment
    print(f"{VERMELHO}>>> ALERTA! Já passou o tempo de você se alistar!{RESET}")
    print(f"Você tem {current_age} anos e deveria ter se alistado em {year_enlistment}.")
    print(f"Você está **{anos_atrasados} ano(s)** atrasado(s). Busque regularizar sua situação o mais rápido possível!")

print(f"\n{CIANO}{'=' * 50}{RESET}")
print(f"{AZUL}{'OBRIGADO POR USAR O PROGRAMA!'.center(50)}{RESET}")
print(f"{CIANO}{'=' * 50}{RESET}")
