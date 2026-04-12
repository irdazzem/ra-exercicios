ninicial = int(input("Número inicial: "))
nfinal = int(input("Número final: "))
for i in range(1,11):
    print(f"{ninicial} * {i} = {ninicial*i}")
print("--------------------------")
for i in range(ninicial+1, nfinal):
    for n in range(1,11):
        print(f"{i} * {n} = {i*n}")
    print("--------------------------")
for i in range(1,11):
    print(f"{nfinal} * {i} = {nfinal*i}")

