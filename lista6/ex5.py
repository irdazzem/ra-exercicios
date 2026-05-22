vetor = []
pares = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

for numero in vetor:
    if numero % 2 == 0:
        pares += 1

print("Quantidade de pares:", pares)