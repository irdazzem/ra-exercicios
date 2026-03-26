x = int(input("Digite sua coordenada x: "))
y = int(input("Digite sua coordenada y: "))

if x == 0 and y <= 10:
    print("Na fronteira")
elif y == 0 and x <=10:
    print("Na fronteira")
elif y == 10 and x <= 10:
    print("Na fronteira")
elif x == 10 and y <= 10:
    print("Na fronteira")
elif x < 0 or x > 10:
    print("Fora do quadrado")
elif y <0 or y > 10:
    print("Fora do quadrado")
else:
    print("Dentro do quadrado")

