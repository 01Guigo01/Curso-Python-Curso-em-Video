n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
res = n1 % n2
e = n1 ** n2

print(f"A soma é {s}\n"
      f"A subtração é {su}\n"
      f"A multiplicação é {m}\n"
      f"A divisão é {d:.2f}\n"
      f"A divisão inteira é {di}\n"
      f"O resto da divisão é {res}\n"
      f"A potência é {e}")
