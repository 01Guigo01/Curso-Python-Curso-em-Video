"""

DESESAFIO 029

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.

"""

print("=" * 150)

print("RADAR ELETRÔNICO".center(50))

vel_car = int(input("Digite a velocidade do carro: "))

if vel_car > 80:
    traffic_fine = (vel_car - 80) * 7
    print(f"Você foi multado!!! A velocidade permitada é de 80 Km/h, mas você estava a {vel_car} Km/h, o valor da multa é "
          f"de R$ {traffic_fine:.2f}")
else:
    print(f"Você está a {vel_car} Km/h, esta no limite dirija em segurança!")


print("=" * 150)
