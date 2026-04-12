numero = int(input("Digite seu número: "))
while numero < 0:
    numero = int(input("O número deve ser inteiro e positivo.\nDigite seu número: "))
soma = 0
resultado = 0
for i in range(1, numero+1):
    soma += 1 
    resultado+=soma
    if i == numero:
        print(i, end=" ")
    else:
        print(i,end=" + ")
print("=", resultado)

