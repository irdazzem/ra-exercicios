pares = 0
impares = 0
i = 0
while i < 10:
    numero = int(input(f"Digite o {i+1} número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")