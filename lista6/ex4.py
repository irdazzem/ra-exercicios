posicoes = []
for i in range(8):
    numeros = int(input('Posições: '))
    posicoes.append(numeros)
print("\nDigite duas posições (0 a 7):")
x = int(input("X: "))
y = int(input("Y: "))
soma = posicoes[x] + posicoes[y]
print(f"posição[{x}] = {posicoes[x]}")
print(f"vetor[{y}] = {posicoes[y]}")
print(f"Soma: {posicoes[x]} + {posicoes[y]} = {soma}")