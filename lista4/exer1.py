contador = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        contador += 1
        print(i)
print(f"Números totais: {contador}")