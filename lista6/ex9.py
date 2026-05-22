vetor = []
negativos = 0
soma_positivos = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

for numero in vetor:
    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero

print("Negativos:", negativos)
print("Soma dos positivos:", soma_positivos)