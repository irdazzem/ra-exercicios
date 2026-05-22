valores = []

for i in range(5):
    numero = float(input("Digite um valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)
media = sum(valores) / 5

print("Valores:", valores)
print("Maior:", maior)
print("Menor:", menor)
print("Média:", media)