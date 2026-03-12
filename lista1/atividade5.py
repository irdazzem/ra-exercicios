## Algoritmo Calculo Idade em Meses
mesNascimento = int(input("Digite o número do mês em que você nasceu: "))
anoNascimento = int(input("Digite o seu ano de nascimento: "))
## Supondo mês 3 
difMes = 3 - mesNascimento
mesesIdade = (2026-anoNascimento)*12
meses = mesesIdade + difMes
print(f"Sua idade em meses é: {meses}")

