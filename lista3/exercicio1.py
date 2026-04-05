nota = float(input("Digite sua nota: ")) 
while nota < 0 or nota > 10:
    print("A nota deve estar entre 1 e 10") 
    nota = float(input("Nota valido: "))  
print("Nota validada.")

