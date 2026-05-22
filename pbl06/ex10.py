tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for linha in tabuleiro:
    print(linha)

linha = int(input("Linha: "))
coluna = int(input("Coluna: "))

tabuleiro[linha][coluna] = "X"

print()

for linha in tabuleiro:
    print(linha)