nome = str(input("Digite seu nome: ")).upper()

if nome == "GUILHERME":
    print("Que nome lindo você tem!")
elif nome == "PEDRO" or nome == "MARIA" or nome = "PAULO":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Claudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é normal.")

print(f"Tenha um bom dia, {nome.title()}")
