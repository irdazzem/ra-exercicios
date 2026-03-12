## Algoritmo Calculo de Idade
mesNascimento = int(input("Digite o seu mês de nascimento em número: "))
anoNascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2026 - anoNascimento
## Supondo mês 3
if(mesNascimento>3):
    print(f"Sua idade é: {idade-1}")
else:
    print(f"Sua idade é: {idade}")
