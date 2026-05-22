import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")

random.shuffle(alfabeto)

print(alfabeto)

letra = input("Digite uma letra: ")

posicao = int(input("Digite a posição que você acha que ela está: "))

if alfabeto[posicao] == letra:
    print("Acertou!")
else:
    print("Errou!")
    print("A letra estava na posição:", alfabeto.index(letra))