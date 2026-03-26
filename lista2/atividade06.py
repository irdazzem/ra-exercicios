a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

existencia = a + b > c and a + c > b and b + c > a
if max(a,b,c) == a:
    retangulo = a**2 == (b**2) + (c**2)
elif max(a,b,c) == b:
    retangulo = b**2 == (a**2) + (c**2)
elif max(a,b,c) == c:
    retangulo = c**2 == (a**2) + (b**2)

if existencia == True:
    if a == b and a == c:
        print("Esse triângulo é equilátero.")
    elif retangulo == True:
        if a != b and b != c and a != c:
            print("Esse triângulo é retângulo e escaleno.")
        else:
            print("Esse triângulo é retângulo e isósceles.")
    elif a != b and b != c and a != c:
        print("Esse triângulo é escaleno.")
    else:
        print("Esse triângulo é isósceles.")
else:
    print("Esses lados impossibilitam a formação de um triângulo.")






    