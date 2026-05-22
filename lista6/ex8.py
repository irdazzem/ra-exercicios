notas = []
soma = 0

for i in range(15):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma += nota

media = soma / 15

print("Média geral:", media)