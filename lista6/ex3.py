conjunto1 = []
for i in range(10):
    n = int(input("Número: "))
    conjunto1.append(n)
conjunto2 = []
for i in range(10):
    quadrado = conjunto1[i] ** 2
    conjunto2.append(quadrado)
print(conjunto1)
print(conjunto2)