valores = []

for i in range(5):
    numero = float(input("Digite um valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)

print("Posição do maior:", valores.index(maior))
print("Posição do menor:", valores.index(menor))