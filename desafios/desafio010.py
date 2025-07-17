""""
DESAFIO 010

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar

"""

money = float(input("Digite o valor para converter: "))
dolar = money / 5.55
euro = money / 6.45


print("=" * 50)

print(f"Você tem R${money:.2f} Reais\n"
      f"E pode trocar por ${dolar:.2f}\n"
      f"Ou pode trocar por €{euro:.2f}")

print("=" * 50)
