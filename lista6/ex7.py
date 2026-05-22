vetor = []

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

maior = max(vetor)
posicao = vetor.index(maior)

print("Vetor:", vetor)
print("Maior elemento:", maior)
print("Posição:", posicao)