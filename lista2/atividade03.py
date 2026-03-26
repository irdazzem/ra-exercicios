ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("Esse ano é bissexto.")
elif ano % 400 == 0:
    print("Esse ano é bissexto.")
else:
    print("Esse ano não é bissexto")
    