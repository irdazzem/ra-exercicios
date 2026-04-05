soma = 0
quantidade = 0
numero = float(input("Digite um número (-1 para encerrar): "))
while numero != -1:
    soma += numero
    quantidade += 1
    numero = float(input("Digite um número (-1 para encerrar): "))
if quantidade > 0:
    media = soma / quantidade
    print(f"Média dos números: {media}")
else:
    print("Nenhum número foi digitado.")